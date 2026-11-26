"""1D Gauss–Legendre on [-1, 1]. Owner: Kai."""

from __future__ import annotations

from typing import Tuple

import numpy as np
from scipy.special import roots_legendre

from quad_project.types import FloatArray


def gauss_legendre_nodes_weights(n: int) -> Tuple[FloatArray, FloatArray]:
    """
    Return nodes and weights for n-point Gauss–Legendre on [-1, 1].

    Kai: extend / wrap as needed for the tensor product scope.
    """
    if n < 1:
        raise ValueError("n must be >= 1")
    x, w = roots_legendre(n)
    return np.asarray(x, dtype=float), np.asarray(w, dtype=float)
