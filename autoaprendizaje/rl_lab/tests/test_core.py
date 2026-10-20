from __future__ import annotations

import unittest

import numpy as np
import pandas as pd

from autoaprendizaje.rl_lab.core import (
    BanditConfig,
    epsilon_at_step,
    incremental_update,
    run_experiment,
)


class BanditCoreTests(unittest.TestCase):
    def test_same_seed_produces_identical_result(self) -> None:
        config = BanditConfig(steps=40, runs=25, seed=7)

        first = run_experiment(config)
        second = run_experiment(config)

        pd.testing.assert_frame_equal(first.series, second.series)
        np.testing.assert_allclose(first.final_estimates, second.final_estimates)
        self.assertEqual(first.summary, second.summary)

    def test_incremental_update_supports_both_methods(self) -> None:
        sample_average = incremental_update(
            estimate=2.0,
            reward=8.0,
            count=3,
            method="sample_average",
            alpha=0.1,
        )
        constant_alpha = incremental_update(
            estimate=2.0,
            reward=8.0,
            count=3,
            method="constant_alpha",
            alpha=0.1,
        )

        self.assertAlmostEqual(sample_average, 4.0)
        self.assertAlmostEqual(constant_alpha, 2.6)

    def test_epsilon_decay_respects_minimum(self) -> None:
        config = BanditConfig(
            policy="epsilon_decay",
            epsilon=0.5,
            epsilon_decay=0.9,
            epsilon_min=0.1,
        )

        self.assertEqual(epsilon_at_step(config, 0), 0.5)
        self.assertAlmostEqual(epsilon_at_step(config, 3), 0.3645)
        self.assertEqual(epsilon_at_step(config, 10_000), 0.1)

    def test_non_stationary_environment_changes_true_values(self) -> None:
        result = run_experiment(
            BanditConfig(
                steps=30,
                runs=20,
                seed=11,
                non_stationary=True,
                drift_std=0.05,
            )
        )

        self.assertFalse(
            np.allclose(result.initial_true_values, result.final_true_values)
        )

    def test_stationary_environment_preserves_true_values(self) -> None:
        result = run_experiment(
            BanditConfig(steps=30, runs=20, seed=11, non_stationary=False)
        )

        np.testing.assert_allclose(
            result.initial_true_values, result.final_true_values
        )

    def test_result_contains_expected_series_and_summary(self) -> None:
        result = run_experiment(BanditConfig(steps=25, runs=10))

        self.assertEqual(len(result.series), 25)
        self.assertEqual(
            list(result.series.columns),
            [
                "paso",
                "recompensa_media",
                "recompensa_acumulada_media",
                "accion_optima_pct",
                "epsilon",
            ],
        )
        self.assertTrue(
            {
                "recompensa_media",
                "recompensa_media_ultimos_100",
                "recompensa_acumulada_final",
                "accion_optima_pct",
                "accion_optima_ultimos_100_pct",
                "epsilon_final",
            }.issubset(result.summary)
        )
        self.assertTrue(result.series["accion_optima_pct"].between(0, 100).all())
        exported = result.export_frame("prueba")
        self.assertEqual(exported.loc[0, "experimento"], "prueba")
        self.assertEqual(exported.loc[0, "config_epsilon"], 0.1)
        self.assertIn("epsilon", exported.columns)

    def test_invalid_decay_configuration_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            BanditConfig(
                policy="epsilon_decay", epsilon=0.1, epsilon_min=0.2
            )


if __name__ == "__main__":
    unittest.main()
