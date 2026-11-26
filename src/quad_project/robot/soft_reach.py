"""2R arm soft reachability — primary app (L5). Owner: Mario."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple

import numpy as np

from quad_project.integrands.base import NamedIntegrand, _check_batch
from quad_project.types import FloatArray


@dataclass
class Robot2RSoftReach(NamedIntegrand):
    """
    Map x in [-1,1]^2 → joint angles → forward kinematics → soft score φ(||p - p★||).

    Mario: fill in link lengths, angle limits, φ, and target. Until then this
    raises so method owners keep using test integrands.
    """

    name: str = "robot_2r_soft"
    link_lengths: Tuple[float, float] = (1.0, 1.0)
    # joint i maps from [-1,1] to [lo, hi]
    joint_limits: Tuple[Tuple[float, float], Tuple[float, float]] = (
        (-np.pi, np.pi),
        (-np.pi, np.pi),
    )
    target: Tuple[float, float] = (1.0, 0.5)
    sigma: float = 0.25

    def __call__(self, x: FloatArray) -> FloatArray:
        x = _check_batch(x)
        if x.shape[1] != 2:
            raise ValueError("robot_2r_soft expects d=2 (two joints)")
        raise NotImplementedError(
            "Mario: map x→θ, FK p(θ), return φ(||p-p★||) vectorized (see docs/contracts.md C3)"
        )

    def exact_integral(self, d: int) -> Optional[float]:
        return None
