"""Read/write Result rows as CSV (contract C2)."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, List, Optional, Union

import pandas as pd

from quad_project.types import Result

CSV_COLUMNS = [
    "method",
    "integrand",
    "d",
    "n_nodes_or_samples",
    "value",
    "error",
    "seconds",
    "seed",
]


def result_to_row(r: Result) -> dict:
    return {
        "method": r.method,
        "integrand": r.integrand,
        "d": r.d,
        "n_nodes_or_samples": r.n_nodes_or_samples,
        "value": r.value,
        "error": "" if r.error is None else r.error,
        "seconds": r.seconds,
        "seed": "" if r.seed is None else r.seed,
    }


def append_results(path: Union[str, Path], results: Iterable[Result]) -> Path:
    """Append results to CSV, creating the file with the locked header if needed."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df_new = pd.DataFrame([result_to_row(r) for r in results], columns=CSV_COLUMNS)
    if path.exists() and path.stat().st_size > 0:
        df_old = pd.read_csv(path)
        missing = [c for c in CSV_COLUMNS if c not in df_old.columns]
        if missing:
            raise ValueError(f"Existing CSV missing columns {missing}; see docs/contracts.md C2")
        df = pd.concat([df_old[CSV_COLUMNS], df_new], ignore_index=True)
    else:
        df = df_new
    df.to_csv(path, index=False)
    return path


def load_results(path: Union[str, Path]) -> pd.DataFrame:
    path = Path(path)
    df = pd.read_csv(path)
    missing = [c for c in CSV_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"CSV missing columns {missing}; see docs/contracts.md C2")
    return df[CSV_COLUMNS]


def empty_error_seed(value: float, seconds: float, **kwargs) -> Result:
    """Helper for deterministic methods (error/seed optional)."""
    return Result(
        error=kwargs.get("error"),
        seed=kwargs.get("seed"),
        value=value,
        seconds=seconds,
        method=kwargs["method"],
        integrand=kwargs["integrand"],
        d=kwargs["d"],
        n_nodes_or_samples=kwargs["n_nodes_or_samples"],
    )
