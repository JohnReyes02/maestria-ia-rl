from __future__ import annotations

import unittest
from pathlib import Path

from streamlit.testing.v1 import AppTest

APP_PATH = Path(__file__).resolve().parents[1] / "app.py"


class StreamlitSmokeTests(unittest.TestCase):
    def test_app_opens_on_fundamentals_without_exceptions(self) -> None:
        app = AppTest.from_file(str(APP_PATH), default_timeout=15).run()

        self.assertFalse(app.exception)
        self.assertGreaterEqual(len(app.radio), 4)
        self.assertEqual(app.sidebar.radio[0].value, "Fundamentos")

    def test_guided_non_stationary_comparison_runs(self) -> None:
        app = AppTest.from_file(str(APP_PATH), default_timeout=20).run()
        app.sidebar.radio[0].set_value("Laboratorio guiado").run()
        app.selectbox[0].set_value("4. Adaptarse a la no estacionariedad").run()
        app.button[0].click().run(timeout=20)

        self.assertFalse(app.exception)
        self.assertEqual(len(app.dataframe), 1)
        table = app.dataframe[0].value
        self.assertEqual(
            list(table["experimento"]),
            ["Promedio muestral", "Alpha constante · 0,10"],
        )

    def test_sandbox_creates_history_and_downloads(self) -> None:
        app = AppTest.from_file(str(APP_PATH), default_timeout=20).run()
        app.sidebar.radio[0].set_value("Sandbox").run()
        app.button[0].click().run(timeout=20)

        self.assertFalse(app.exception)
        self.assertEqual(len(app.session_state["sandbox_results"]), 1)
        self.assertEqual(len(app.get("download_button")), 2)


if __name__ == "__main__":
    unittest.main()
