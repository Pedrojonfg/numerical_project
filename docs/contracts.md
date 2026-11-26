# Locked contracts (L1–L13)

**Decider:** Pedro  
**Status:** Locked — reopen only with Pedro (+ affected owners).  
**Work plan:** [`../plan.md`](../plan.md)

Do not change these in a random PR. Implement against them.

---

## C1 — Integrand API & domain (L1, L2)

- **Signature:** `f(x: np.ndarray) -> np.ndarray`
  - `x` has shape `(n, d)` — `n` points in dimension `d`
  - return shape `(n,)` — one value per point
  - **vectorized** (NumPy ops; no required Python loop over points)
- **Default domain:** \([-1,1]^d\) (course Gauss–Legendre canon)
- **Physical / joint domains:** map into \([-1,1]^d\) **inside** the integrand (callers always pass points in the default cube)
- **Exact integral of `f ≡ 1`:** \(2^d\)

### Method notes

| Method | Domain handling |
|---|---|
| Tensor / 1D Gauss (Kai) | Nodes/weights native on \([-1,1]\) |
| Monte Carlo (Mario) | Draw \(U\sim\mathrm{Unif}[0,1]^d\), set \(X = 2U - 1\); multiply sample mean by volume \(2^d\) |
| Smolyak (Pedro) | Same cube; nested/non-nested choice is autonomous inside the scope |
| Robot soft score (Mario) | Joint box \(\to[-1,1]^2\) inside `robot/` integrand |

---

## C2 — Result CSV schema (L3)

Every experiment appends rows (or writes a file) under `results/` with **exactly** these columns:

| Column | Type / meaning |
|---|---|
| `method` | e.g. `tensor`, `monte_carlo`, `smolyak` |
| `integrand` | registry name, e.g. `constant_one`, `smooth_product`, `genz_peak`, `robot_2r_soft` |
| `d` | dimension (int) |
| `n_nodes_or_samples` | quadrature nodes or MC samples (int) |
| `value` | estimated integral (float) |
| `error` | absolute error vs known truth, or empty |
| `seconds` | wall time for that run (float) |
| `seed` | RNG seed for stochastic methods, or empty |

Helpers: `quad_project.results_io` (read/write). Schema changes need Pedro.

---

## C3 — Primary application (L5)

- **Must:** planar **2R** arm + **soft reachability** integrand  
  \(f(\theta) = \phi(\|p(\theta) - p_\star\|)\) with smooth \(\phi\) (e.g. \(\exp(-r^2/\sigma^2)\)).
- **Owner:** Mario (`src/quad_project/robot/`)
- **Extras (`~` only):** voxel / hard indicator workspace, 3R, animation

Others only **call** the published integrand; they do not edit robot internals.

---

## C4 — Layout, ownership, PRs (L9, L10)

```
src/quad_project/
  integrands/   # Anita (+ expansions via PR by the person who wants them)
  rules/        # one file (or module) per method owner
  robot/        # Mario
  plotting/     # Anita
results/        # CSV outputs (gitkeep; large runs optional locally)
notebooks/      # demos / owner notebooks
slides/         # Mario story arc; Bhuvi qa_cards/
report/         # Pedro skeleton; each fills their section
docs/           # contracts (Pedro)
```

| Area | Writer | Others |
|---|---|---|
| `integrands/`, `plotting/`, `requirements.txt` / lockfile | Anita | PR only |
| `rules/gauss1d.py`, `rules/tensor.py` | Kai | read / import |
| `rules/monte_carlo.py`, `robot/` | Mario | read / import |
| `rules/smolyak.py`, `notebooks/compare_*`, report skeleton | Pedro | read / import |
| `notebooks/demo_*`, `slides/qa_cards/` | Bhuvi | PR only |
| `docs/contracts.md` | Pedro | discuss before change |

**Workflow:** branch `scope/<name>` → **PR into `main`**. No drive-by commits on someone else’s hotspot.

---

## C5 — Stack (L8)

- Python 3
- NumPy, SciPy, Matplotlib
- Install: `pip install -e ".[dev]"` from repo root (see `pyproject.toml`)
- No JAX/Torch unless Pedro adds them

---

## Method set & framing (L6, L7, L11)

| Must | Owner |
|---|---|
| Tensor-product Gauss + curse plots | Kai |
| Plain Monte Carlo (baseline / control, not the hero) | Mario |
| Smolyak / sparse grids | Pedro |

Story: curse of dimensionality → method tournament → robot soft score → recommendation.  
`~` extras (stratified MC, QMC, discontinuous failure case, …): cut first, or **Pedro** implements if kept.

---

## Test integrand minimum set (L4)

Anita’s baseline (names are CSV `integrand=` values):

| Name | Role | Known integral on \([-1,1]^d\) |
|---|---|---|
| `constant_one` | Sanity | \(2^d\) |
| `smooth_product` | Separable smooth | \(2^d\) for \(\prod_i(1+x_i)\) |
| `genz_peak` | Non-separable-ish peak | see `exact_integral` in code / docstring |

**Expansion:** anyone may add integrands **themselves** via PR. Do not assign extra integrand work to Anita.

---

## Cuts & overflow (L12, L13)

Default cut order: animation → stratified/QMC → discontinuous experiment → voxels → 3R → Smolyak *live* demo (keep Pedro theory card).  
**Reopen** the cut list with the group if a must-have is at risk — don’t silently delete someone’s core scope.

Overflow / glue (comparison notebook, report skeleton, orphans) → **Pedro**.
