from __future__ import annotations

from pathlib import Path
from typing import Optional, Union

import matplotlib.pyplot as plt
import pandas as pd

from quad_project.results_io import load_results


def load_and_pivot(path: Union[str, Path]) -> pd.DataFrame:
    return load_results(path)


def plot_error_vs_nodes(
    path: Union[str, Path],
    *,
    integrand: Optional[str] = None,
    d: Optional[int] = None,
    ax: Optional[plt.Axes] = None,
) -> plt.Axes:
    """
    Basic error-vs-nodes chart from a results CSV.
    Works with partial/fake CSVs so Bhuvi can build demos early.
    """
    df = load_results(path)
    if integrand is not None:
        df = df[df["integrand"] == integrand]
    if d is not None:
        df = df[df["d"] == d]
    df = df.dropna(subset=["error"])
    if ax is None:
        _, ax = plt.subplots()
    for method, g in df.groupby("method"):
        g = g.sort_values("n_nodes_or_samples")
        ax.loglog(g["n_nodes_or_samples"], g["error"], marker="o", label=method)
    ax.set_xlabel("n_nodes_or_samples")
    ax.set_ylabel("|error|")
    ax.legend()
    ax.grid(True, which="both", ls=":", alpha=0.5)
    return ax
