"""Shared types for the quadrature tournament (contracts C1–C2)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Optional, Protocol

import numpy as np
import numpy.typing as npt

FloatArray = npt.NDArray[np.floating]

# C1: batch integrand on [-1, 1]^d
IntegrandFn = Callable[[FloatArray], FloatArray]


class Integrand(Protocol):
    """Named integrand with optional exact integral for error columns."""

    name: str

    def __call__(self, x: FloatArray) -> FloatArray:
        """Evaluate f at points x with shape (n, d) → (n,)."""

    def exact_integral(self, d: int) -> Optional[float]:
        """Return closed-form integral over [-1,1]^d, or None if unknown."""


@dataclass(frozen=True)
class Result:
    """One experiment row (C2 / L3)."""

    method: str
    integrand: str
    d: int
    n_nodes_or_samples: int
    value: float
    error: Optional[float]
    seconds: float
    seed: Optional[int]
