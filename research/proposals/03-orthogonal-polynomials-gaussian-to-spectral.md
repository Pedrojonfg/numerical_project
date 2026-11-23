# Proposal 3: Orthogonal Polynomials — From Gaussian Quadrature to Chebyshev Spectral Methods

**One-line pitch:** Build the theory and code for classical orthogonal polynomials and Gaussian quadrature (suggested topic), show why they crush composite Newton–Cotes on smooth integrands, then let Pedro alone extend the same toolkit to Chebyshev collocation for a boundary-value / ODE problem.

**Suggested-topic alignment:** Instructor topic **2 (Orthogonal polynomials)** plus the course’s Gaussian quadrature thread. Spectral collocation is the optional research wing — not required for the whole group.

**Fit score (group):** ★★★★☆ — every respondent rated orthogonal polynomials ≥ 6 (best *floor* among theory-heavy suggested topics). Avoids Kai’s hard zeros on minimax / L2-poly-*as-project* by staying in the orthogonal-poly / quadrature lane.

---

## Why this fits the group

| Person | Fit | Why |
|---|---|---|
| **Kai** | Excellent | Orthogonal polynomials **8**; loves rigorous-but-masterable math; geometry / scientific computing interests fit Chebyshev approximation visuals. Explicitly *not* a minimax-equioscillation project (his 0) or smoothing-splines project (his 1). |
| **Pedro** | Excellent | Approximation theory interest; BVPs 8; can solo the spectral / collocation OOS module (differentiation matrices, solving \(u''=f\) or a nonlinear BVP with Newton). Satisfies “research flavor” without a theory-only project (application + experiments remain). |
| **Mario** | Good | Orth. polys 6, approx theory selected in themes, scientific computing 8. Owns implementation benchmarks vs trapezoid/Simpson and an applied integral (physics/engineering). Short-notes ceiling OK: recurrence + Golub–Welsch recipe. |
| **Bhuvi** | Good | Orth. polys 6; finance lean (7) → optional applied integral from option pricing / expected payoff if wanted, or stick to physics. Oral role: “why special nodes beat equal spacing” with pictures. |
| **Member 5** | Excellent | Closest to class: Gaussian quadrature already on the roadmap; implement Legendre nodes/weights, change of interval, compare to Simpson. Pure syllabus + lab-style notes. |

**Avoided landmines:** Not framed as minimax (Kai 0), not smoothing splines (Kai 1), not education-demo product, not biology, not floating-point archaeology. Theory is present but always paired with code and plots (Mario / Pedro constraints).

---

## Project narrative (30 seconds)

> “Orthogonal polynomials are the hidden engine of Gaussian quadrature: choose nodes as zeros of \(P_n\), and you integrate degree \(2n-1\) polynomials exactly. We derive three-term recurrences, compute nodes/weights, and beat trapezoidal/Simpson on smooth problems. Then we show the same Chebyshev family yields spectral collocation — turning a BVP into a linear algebra problem with exponential accuracy for analytic solutions.”

Two acts, one theme: **polynomials chosen by orthogonality unlock accuracy**.

---

## Mathematical core

### Act I — Shared (suggested topic + class)

**Orthogonality** on \([a,b]\) with weight \(w>0\):
\[
\langle p,q\rangle_w = \int_a^b p(x)q(x)w(x)\,dx = 0 \quad (p\neq q\text{ in the family}).
\]

Families to cover (pick Legendre as mandatory; Chebyshev as bridge to Act II):

| Family | Interval | Weight | Role |
|---|---|---|---|
| Legendre \(P_n\) | \([-1,1]\) | \(1\) | Gauss–Legendre quadrature |
| Chebyshev \(T_n\) | \([-1,1]\) | \((1-x^2)^{-1/2}\) | Oscillation control, spectral methods |
| (Optional) Hermite | \(\mathbb{R}\) | \(e^{-x^2}\) | Nice if someone wants Gaussian-weight integrals |

**Three-term recurrence** (implement, don’t only cite):
\[
p_{n+1}(x)=(x-\alpha_n)p_n(x)-\beta_n p_{n-1}(x).
\]

**Gaussian quadrature:** nodes = zeros of \(p_n\); weights from Christoffel numbers / first eigenvector entry (Golub–Welsch Jacobi matrix eigenproblem — short tutorial, implementable in ~30 lines with NumPy).

**Experiments (shared):**
- Exactness check on polynomials up to degree \(2n-1\).  
- Smooth non-polynomial \(f\) (e.g. \(e^{-x^2}\cos x\)): error vs \(n\) for Gauss vs composite Simpson with comparable evaluations.  
- Change of interval \([a,b]\to[-1,1]\).

### Act II — Pedro only (OOS)

**Chebyshev differentiation matrix** on Gauss–Lobatto nodes \(x_j=\cos(\pi j/N)\):
approximate \(u'(x_i)\approx \sum_j D_{ij}u(x_j)\).

Solve a model BVP, e.g.
\[
u''=f(x),\quad u(-1)=u(1)=0
\]
or a nonlinear problem via Newton on the collocation residual (reuses class Newton).

**Manufactured solution:** pick \(u_{\mathrm{exact}}\), set \(f=u_{\mathrm{exact}}''\), measure \(\|u_N-u_{\mathrm{exact}}\|_\infty\) vs \(N\) — expect spectral (roughly exponential) decay for analytic \(u\).

Optional stretch: time-dependent heat equation with Chebyshev in space + RK/BDF in time — only if Act II finishes early.

**Why Pedro alone:** spectral methods are after Quiz-2 / outside typical BAM Y2 Numerical Methods depth; the group’s oral can treat Act II as “extension preview” with Pedro fielding deep questions.

---

## Applied wrappers (choose one primary)

1. **Engineering integral** without closed form (Mario/Kai): e.g. arc length, moments of inertia, radiative view-factor style integrals — method-first with a real integrand.  
2. **Finance-flavored** (Bhuvi interest): expected payoff integrals under a simple density (not a full Black–Scholes course). Keep light.  
3. **Geometry** (Kai/Pedro): Chebyshev approximation of a curve / ellipse perimeter comparisons.  

Avoid ML-kernel rabbit holes and biology.

---

## Work packages (5 people)

| Package | Owner | In / out | Deliverable |
|---|---|---|---|
| WP1 — Legendre recurrence + roots/weights | Member 5 + Kai | Suggested + class Gauss | `OrthogonalFamily` + Gauss rule |
| WP2 — Benchmarks vs Newton–Cotes | Mario + Bhuvi | In-syllabus comparison | Error/cost plots, recommendation table |
| WP3 — Chebyshev family + visuals | Kai | Short notes | \(T_n\) plots, weight intuition, link slide to Act II |
| WP4 — Spectral collocation BVP | **Pedro alone** | **OOS** | Diff matrix, BVP solve, spectral convergence plot |
| WP5 — Application integrand + oral | Bhuvi + Mario | Applied | One real integral story; Q&A cards |

Scope for 5: theory + two families + systematic quadrature contest + one spectral extension is substantial and coherent (not five disconnected mini-projects).

---

## Experiments / figures for the talk

1. Overlay \(P_n\) / \(T_n\) and mark Gauss nodes.  
2. Semi-log error vs nodes: Gauss vs Simpson.  
3. Conditioning / stability note: evaluate polynomials via recurrence (not naïve monomials) — practical insight without an “errors chapter” reboot.  
4. Pedro: \(\log\|e\|_\infty\) vs \(N\) for collocation (the “wow” slide).  
5. Failure case: integrand with singularity or low regularity — Gauss loses magic; shows maturity.

---

## Oral defense map

| Question | Who |
|---|---|
| Why are orthogonal polynomials useful for integration? | Kai / Member 5 |
| How do you get nodes and weights in code? | Member 5 |
| Why not always use high-order Gauss? | Mario |
| What is a Chebyshev differentiation matrix? | **Pedro** |
| Show spectral convergence — why so fast? | **Pedro** |
| Walk us through your applied integral. | Bhuvi / Mario |

---

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Looks too theoretical for Mario | Lead with plots and the applied integral; put proofs in appendix |
| Confused with “minimax project” by instructor/peers | Title and abstract say *orthogonal polynomials & quadrature*; never promise Remez |
| Spectral Act II fails | Project still complete with Act I alone — Pedro’s part is upside, not a single point of failure |
| Golub–Welsch intimidating | Use SciPy roots only for validation; implement Jacobi eigenroute from a 2-page lab note |

---

## Recommended stack & references

- NumPy `linalg.eigh` for Jacobi matrix; Matplotlib  
- Suli & Mayers (course-adjacent) for approximation culture — **do not** make Ch. 8 minimax the spine  
- BYU ACME Gaussian Quadrature lab pattern  
- Trefethen *Approximation Theory and Approximation Practice* (Pedro, selective) for Chebyshev spectral intuition  

---

## Verdict

Best pick if the group wants a **mathematically elegant, highly defendable** project with **uniform method interest (≥6)** and a clean Pedro-only research cliff (spectral methods). Slightly less “robot wow” than Proposals 1–2, but extremely coherent for oral Q&A.
