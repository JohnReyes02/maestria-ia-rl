"""Carga validada y de solo lectura de los resultados de Pacman."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

PACMAN_REQUIRED_COLUMNS = {
    "caso",
    "epsilon",
    "alpha",
    "gamma",
    "semilla_fija",
    "promedio_primeras_100",
    "promedio_ultimas_100",
    "promedio_evaluacion",
    "victorias",
    "derrotas",
    "tablero",
}


def load_pacman_results(path: Path, expected_rows: int | None = 11) -> pd.DataFrame:
    """Lee el resumen sin modificarlo y verifica su contrato mínimo."""

    data = pd.read_csv(path)
    missing = PACMAN_REQUIRED_COLUMNS.difference(data.columns)
    if missing:
        columns = ", ".join(sorted(missing))
        raise ValueError(f"Faltan columnas requeridas en Pacman: {columns}")
    if expected_rows is not None and len(data) != expected_rows:
        raise ValueError(
            f"Se esperaban {expected_rows} experimentos de Pacman y se encontraron {len(data)}"
        )
    if data["caso"].duplicated().any():
        raise ValueError("Los identificadores de los casos de Pacman deben ser únicos")
    if not ((data["victorias"] + data["derrotas"]) == 10).all():
        raise ValueError("Cada caso de Pacman debe contener diez evaluaciones")
    return data
