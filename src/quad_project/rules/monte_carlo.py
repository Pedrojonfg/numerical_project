"""Plain Monte Carlo on [-1,1]^d. Owner: Mario."""

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from quad_project.types import IntegrandFn


def monte_carlo(
    f: "IntegrandFn",
    d: int,
    n_samples: int,
    *,
    seed: Optional[int] = None,
) -> float:
    """
    Placeholder for volume-scaled MC.

    Sample U ~ Unif[0,1]^d, X = 2U - 1, estimate (2^d) * mean(f(X)).
    """
    raise NotImplementedError("Mario: implement plain Monte Carlo (see plan.md / contracts C1)")
