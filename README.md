# Numerical Methods — Final Project

**Chosen topic:** Multidimensional quadrature (tensor Gauss vs Monte Carlo vs Smolyak) + 2R soft reachability.

| Doc | Purpose |
|---|---|
| [`docs/project-in-plain-words.md`](docs/project-in-plain-words.md) | **Whole project** in plain words + who does which part |
| [`docs/owners/`](docs/owners/README.md) | Personal guide per person (plain language + unlocks) |
| [`plan.md`](plan.md) | Full work split |
| [`docs/contracts.md`](docs/contracts.md) | **Locked** technical contracts (read before coding) |

## Team — open your page

| Person | Guide | Owns (short) |
|---|---|---|
| Kai | [docs/owners/kai.md](docs/owners/kai.md) | Tensor / grid method + “explosion with dimension” plots |
| Pedro | [docs/owners/pedro.md](docs/owners/pedro.md) | Sparse method + comparison + report skeleton + extras |
| Mario | [docs/owners/mario.md](docs/owners/mario.md) | Random method + robot score + slide story |
| Bhuvi | [docs/owners/bhuvi.md](docs/owners/bhuvi.md) | Live demo + Q&A cards |
| Anita | [docs/owners/anita.md](docs/owners/anita.md) | Shared test problems, CSV/plots toolkit, dependencies |

**Workflow:** `scope/<name>` branch → **PR into `main`**. See contracts for file ownership.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pytest -q
```

Domain is **\([-1,1]^d\)** (course Gauss). MC must use \(X=2U-1\) and volume \(2^d\).

## Layout

```
src/quad_project/   # importable package
  integrands/       # shared test f's
  rules/            # methods (stubs until owners implement)
  robot/            # 2R soft score (Mario)
  plotting/         # CSV → figures
results/            # experiment CSVs (see example_fake.csv)
notebooks/          # demos
docs/contracts.md   # do not change casually
plan.md             # who owns what
```

## Quick smoke

```python
from quad_project.integrands import get_integrand
import numpy as np

f = get_integrand("constant_one")
x = np.random.default_rng(0).uniform(-1, 1, size=(100, 3))
assert f(x).shape == (100,)
assert f.exact_integral(3) == 8.0
```

## Research archive

Earlier proposal pitches: [`research/proposals/`](research/proposals/).  
Group-fit brief: [`research/briefs/research-brief-group-fit.md`](research/briefs/research-brief-group-fit.md).  
Beamer chooser: [`presentation/`](presentation/).
