"""Smoke tests so the team can start against locked contracts."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest

from quad_project.integrands import get_integrand, list_integrands
from quad_project.results_io import CSV_COLUMNS, append_results, load_results
from quad_project.rules.gauss1d import gauss_legendre_nodes_weights
from quad_project.types import Result


def test_integrand_batch_api_and_domain_sanity():
    names = list_integrands()
    assert set(names) >= {"constant_one", "smooth_product", "genz_peak"}
    rng = np.random.default_rng(0)
    for d in (1, 2, 3):
        x = rng.uniform(-1.0, 1.0, size=(50, d))
        for name in names:
            f = get_integrand(name)
            y = f(x)
            assert y.shape == (50,)
            exact = f.exact_integral(d)
            assert exact is not None
            if name == "constant_one":
                assert exact == pytest.approx(2**d)


def test_smooth_product_exact_formula():
    f = get_integrand("smooth_product")
    assert f.exact_integral(4) == pytest.approx(16.0)


def test_gauss1d_nodes_on_minus_one_one():
    x, w = gauss_legendre_nodes_weights(5)
    assert x.min() >= -1.0 and x.max() <= 1.0
    assert len(x) == len(w) == 5
    # Integrate 1 exactly
    assert float(np.sum(w)) == pytest.approx(2.0)


def test_csv_roundtrip(tmp_path: Path):
    path = tmp_path / "run.csv"
    rows = [
        Result(
            method="tensor",
            integrand="constant_one",
            d=2,
            n_nodes_or_samples=9,
            value=4.0,
            error=0.0,
            seconds=0.01,
            seed=None,
        ),
        Result(
            method="monte_carlo",
            integrand="constant_one",
            d=2,
            n_nodes_or_samples=1000,
            value=3.99,
            error=0.01,
            seconds=0.02,
            seed=42,
        ),
    ]
    append_results(path, rows)
    df = load_results(path)
    assert list(df.columns) == CSV_COLUMNS
    assert len(df) == 2
    append_results(path, rows[:1])
    assert len(load_results(path)) == 3
