# Proposal 1: Beating the Curse of Dimensionality — Multidimensional Quadrature for Robot / Geometry Volumes

**One-line pitch:** Compare deterministic multi-D quadrature (tensor-product Gauss → Smolyak sparse grids) against Monte Carlo on the same integrals, then apply the winners to a concrete robotics/geometry volume problem that is easy to demo live.

**Suggested-topic alignment:** Instructor explicitly lists multidimensional integration and Monte Carlo as suitable (not covered in lectures). Orthogonal polynomials / Gaussian quadrature from class feed the 1D building blocks.

**Fit score (group):** ★★★★★ — strongest method consensus in the survey (multi-D avg 7.8, min 6).

---

## Why this fits the group

| Person | Fit | Why |
|---|---|---|
| **Kai** | Excellent | Rated multidimensional integration **10/10**. Owns the mathematical spine (Fubini, tensor product, curse of dimensionality, sparse grids from a textbook chapter). Geometry interest (9) matches the application. MC stays a *baseline competitor*, not the hero — mitigates his low MC score (3). |
| **Pedro** | Excellent | Can take the research-flavored OOS block alone: Smolyak construction, nested rules, or QMC / adaptive sparse grids. High scores on multi-D (8) and MC (9); loves memorable + applied impact. |
| **Mario** | Strong | Multi-D 7, MC 8, robotics 8, scientific computing 8. Natural owner of Monte Carlo experiments + variance / cost plots + robotics case study narrative for slides. Stays within short notes beyond class for his parts. |
| **Bhuvi** | Good | Method ratings mid/high (multi-D 6, MC 6). Role is oral-friendly: explain “why \(N^d\) explodes”, run demos, own Q&A on cost-vs-accuracy plots. No heavy theory required. |
| **Member 5** | Good | Syllabus-only work: reuse 1D Gauss / Simpson from lectures, implement product rules in 2D–3D, help with plotting and report tables. Zero need for sparse-grid theory. |

**Avoided landmines:** Not error-theory-centric (Kai). Not biology (Mario). Not education-demo framing (Kai). Not pure theory (Mario / Pedro veto). Application is robotics/geometry — top shared app bands.

---

## Project narrative (what you tell the professor in 30 seconds)

> “Gaussian quadrature is spectacular in 1D, but a naïve product rule dies exponentially with dimension. We implement tensor-product rules, show the curse of dimensionality on smooth test integrands, then introduce sparse (Smolyak) grids and Monte Carlo as alternatives. We finish by estimating a robot-arm reachable-volume / configuration-space integral — a real quantity engineers care about — and recommend which method to use in which dimension.”

That story is original enough (application + method tournament) while still planted on the suggested list.

---

## Mathematical core (group-shared, mostly in-syllabus or short notes)

### 1. From 1D to \(d\)D
Given a 1D rule \(I_n(g) = \sum_{i=1}^n w_i g(x_i)\) (Gauss–Legendre from class / notes):

\[
I_n^{\otimes d}(f) = \sum_{i_1=1}^n \cdots \sum_{i_d=1}^n \Big(\prod_{k=1}^d w_{i_k}\Big)\, f(x_{i_1},\ldots,x_{i_d}).
\]

Exactness for products of univariate polynomials; **node count \(n^d\)**.

### 2. The curse (experimental, not a floating-point lecture)
For a smooth \(f:[0,1]^d\to\mathbb{R}\), plot:
- absolute error vs \(n\) for fixed \(d\in\{2,3,4,5\}\);
- node count and wall-clock vs \(d\) at fixed accuracy target.

This is *cost-vs-accuracy*, not “IEEE rounding” — addresses Kai’s dislike of error-theory projects while still looking numerical-methods serious.

### 3. Monte Carlo baseline (syllabus-listed project topic)
\[
\hat{I}_N = \frac{|\Omega|}{N}\sum_{j=1}^N f(X_j),\qquad X_j\sim\mathrm{Unif}(\Omega).
\]
Standard \(\mathcal{O}(N^{-1/2})\) rate (independent of \(d\) in the probabilistic sense). Optional light variance reduction (stratified / importance) if Mario wants a clean extra — still short notes.

### 4. Pedro-only OOS block — Sparse / Smolyak grids
Smolyak combines 1D difference operators \(\Delta_i = I_i - I_{i-1}\) so that total multi-index level is bounded:

\[
A_{d,k} = \sum_{|\mathbf{i}|_1 \le d+k} (\Delta_{i_1}\otimes\cdots\otimes\Delta_{i_d}).
\]

Expected talking points for Q&A he alone must own: nested vs non-nested 1D rules, polynomial exactness of total order \(\approx 2k-1\), when sparse grids beat tensors, when MC still wins (non-smooth integrands, \(d\gtrsim 10\)).

Optional Pedro stretch (only if time): randomized QMC (Sobol’) as a fourth competitor.

---

## Applied case study (shared story)

**Primary application (recommended): planar / 3D serial arm workspace measure.**

1. Model a 2R or 3R arm with joint limits \([\theta_i^{\min},\theta_i^{\max}]\).
2. Forward kinematics \(p(\theta)\in\mathbb{R}^2\) or \(\mathbb{R}^3\).
3. Estimate a *numerical volume / area* of interest, e.g.:
   - **Task-space coverage** via Monte Carlo in joint space + voxel / indicator on a workspace grid (Mario-friendly, literature classic);
   - **Smooth surrogate integrals** such as \(\int_{[0,1]^d} \phi(\|p(\theta)-p_\star\|)\,d\theta\) (reachability soft score) so *deterministic* quadrature also applies (Kai/Pedro-friendly).

**Secondary application (backup if robotics coding slips):** analytic multi-D test suite (Genz family) + one geometric integral (volume of a torus / intersection of balls) so the method comparison still stands.

Why this app: robotics/control scored min 6 across the group; geometry scored high for Kai and Pedro; demos animate well for oral Q&A.

---

## Work packages (5 people, ~4–5 weeks)

| Package | Owner | In / out of syllabus | Deliverable |
|---|---|---|---|
| WP0 — Shared scaffold | Member 5 + Bhuvi | In | Repo, notebooks, common test integrands, plotting helpers |
| WP1 — 1D Gauss + tensor products \(d=2..5\) | Member 5 + Kai | In + short notes | Product-rule code, curse plots |
| WP2 — Monte Carlo (+ optional stratification) | Mario | Suggested topic / short notes | Estimators, CI / variability over seeds, high-\(d\) curves |
| WP3 — Sparse grids / Smolyak | **Pedro alone** | **OOS / research** | Implementation + theory slides he can defend |
| WP4 — Robot / geometry case study | Mario + Bhuvi (+ Kai review) | Applied; FK is high-school trig | FK model, volume/score integrals, comparison table |
| WP5 — Oral story & report | All (Bhuvi coordinates Q&A cards) | — | 15–20 min talk; 1-page “who owns what” for interruptions |

**Complexity for a group of 5:** Method tournament (3–4 algorithms) × dimension sweep × one applied case is clearly “more substantial” as the rubric expects for larger groups — without inventing fake complexity.

---

## Experiments that look good in Q&A

1. Heatmap: error vs \((d, n)\) for tensor Gauss on a smooth product integrand.  
2. Nodes vs accuracy: tensor vs Smolyak vs MC at \(d=5,6\).  
3. Break-even chart: “For this smoothness class, MC overtakes tensors at dimension ___.”  
4. Robot demo: arm animation + estimated workspace measure converging.  
5. Failure case (insight points): discontinuous indicator → Gauss bad, MC fine — shows critical thinking.

---

## Oral defense map (70% of grade)

| Likely question | Who answers |
|---|---|
| Why does product Gauss need \(n^d\) points? | Kai / Member 5 |
| What does “exact for polynomials of degree \(2n-1\)” mean in 1D? | Member 5 |
| Why is MC’s rate independent of dimension? | Mario |
| What is Smolyak actually combining? | **Pedro only** |
| Why did you choose this robot integral? | Mario / Bhuvi |
| When would you *not* use sparse grids? | Pedro (+ Kai) |

Everyone can answer a surface version of WP1–WP2; only Pedro needs the sparse-grid deep cut.

---

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Sparse grids too hard for the group | Encapsulate as Pedro-only; group presents tensor vs MC even if Smolyak slips |
| Robot volume coding eats time | Fall back to Genz tests + torus volume; keep robotics as motivation slides |
| Another group claims “Monte Carlo” | Differentiate: *multi-D method contest + robotics volume*; claim topic early with instructor |
| Kai bored by MC | Frame MC as the high-\(d\) control method, not the theory focus |

---

## Recommended stack

- Python, NumPy/SciPy (`scipy.special.roots_legendre`), Matplotlib  
- Optional: `torch`/`jax` unnecessary  
- References: course Gauss slides; a short Smolyak note (e.g. Alexanderian sparse quadrature note); Heiss & Winschel sparse-grid intuition; robot workspace MC papers for motivation only  

---

## Verdict

Best default pick if the group wants **maximum shared enthusiasm + clear Pedro OOS lane + oral-friendly demos**. Claim early: multidimensional integration topics will be popular.
