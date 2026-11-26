"""Smolyak / sparse grids on [-1,1]^d. Owner: Pedro."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from quad_project.types import IntegrandFn


def smolyak(f: "IntegrandFn", d: int, level: int) -> float:
    """Placeholder for sparse-grid quadrature A_{d,k}."""
    raise NotImplementedError("Pedro: implement Smolyak sparse grids")
