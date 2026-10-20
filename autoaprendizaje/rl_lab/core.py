"""Núcleo reproducible para experimentos de bandidos de k brazos.

La simulación no depende de Streamlit. Esto permite probarla, reutilizarla en
notebooks y extenderla con otros entornos de aprendizaje por refuerzo.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Literal

import numpy as np
import pandas as pd

Policy = Literal["greedy", "epsilon_greedy", "epsilon_decay"]
UpdateMethod = Literal["sample_average", "constant_alpha"]


@dataclass(frozen=True, slots=True)
class BanditConfig:
    """Configuración completa y reproducible de un experimento."""

    n_arms: int = 10
    steps: int = 1_000
    runs: int = 200
    seed: int = 42
    policy: Policy = "epsilon_greedy"
    epsilon: float = 0.10
    epsilon_decay: float = 0.995
    epsilon_min: float = 0.01
    update_method: UpdateMethod = "sample_average"
    alpha: float = 0.10
    non_stationary: bool = False
    drift_std: float = 0.01
    reward_std: float = 1.0

    def __post_init__(self) -> None:
        if self.n_arms < 2:
            raise ValueError("n_arms debe ser al menos 2")
        if self.steps < 1 or self.runs < 1:
            raise ValueError("steps y runs deben ser positivos")
        if not 0 <= self.epsilon <= 1:
            raise ValueError("epsilon debe estar entre 0 y 1")
        if not 0 <= self.epsilon_min <= 1:
            raise ValueError("epsilon_min debe estar entre 0 y 1")
        if self.epsilon_min > self.epsilon and self.policy == "epsilon_decay":
            raise ValueError("epsilon_min no puede superar epsilon")
        if not 0 < self.epsilon_decay <= 1:
            raise ValueError("epsilon_decay debe estar en (0, 1]")
        if not 0 < self.alpha <= 1:
            raise ValueError("alpha debe estar en (0, 1]")
        if self.drift_std < 0 or self.reward_std < 0:
            raise ValueError("las desviaciones estándar no pueden ser negativas")

    def to_dict(self) -> dict[str, int | float | str | bool]:
        """Devuelve la configuración en un formato serializable."""

        return asdict(self)


@dataclass(frozen=True, slots=True)
class ExperimentResult:
    """Series, resumen y valores finales de una simulación."""

    config: BanditConfig
    series: pd.DataFrame
    summary: dict[str, float]
    initial_true_values: np.ndarray
    final_true_values: np.ndarray
    final_estimates: np.ndarray

    def export_frame(self, experiment_name: str) -> pd.DataFrame:
        """Combina series y metadatos para descargar un experimento."""

        exported = self.series.copy()
        exported.insert(0, "experimento", experiment_name)
        for key, value in reversed(self.config.to_dict().items()):
            exported.insert(1, f"config_{key}", value)
        return exported


def epsilon_at_step(config: BanditConfig, step: int) -> float:
    """Calcula epsilon para un paso usando la política configurada."""

    if config.policy == "greedy":
        return 0.0
    if config.policy == "epsilon_greedy":
        return config.epsilon
    return max(config.epsilon_min, config.epsilon * config.epsilon_decay**step)


def incremental_update(
    estimate: float,
    reward: float,
    count: int,
    method: UpdateMethod,
    alpha: float,
) -> float:
    """Aplica Q <- Q + paso * (R - Q) para una acción seleccionada."""

    if count < 1:
        raise ValueError("count debe ser al menos 1")
    step_size = 1.0 / count if method == "sample_average" else alpha
    return estimate + step_size * (reward - estimate)


def _random_argmax(values: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    """Obtiene un máximo por fila rompiendo empates de forma aleatoria."""

    maxima = values.max(axis=1, keepdims=True)
    candidates = values == maxima
    tie_breakers = rng.random(values.shape)
    tie_breakers[~candidates] = -1.0
    return tie_breakers.argmax(axis=1)


def run_experiment(config: BanditConfig) -> ExperimentResult:
    """Simula múltiples corridas independientes de un bandido de k brazos.

    Cada brazo entrega recompensas normales alrededor de un valor real oculto.
    En el caso no estacionario, esos valores realizan una caminata aleatoria al
    terminar cada paso. La semilla controla ambiente, recompensas y política.
    """

    rng = np.random.default_rng(config.seed)
    true_values = rng.normal(0.0, 1.0, size=(config.runs, config.n_arms))
    initial_true_values = true_values.mean(axis=0).copy()
    estimates = np.zeros((config.runs, config.n_arms), dtype=float)
    counts = np.zeros((config.runs, config.n_arms), dtype=np.int64)
    run_indices = np.arange(config.runs)

    average_rewards = np.empty(config.steps, dtype=float)
    optimal_action_rates = np.empty(config.steps, dtype=float)
    epsilons = np.empty(config.steps, dtype=float)

    for step in range(config.steps):
        epsilon = epsilon_at_step(config, step)
        epsilons[step] = epsilon

        greedy_actions = _random_argmax(estimates, rng)
        random_actions = rng.integers(config.n_arms, size=config.runs)
        explore = rng.random(config.runs) < epsilon
        actions = np.where(explore, random_actions, greedy_actions)

        optimal_actions = true_values.argmax(axis=1)
        rewards = true_values[run_indices, actions] + rng.normal(
            0.0, config.reward_std, size=config.runs
        )

        counts[run_indices, actions] += 1
        if config.update_method == "sample_average":
            step_sizes = 1.0 / counts[run_indices, actions]
        else:
            step_sizes = np.full(config.runs, config.alpha)
        current = estimates[run_indices, actions]
        estimates[run_indices, actions] = current + step_sizes * (rewards - current)

        average_rewards[step] = rewards.mean()
        optimal_action_rates[step] = 100.0 * np.mean(actions == optimal_actions)

        if config.non_stationary and config.drift_std > 0:
            true_values += rng.normal(0.0, config.drift_std, size=true_values.shape)

    cumulative_rewards = np.cumsum(average_rewards)
    series = pd.DataFrame(
        {
            "paso": np.arange(1, config.steps + 1),
            "recompensa_media": average_rewards,
            "recompensa_acumulada_media": cumulative_rewards,
            "accion_optima_pct": optimal_action_rates,
            "epsilon": epsilons,
        }
    )
    tail_size = min(100, config.steps)
    summary = {
        "recompensa_media": float(average_rewards.mean()),
        "recompensa_media_ultimos_100": float(average_rewards[-tail_size:].mean()),
        "recompensa_acumulada_final": float(cumulative_rewards[-1]),
        "accion_optima_pct": float(optimal_action_rates.mean()),
        "accion_optima_ultimos_100_pct": float(
            optimal_action_rates[-tail_size:].mean()
        ),
        "epsilon_final": float(epsilons[-1]),
    }

    return ExperimentResult(
        config=config,
        series=series,
        summary=summary,
        initial_true_values=initial_true_values,
        final_true_values=true_values.mean(axis=0).copy(),
        final_estimates=estimates.mean(axis=0).copy(),
    )
