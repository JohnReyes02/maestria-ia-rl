from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import pandas as pd

from autoaprendizaje.rl_lab.pacman import load_pacman_results

PROJECT_ROOT = Path(__file__).resolve().parents[3]
PACMAN_RESULTS = (
    PROJECT_ROOT / "laboratorios" / "modulo_1" / "resultados" / "resumen.csv"
)


class PacmanDataTests(unittest.TestCase):
    def test_repository_summary_has_expected_eleven_cases(self) -> None:
        data = load_pacman_results(PACMAN_RESULTS)

        self.assertEqual(len(data), 11)
        self.assertEqual(data["caso"].nunique(), 11)
        self.assertEqual(
            set(data["tablero"]), {"smallGrid", "mediumGrid", "mediumClassic"}
        )

    def test_missing_columns_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.csv"
            pd.DataFrame({"caso": ["01_base"]}).to_csv(path, index=False)

            with self.assertRaisesRegex(ValueError, "Faltan columnas"):
                load_pacman_results(path, expected_rows=None)


if __name__ == "__main__":
    unittest.main()
