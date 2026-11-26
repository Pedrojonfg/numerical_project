# Multidimensional Quadrature — Work Split

People: **Kai, Pedro, Mario, Bhuvi, Anita** | Decider: **Pedro** | Challenger: **Kai**  
Load rule: aim equitable; **if anyone is overloaded, Pedro absorbs the extra** (never push overflow onto Kai / Mario / Bhuvi / Anita).  
Approval: **assignments pending team nod**; **all L1–L13 locked** (Pedro)

**Goal of this split:** five vertical scopes that each person can finish largely alone. The only shared work is a thin **contract** (agree once, then diverge). No calendars, cycles, or effort estimates in this plan.

---

## 0. Initial decisions

| ID | Status | Locked value | Notes |
|---|---|---|---|
| **L1** | **Locked** | `f(x: ndarray (n,d)) -> ndarray (n,)`; vectorized | — |
| **L2** | **Locked** | Default domain = \([-1,1]^d\) (course Gauss canon); physical maps *inside* the integrand | MC samples via \(2U-1\); sanity \(f\equiv 1\) integrates to \(2^d\) |
| **L3** | **Locked** | CSV: `method, integrand, d, n_nodes_or_samples, value, error, seconds, seed` | Empty `error` / `seed` OK |
| **L4** | **Locked (min set)** | Anita ships: smooth product, one Genz-style, \(f=1\) | **Reopenable for expansion:** anyone may add more integrands **themselves** via PR; no dumping work on Anita/others |
| **L5** | **Locked** | Primary app = **2R soft reachability** (smooth \(\phi\)); Mario owns `robot/` | Voxel / indicator / 3R / animation = `~` extras only |
| **L6** | **Locked** | Tensor (Kai) · plain MC (Mario) · Smolyak (Pedro) | Group story survives without Smolyak live demo |
| **L7** | **Locked** | `~` extras → Pedro if kept | — |
| **L8** | **Locked** | Python 3 + NumPy/SciPy/Matplotlib; `src/quad_project/` | — |
| **L9** | **Locked** | Layout as planned | — |
| **L10** | **Locked** | One writer per area; lockfile = Anita; contracts = Pedro; **all integration via PRs** | No direct drive-by commits to others’ files on `main` |
| **L11** | **Locked** | Curse + tournament + robot; MC = baseline/control | — |
| **L12** | **Locked (default cut order)** | §5 order; Pedro breaks ties | **Reopenable** if the group really must cut — revisit together, don’t silently delete someone’s must-have |
| **L13** | **Locked** | Report skeleton + comparison notebook + orphans → Pedro | — |

**Not initial locks** (owners decide alone later): local algorithms, notebook aesthetics, slide colors, test counts inside a method, robot link lengths / \(\sigma\), Smolyak level indexing details.

---

## 1. Shared contracts

After L1–L13, **nobody waits on anyone else’s unfinished method**.

| # | Contract | Source | Status |
|---|---|---|---|
| C1 | Integrand batch API + domain \([-1,1]^d\) | L1–L2 | Locked |
| C2 | Result CSV columns | L3 | Locked |
| C3 | Primary app = 2R soft reachability | L5 | Locked |
| C4 | Repo layout + ownership + **PR workflow** | L9–L10 | Locked |
| C5 | Stack | L8 | Locked |

**Independence rule:** develop on Anita’s **test integrands** first (on \([-1,1]^d\)). Plug in Mario’s robot integrand when it exists — a re-run, not a blocker.

**Domain reminders:** Gauss nodes stay native on \([-1,1]\); MC uses \(X=2U-1\), \(U\sim\mathrm{Unif}[0,1]^d\), volume factor \(2^d\); robot joint box maps into \([-1,1]^2\) *inside* Mario’s integrand.

**Optional `~` (cut first; else Pedro):** stratified / importance MC; Sobol’ QMC; 3R arm; voxel / hard indicator workspace; discontinuous “Gauss fails / MC works” experiment; arm animation.

**No-gos:** floating-point/error-theory deep dive; biology; education-demo-as-spine; pure theory with no experiments; requiring the whole group to master Smolyak.

---

## 2. One owner per scope (equitable, preference-fit)

Each person owns **one primary package** end-to-end (code + figures + the Q&A for that package). Same number of primary scopes; shared oral/report glue is split so nobody is only “helper.”

| Person | Primary scope | Done looks like | Preference fit | Writes (others read only) |
|---|---|---|---|---|
| **Kai** | **Tensor Gauss & the curse** | 1D Gauss–Legendre; product rule for \(d=2..5\); curse plots (error vs \(n\), nodes/time vs \(d\)); CSVs under `results/` for his method | Multi-D 10; geometry/math spine; MC is *not* his job | `rules/gauss1d.py`, `rules/tensor.py`, his notebooks/figures |
| **Pedro** | **Smolyak / sparse grids** (+ overflow) | Working sparse rule on shared integrands; nodes-vs-accuracy vs the *same* tests; theory he alone defends; also report skeleton, cross-method comparison notebook, and any `~` extras the group keeps | Research / OOS lane; **absorbs extra load** | `rules/smolyak.py`, `notebooks/compare_*`, report skeleton, optional `~` code |
| **Mario** | **Monte Carlo + robot integrand** | Plain MC on shared tests (multi-seed bands, high-\(d\) curves); 2R FK + soft-reachability `Integrand`; CSVs for MC (+ robot runs) | MC 8; robotics 8; applied impact | `rules/monte_carlo.py`, `robot/`, his notebooks/figures |
| **Bhuvi** | **Live demo & oral defense pack** | Demo notebook/script that **only loads `results/` CSVs`**; full Q&A card deck; backup geometry figure (e.g. torus / ball intersection) using Anita’s integrands + any ready method CSVs | Oral-friendly; short notes; easy live answers | `notebooks/demo_*`, `slides/qa_cards/`, backup-geometry notebook |
| **Anita** | **Scaffold, test suite & plot toolkit** | Repo runnable; C1–C2 implemented as stubs + 2–3 smooth test integrands (Genz-style); plotting helpers that read the CSV schema (developable with **fake** CSVs); README “how to run” | Syllabus-only; clear bounded work | `integrands/`, `plotting/`, `requirements` / lockfile, README, CSV schema doc |

**Report & slides (glue; Pedro takes slack):**
- Each person writes **their method / package section** alone.
- **Mario** owns the overall slide *story arc* (motivation → curse → tournament → robot → recommendation).
- **Bhuvi** owns merging Q&A cards and the cross-brief so everyone can answer a surface version of others’ parts.
- **Anita** owns assembling numerical **tables** in the report from `results/` CSVs.
- **Pedro** owns the report skeleton, the **cross-method comparison** notebook/figures, and any work that would otherwise overload someone else; others fill their sections.
- **Kai** reviews mathematical wording for tensor / curse claims (consult only — not a gate on merging).

---

## 3. How you avoid blocking each other

| Situation | What to do |
|---|---|
| Method not ready | Use Anita’s test integrands; never sit idle waiting for Smolyak/MC/tensor |
| Robot not ready | Method work stays on test integrands; Mario’s robot is a drop-in `Integrand` later |
| Want a comparison plot | Read CSVs from `results/`; if a method file is missing, plot the ones that exist |
| Need a new dependency | Ask Anita (lockfile owner); don’t edit lockfile in parallel |
| Shared plot helper missing | Anita accepts small PRs; or temporarily plot inside your own notebook |
| Two people edit the same file | Don’t — follow the ownership map above |

**Hotspots (single writer):** lockfile / `requirements` → Anita; CSV column names → Anita (change = re-open C2); `robot/` → Mario; each `rules/*.py` → its owner.

**Branches + PRs:** one branch per scope (`scope/tensor`, `scope/smolyak`, `scope/mc`, `scope/scaffold`, `scope/demo`); open a **PR into `main`** when the slice runs; review lightly (owner of touched hotspot); don’t push half-finished shared refactors straight to `main`. Extra integrands (L4 expansion) = PR by the person who wants them.

---

## 4. Oral Q&A ownership (70% of grade)

| Likely question | Answers |
|---|---|
| Why does product Gauss need \(n^d\) points? | **Kai** (Bhuvi has a short surface card) |
| What does 1D Gauss “exact for degree \(2n-1\)” mean? | **Kai** / **Anita** (syllabus angle) |
| Why is MC’s rate independent of dimension? | **Mario** |
| What is Smolyak combining? When does it lose? | **Pedro only** |
| Why this robot integral? | **Mario** (Bhuvi can demo the figure) |
| How do we run the demo / read the plots? | **Bhuvi** |
| Where do the test problems / CSV tables come from? | **Anita** |

Everyone should still know the **60-second shared story**; Bhuvi’s cards cover the cross-brief.

---

## 5. Cut order (if something must drop)

1. Arm animation / extra polish  
2. Stratified MC / Sobol’  
3. Discontinuous failure-case experiment (keep as a talking point)  
4. Voxel workspace (keep soft score)  
5. 3R (stay on 2R)  
6. Smolyak *live* demo (Pedro can keep a theory card; group story still = tensor vs MC + robot)  
7. **Do not drop without group nod:** shared tests, curse plot, MC baseline, one applied integral, Q&A map  

---

## 6. Decision log (minimal)

| # | Decision | Class | Constrains |
|---|---|---|---|
| D1 | L1–L13 locked by Pedro (see §0) | Team-lock | All |
| D2 | Smolyak is Pedro-only; group oral stands without it | Team-lock | Pedro, slides |
| D3 | MC is baseline/control, not the mathematical hero | Team-lock | Framing (Kai) |
| D4 | 2R soft reachability is the primary app; voxel/`~` extras optional | Team-lock | Mario, demos |
| D4b | Default domain \([-1,1]^d\) (course canon) | Team-lock | All rules + integrands |
| D5 | Overflow / orphaned work → Pedro | Team-lock | Load |
| D6 | Implementation details inside a scope | Autonomous | Owner only |

---

### Approval gate

| Person | Owns | Can start alone after C1–C2 exist? | OK? |
|---|---|---|---|
| Kai | Tensor + curse | Yes (on Anita’s test \(f\)) | ☐ |
| Pedro | Smolyak + comparison + overflow | Yes (on Anita’s test \(f\)) | ☐ |
| Mario | MC + robot integrand | Yes (MC on tests; robot in parallel) | ☐ |
| Bhuvi | Demo + Q&A cards + backup geometry | Yes (fake or partial CSVs) | ☐ |
| Anita | Scaffold + test integrands + plot toolkit | Yes (immediately) | ☐ |

**Decider sign-off:** pending  

Once approved: we can add `docs/contracts.md` and empty `scope/*` branches if you want.
