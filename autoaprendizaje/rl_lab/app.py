"""Interfaz web local de RL Lab."""

from __future__ import annotations

import json
import sys
from dataclasses import replace
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from autoaprendizaje.rl_lab.core import BanditConfig, ExperimentResult, run_experiment
from autoaprendizaje.rl_lab.pacman import load_pacman_results

PACMAN_RESULTS = (
    PROJECT_ROOT / "laboratorios" / "modulo_1" / "resultados" / "resumen.csv"
)
COLORS = ["#127C78", "#E07A3F", "#6C5FB5", "#C94F6D", "#4C78A8"]


st.set_page_config(
    page_title="RL Lab · Autoaprendizaje",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    :root {
        --ink: #18302d;
        --muted: #5b6f6b;
        --paper: #f7faf7;
        --mint: #dff2e8;
        --coral: #f4a261;
        --teal: #127c78;
    }
    .stApp { background: linear-gradient(145deg, #f7faf7 0%, #f4f0e8 100%); }
    [data-testid="stMain"], [data-testid="stMain"] p,
    [data-testid="stMain"] li, [data-testid="stMain"] label,
    [data-testid="stMain"] h1, [data-testid="stMain"] h2,
    [data-testid="stMain"] h3 { color: #18302d; }
    [data-testid="stSidebar"] { background: #173c3a; }
    [data-testid="stSidebar"] * { color: #f7fbf8; }
    .rl-hero {
        border: 1px solid rgba(18, 124, 120, .18);
        border-radius: 24px;
        padding: 2rem 2.2rem;
        margin-bottom: 1.25rem;
        background: linear-gradient(115deg, #e0f3e9 0%, #fff8ed 100%);
        box-shadow: 0 12px 36px rgba(24, 48, 45, .08);
    }
    .rl-kicker { color: #127c78; font-weight: 800; letter-spacing: .12em; }
    .rl-hero h1 { color: #18302d; margin: .25rem 0 .5rem; font-size: 2.65rem; }
    .rl-hero p { color: #4d625e; max-width: 760px; font-size: 1.08rem; }
    .concept-card {
        min-height: 155px; border-radius: 18px; padding: 1rem 1.1rem;
        background: rgba(255,255,255,.76); border: 1px solid rgba(18,124,120,.14);
    }
    .concept-card h3 {
        color: #127c78; margin-top: 0; font-size: 1.35rem;
        word-break: keep-all; overflow-wrap: normal;
    }
    .concept-card p { color: #4d625e; }
    .formula-box {
        border-left: 5px solid #e07a3f; padding: .8rem 1rem;
        background: #fff8ed; border-radius: 8px; margin: .8rem 0;
    }
    div[data-testid="stMetric"] {
        background: rgba(255,255,255,.78); border: 1px solid rgba(18,124,120,.12);
        padding: .8rem; border-radius: 16px;
    }
    div.stButton > button[kind="primary"],
    div.stFormSubmitButton > button[kind="primary"] {
        background: #127c78; border-color: #127c78; color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def hero(kicker: str, title: str, description: str) -> None:
    st.markdown(
        f"""
        <section class="rl-hero">
          <div class="rl-kicker">{kicker}</div>
          <h1>{title}</h1>
          <p>{description}</p>
        </section>
        """,
        unsafe_allow_html=True,
    )


def plot_results(results: list[tuple[str, ExperimentResult]]) -> plt.Figure:
    """Compara recompensa y selección óptima en una figura."""

    figure, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
    for index, (name, result) in enumerate(results):
        color = COLORS[index % len(COLORS)]
        axes[0].plot(
            result.series["paso"],
            result.series["recompensa_media"].rolling(20, min_periods=1).mean(),
            label=name,
            color=color,
            linewidth=2,
        )
        axes[1].plot(
            result.series["paso"],
            result.series["accion_optima_pct"].rolling(20, min_periods=1).mean(),
            label=name,
            color=color,
            linewidth=2,
        )
    axes[0].set_ylabel("Recompensa media")
    axes[0].set_title("Recompensa por paso · media móvil de 20 pasos")
    axes[1].set_ylabel("Acción óptima (%)")
    axes[1].set_xlabel("Paso")
    axes[1].set_ylim(0, 100)
    axes[1].set_title("Frecuencia de selección de la mejor acción")
    for axis in axes:
        axis.grid(alpha=0.2)
        axis.legend(frameon=False, ncol=2)
    figure.tight_layout()
    return figure


def results_table(results: list[tuple[str, ExperimentResult]]) -> pd.DataFrame:
    rows = []
    for name, result in results:
        rows.append(
            {
                "experimento": name,
                "recompensa media": result.summary["recompensa_media"],
                "últimos 100": result.summary["recompensa_media_ultimos_100"],
                "acción óptima (%)": result.summary["accion_optima_pct"],
                "acción óptima últimos 100 (%)": result.summary[
                    "accion_optima_ultimos_100_pct"
                ],
                "epsilon final": result.summary["epsilon_final"],
            }
        )
    return pd.DataFrame(rows)


def render_fundamentals() -> None:
    hero(
        "01 · FUNDAMENTOS",
        "Antes del algoritmo, entiende el ciclo",
        "Un agente observa, actúa y recibe consecuencias. La meta de esta sección "
        "es reconocer cada pieza antes de ajustar parámetros.",
    )

    st.subheader("El ciclo de aprendizaje por refuerzo")
    concepts = [
        ("Agente", "Quien toma decisiones para alcanzar un objetivo."),
        ("Entorno", "El mundo que responde a las acciones del agente."),
        ("Estado", "La información disponible para decidir en un instante."),
        ("Acción", "Una decisión que el agente puede ejecutar."),
        ("Recompensa", "La señal inmediata que evalúa una transición."),
        ("Política", "La regla que relaciona estados u observaciones con acciones."),
        ("Valor", "La recompensa futura esperada desde una situación o acción."),
        ("Dinámica", "Cómo cambia el entorno después de una acción."),
    ]
    for row_start in range(0, len(concepts), 4):
        columns = st.columns(4)
        for column, (title, text) in zip(columns, concepts[row_start : row_start + 4]):
            with column:
                st.markdown(
                    f'<div class="concept-card"><h3>{title}</h3><p>{text}</p></div>',
                    unsafe_allow_html=True,
                )

    st.divider()
    st.subheader("Comprueba la intuición: robot aspirador")
    st.write(
        "El robot decide entre avanzar, girar o aspirar. Consume batería, obtiene "
        "una recompensa al retirar suciedad y percibe su posición y sensores cercanos."
    )
    with st.form("fundamentals_quiz"):
        q_agent = st.radio(
            "¿Cuál es el agente?",
            ["La habitación", "El robot", "La suciedad"],
            horizontal=True,
        )
        q_state = st.radio(
            "¿Cuál opción describe mejor el estado?",
            [
                "La posición, batería y sensores disponibles",
                "La recompensa total al final",
                "Únicamente la acción aspirar",
            ],
        )
        q_policy = st.radio(
            "¿Qué representa la política?",
            [
                "La regla usada para escoger una acción con la información actual",
                "La forma física de la habitación",
                "El nivel máximo de batería",
            ],
        )
        checked = st.form_submit_button("Comprobar respuestas", type="primary")
    if checked:
        correct = sum(
            [
                q_agent == "El robot",
                q_state == "La posición, batería y sensores disponibles",
                q_policy
                == "La regla usada para escoger una acción con la información actual",
            ]
        )
        if correct == 3:
            st.success("3/3. Ya separas quién decide, qué observa y cómo elige.")
        else:
            st.warning(
                f"{correct}/3. Pista: el agente decide, el estado informa y la política elige."
            )

    st.markdown(
        """
        <div class="formula-box">
        <strong>Puente hacia los bandidos:</strong> no existe un estado cambiante;
        el agente repite una elección y estima el valor de cada acción a partir de
        recompensas inciertas.
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_pacman() -> None:
    hero(
        "02 · CASO REAL",
        "Pacman: leer resultados sin exagerar conclusiones",
        "Explora las once configuraciones que ya ejecutaste. Aquí analizamos datos "
        "guardados; no se inicia ningún entrenamiento nuevo.",
    )
    try:
        data = load_pacman_results(PACMAN_RESULTS)
    except (OSError, ValueError) as error:
        st.error(f"No fue posible cargar el resumen de Pacman: {error}")
        return

    selected_boards = st.multiselect(
        "Tableros",
        options=data["tablero"].drop_duplicates().tolist(),
        default=data["tablero"].drop_duplicates().tolist(),
    )
    filtered = data[data["tablero"].isin(selected_boards)].copy()
    if filtered.empty:
        st.info("Selecciona al menos un tablero para comenzar el análisis.")
        return

    metric_columns = st.columns(3)
    metric_columns[0].metric("Configuraciones", len(filtered))
    metric_columns[1].metric("Victorias", int(filtered["victorias"].sum()))
    best = filtered.loc[filtered["promedio_evaluacion"].idxmax()]
    metric_columns[2].metric(
        "Mayor promedio observado",
        f"{best['promedio_evaluacion']:.1f}",
        help=f"Caso {best['caso']}; es una observación, no una prueba de superioridad.",
    )

    plot_data = filtered.set_index("caso")[
        ["promedio_primeras_100", "promedio_ultimas_100", "promedio_evaluacion"]
    ]
    plot_data.columns = ["Primeras 100", "Últimas 100", "Evaluación"]
    figure, axis = plt.subplots(figsize=(11, max(4.5, len(filtered) * 0.42)))
    plot_data.plot.barh(ax=axis, color=COLORS[:3])
    axis.axvline(0, color="#18302d", linewidth=0.8)
    axis.set_xlabel("Recompensa / puntaje promedio")
    axis.set_ylabel("Caso")
    axis.legend(frameon=False, ncol=3)
    axis.grid(axis="x", alpha=0.2)
    figure.tight_layout()
    st.pyplot(figure, width="stretch")
    plt.close(figure)

    visible_columns = [
        "caso",
        "tablero",
        "epsilon",
        "alpha",
        "gamma",
        "promedio_primeras_100",
        "promedio_ultimas_100",
        "promedio_evaluacion",
        "victorias",
        "derrotas",
    ]
    st.dataframe(filtered[visible_columns], hide_index=True, width="stretch")

    st.info(
        "**Hecho observado:** cada configuración usa una semilla fija y diez juegos "
        "de evaluación. **Límite:** estas corridas permiten describir diferencias, "
        "pero no afirmar que un parámetro es universalmente superior."
    )
    with st.expander("Preguntas para interpretar el experimento"):
        st.markdown(
            """
            - ¿Qué cambia entre las primeras y las últimas 100 partidas?
            - ¿Por qué una recompensa de entrenamiento no equivale al puntaje de evaluación?
            - ¿Qué ocurre con epsilon y alpha cuando termina el entrenamiento?
            - ¿Es válida una comparación directa si también cambia el tablero?
            """
        )


def guided_presets(topic: str) -> tuple[list[tuple[str, BanditConfig]], str]:
    base = BanditConfig()
    if topic == "1. Explorar o explotar":
        return (
            [
                ("Greedy · ε=0", replace(base, policy="greedy")),
                ("ε-greedy · ε=0,10", base),
            ],
            "Greedy puede comprometerse pronto con una estimación afortunada; "
            "epsilon-greedy sigue reservando algunas decisiones para explorar.",
        )
    if topic == "2. Reducir la exploración":
        return (
            [
                ("ε fijo · 0,10", base),
                ("ε decay · 0,10→0,01", replace(base, policy="epsilon_decay")),
            ],
            "El decay explora más al comienzo y disminuye gradualmente hasta "
            "epsilon mínimo. Observa si esa reducción ocurre demasiado pronto.",
        )
    if topic == "3. Detectar un mundo cambiante":
        constant = replace(base, update_method="constant_alpha")
        return (
            [
                ("Estacionario", constant),
                (
                    "No estacionario",
                    replace(constant, non_stationary=True, drift_std=0.01),
                ),
            ],
            "En el segundo entorno, el valor real de cada brazo cambia después "
            "de cada paso mediante una caminata aleatoria.",
        )
    return (
        [
            (
                "Promedio muestral",
                replace(base, non_stationary=True, update_method="sample_average"),
            ),
            (
                "Alpha constante · 0,10",
                replace(base, non_stationary=True, update_method="constant_alpha"),
            ),
        ],
        "El promedio muestral conserva toda la historia. Alpha constante da un "
        "peso sostenido a recompensas recientes y suele adaptarse mejor al cambio.",
    )


def render_guided_lab() -> None:
    hero(
        "03 · LABORATORIO GUIADO",
        "Bandidos: aprende cambiando una idea a la vez",
        "Compara estrategias bajo la misma semilla. Las curvas promedian 200 "
        "corridas para mostrar tendencias y no una única historia afortunada.",
    )
    topic = st.selectbox(
        "Elige una pregunta",
        [
            "1. Explorar o explotar",
            "2. Reducir la exploración",
            "3. Detectar un mundo cambiante",
            "4. Adaptarse a la no estacionariedad",
        ],
    )
    presets, intuition = guided_presets(topic)
    st.write(intuition)

    if st.button("Ejecutar comparación guiada", type="primary"):
        with st.spinner("Simulando decisiones y recompensas..."):
            st.session_state["guided_results"] = [
                (name, run_experiment(config)) for name, config in presets
            ]
            st.session_state["guided_topic"] = topic

    results = st.session_state.get("guided_results")
    if results and st.session_state.get("guided_topic") == topic:
        figure = plot_results(results)
        st.pyplot(figure, width="stretch")
        plt.close(figure)
        st.dataframe(
            results_table(results).style.format(precision=3),
            hide_index=True,
            width="stretch",
        )
        st.markdown(
            """
            <div class="formula-box">
            <strong>Actualización incremental:</strong>
            Q<sub>n+1</sub>(a) = Q<sub>n</sub>(a) + α [R<sub>n</sub> − Q<sub>n</sub>(a)].
            Con promedio muestral, α = 1/N(a); con alpha constante, el paso no
            desaparece y las observaciones recientes conservan influencia.
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.caption("Ejecuta la comparación para ver las curvas y métricas.")


def render_sandbox() -> None:
    hero(
        "04 · SANDBOX",
        "Diseña y compara tus propios experimentos",
        "Controla una variable, formula una predicción y comprueba qué ocurre. "
        "El historial existe solo mientras esta sesión permanezca abierta.",
    )
    if "sandbox_results" not in st.session_state:
        st.session_state["sandbox_results"] = []

    with st.form("sandbox_form"):
        first, second, third = st.columns(3)
        with first:
            experiment_name = st.text_input(
                "Nombre",
                value=f"Experimento {len(st.session_state['sandbox_results']) + 1}",
            )
            n_arms = st.slider("Número de brazos", 2, 20, 10)
            steps = st.slider("Pasos", 100, 3_000, 1_000, 100)
            runs = st.slider("Corridas", 10, 500, 200, 10)
            seed = st.number_input("Semilla", min_value=0, value=42, step=1)
        with second:
            policy_label = st.selectbox(
                "Política",
                ["Greedy", "Epsilon-greedy", "Epsilon decay"],
                index=1,
            )
            epsilon = st.slider("Epsilon inicial", 0.0, 1.0, 0.10, 0.01)
            epsilon_min = st.slider("Epsilon mínimo", 0.0, 1.0, 0.01, 0.01)
            epsilon_decay = st.slider(
                "Factor de decay", 0.900, 1.000, 0.995, 0.001, format="%.3f"
            )
        with third:
            update_label = st.selectbox(
                "Actualización",
                ["Promedio muestral", "Alpha constante"],
            )
            alpha = st.slider("Alpha", 0.01, 1.0, 0.10, 0.01)
            environment_label = st.selectbox(
                "Entorno", ["Estacionario", "No estacionario"]
            )
            drift_std = st.slider("Deriva por paso", 0.0, 0.10, 0.01, 0.005)
            reward_std = st.slider("Ruido de recompensa", 0.0, 3.0, 1.0, 0.1)
        submitted = st.form_submit_button("Ejecutar experimento", type="primary")

    if submitted:
        policies = {
            "Greedy": "greedy",
            "Epsilon-greedy": "epsilon_greedy",
            "Epsilon decay": "epsilon_decay",
        }
        updates = {
            "Promedio muestral": "sample_average",
            "Alpha constante": "constant_alpha",
        }
        try:
            config = BanditConfig(
                n_arms=n_arms,
                steps=steps,
                runs=runs,
                seed=int(seed),
                policy=policies[policy_label],
                epsilon=epsilon,
                epsilon_decay=epsilon_decay,
                epsilon_min=epsilon_min,
                update_method=updates[update_label],
                alpha=alpha,
                non_stationary=environment_label == "No estacionario",
                drift_std=drift_std,
                reward_std=reward_std,
            )
        except ValueError as error:
            st.error(str(error))
        else:
            with st.spinner("Ejecutando experimento..."):
                result = run_experiment(config)
            st.session_state["sandbox_results"].append((experiment_name, result))
            st.success(f"{experiment_name} agregado a la comparación.")

    history: list[tuple[str, ExperimentResult]] = st.session_state["sandbox_results"]
    if not history:
        st.info("Aún no hay experimentos. Empieza con los valores sugeridos.")
        return

    figure = plot_results(history)
    st.pyplot(figure, width="stretch")
    plt.close(figure)
    st.dataframe(
        results_table(history).style.format(precision=3),
        hide_index=True,
        width="stretch",
    )

    combined = pd.concat(
        [result.export_frame(name) for name, result in history], ignore_index=True
    )
    json_payload = [
        {
            "experimento": name,
            "configuracion": result.config.to_dict(),
            "resumen": result.summary,
        }
        for name, result in history
    ]
    download_columns = st.columns([1, 1, 2])
    download_columns[0].download_button(
        "Descargar CSV",
        data=combined.to_csv(index=False).encode("utf-8"),
        file_name="rl_lab_experimentos.csv",
        mime="text/csv",
    )
    download_columns[1].download_button(
        "Descargar JSON",
        data=json.dumps(json_payload, ensure_ascii=False, indent=2).encode("utf-8"),
        file_name="rl_lab_resumen.json",
        mime="application/json",
    )
    if download_columns[2].button("Limpiar historial"):
        st.session_state["sandbox_results"] = []
        st.rerun()


st.sidebar.markdown("## 🧭 RL Lab")
st.sidebar.caption("Laboratorio independiente de autoaprendizaje")
section = st.sidebar.radio(
    "Recorrido",
    ["Fundamentos", "Caso Pacman", "Laboratorio guiado", "Sandbox"],
)
st.sidebar.divider()
st.sidebar.markdown(
    "**Idea de trabajo**\n\n1. Predice qué ocurrirá.\n2. Cambia una variable."
    "\n3. Ejecuta con semilla fija.\n4. Explica el resultado."
)

if section == "Fundamentos":
    render_fundamentals()
elif section == "Caso Pacman":
    render_pacman()
elif section == "Laboratorio guiado":
    render_guided_lab()
else:
    render_sandbox()
