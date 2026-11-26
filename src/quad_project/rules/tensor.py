"""Tensor-product Gauss on [-1,1]^d. Owner: Kai — implement the curse demo here."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from quad_project.types import FloatArray, IntegrandFn


def tensor_gauss(f: "IntegrandFn", d: int, n_per_dim: int) -> float:
    """
    Placeholder for product-rule quadrature.

    Contract: evaluate ``f`` on a batch of shape (n_nodes, d) with nodes in [-1,1]^d.
    """
    raise NotImplementedError("Kai: implement tensor-product Gauss (see plan.md S1)")
