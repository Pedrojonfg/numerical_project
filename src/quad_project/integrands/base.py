from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import numpy as np

from quad_project.types import FloatArray


def _check_batch(x: FloatArray) -> FloatArray:
    x = np.asarray(x, dtype=float)
    if x.ndim != 2:
        raise ValueError(f"Expected x with shape (n, d), got {x.shape}")
    return x


@dataclass
class NamedIntegrand:
    name: str

    def __call__(self, x: FloatArray) -> FloatArray:  # pragma: no cover - abstract
        raise NotImplementedError

    def exact_integral(self, d: int) -> Optional[float]:
        return None


@dataclass
class ConstantOne(NamedIntegrand):
    """f(x) = 1. Exact integral over [-1,1]^d is 2^d."""

    name: str = "constant_one"

    def __call__(self, x: FloatArray) -> FloatArray:
        x = _check_batch(x)
        return np.ones(x.shape[0], dtype=float)

    def exact_integral(self, d: int) -> Optional[float]:
        return float(2**d)


@dataclass
class SmoothProduct(NamedIntegrand):
    """f(x) = prod_i (1 + x_i). Separable; exact integral 2^d on [-1,1]^d."""

    name: str = "smooth_product"

    def __call__(self, x: FloatArray) -> FloatArray:
        x = _check_batch(x)
        return np.prod(1.0 + x, axis=1)

    def exact_integral(self, d: int) -> Optional[float]:
        # int_{-1}^1 (1+x) dx = 2, so product rule → 2^d
        return float(2**d)


@dataclass
class GenzPeak(NamedIntegrand):
    """
    Gaussian-like peak on [-1,1]^d (Genz-inspired, adapted from [0,1] formulas).

    f(x) = exp(-sum_i a_i^2 (x_i - u_i)^2)

    Default a_i = 5, u_i = 0 (peak at origin). Exact integral via product of
    1D Gaussian integrals truncated to [-1,1] (scipy).
    """

    name: str = "genz_peak"
    a: float = 5.0
    u: float = 0.0

    def __call__(self, x: FloatArray) -> FloatArray:
        x = _check_batch(x)
        a = self.a
        u = self.u
        return np.exp(-np.sum((a * (x - u)) ** 2, axis=1))

    def exact_integral(self, d: int) -> Optional[float]:
        # Product of identical 1D integrals int_{-1}^1 exp(-a^2 (x-u)^2) dx
        from scipy.special import erf

        a = float(self.a)
        u = float(self.u)
        if a == 0.0:
            return float(2**d)
        # int exp(-a^2 (x-u)^2) dx = (sqrt(pi)/(2a)) * [erf(a(b-u)) - erf(a(c-u))]
        sqrt_pi = np.sqrt(np.pi)
        one_d = (sqrt_pi / (2.0 * a)) * (
            erf(a * (1.0 - u)) - erf(a * (-1.0 - u))
        )
        return float(one_d**d)
