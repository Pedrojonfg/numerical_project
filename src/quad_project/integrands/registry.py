from __future__ import annotations

from typing import Dict, List

from quad_project.integrands.base import ConstantOne, GenzPeak, NamedIntegrand, SmoothProduct

INTEGRANDS: Dict[str, NamedIntegrand] = {
    "constant_one": ConstantOne(),
    "smooth_product": SmoothProduct(),
    "genz_peak": GenzPeak(),
}


def get_integrand(name: str) -> NamedIntegrand:
    try:
        return INTEGRANDS[name]
    except KeyError as exc:
        known = ", ".join(sorted(INTEGRANDS))
        raise KeyError(f"Unknown integrand {name!r}. Known: {known}") from exc


def list_integrands() -> List[str]:
    return sorted(INTEGRANDS)
