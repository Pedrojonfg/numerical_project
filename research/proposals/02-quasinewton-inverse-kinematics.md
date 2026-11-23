# Proposal 2: Quasi-Newton Methods for Robot Inverse Kinematics

**One-line pitch:** Implement gradient descent, Newton, and BFGS (with line search) on classic benchmarks, then use them to solve planar robot inverse kinematics — a concrete robotics problem that showcases why quasi-Newton exists.

**Suggested-topic alignment:** Instructor topics **1 (Quasi-Newton variants)** and **3 (Unconstrained optimization)** almost verbatim. Rootfinding / Newton from lectures are the springboard.

**Fit score (group):** ★★★★☆ — top application consensus (robotics min 6; ML numerics high); method ratings mixed but salvageable with role design.

---

## Why this fits the group

| Person | Fit | Why |
|---|---|---|
| **Pedro** | Excellent | Rated unconstrained optimization **10/10**, quasi-Newton 7. Perfect OOS owner: BFGS update derivation, Wolfe line search, limited-memory L-BFGS, or singularity / non-isolated minima in IK. Research flavor without forcing the whole group into Nocedal & Wright. |
| **Kai** | Strong | Unconstrained opt 8; robotics 6; ML numerics 8; geometry 9. Happy to own Rosenbrock theory, convergence intuition, and “why Hessian approximations”. Avoids his vetoed topics entirely. |
| **Mario** | Strong | Robotics **8**, ML 8, scientific computing 8. Ideal for FK/IK modelling, demos, and “real impact” slides. Optimization rating 6 is enough for implementation + experiments (not proofs). Ceiling = short notes — BFGS recipe-level is fine for him. |
| **Bhuvi** | Acceptable → good with role design | Unconstrained opt only **3**, but quasi-Newton **6** and “idc” overall. Give Bhuvi: (1) clear geometric IK story, (2) GD vs Newton vs BFGS *demo ownership*, (3) Q&A cards on “what each method needs (gradient / Hessian / history)”. No derivation load. |
| **Member 5** | Good | Syllabus-tied: Newton’s method for systems / minimization as taught; implement GD and exact-Newton on Rosenbrock following a tutorial; help with plots. Never touches L-BFGS. |

**Avoided landmines:** Not biology, not didactic-demo product, not floating-point deep dive, not pure theory (Pedro’s orientation veto). Application is robotics — shared high ground.

**Honest caveat:** Bhuvi’s low unconstrained-opt score is the main weakness vs Proposal 1. Mitigate by making the *story* “Newton’s method variants for robots” (connects to class rootfinding) rather than “optimization theory seminar”.

---

## Project narrative (30 seconds)

> “Newton’s method is fast when you can form a Hessian, and hopeless when you can’t. We compare gradient descent, Newton, and BFGS with line search on Rosenbrock, then deploy the same solvers on planar inverse kinematics: find joint angles so the end-effector hits a target. BFGS gives Newton-like speed without second derivatives — exactly why robots and ML use it.”

Memorable, applied, and on the suggested list (originality via IK case + careful experiments).

---

## Mathematical core

### Shared / in-syllabus or short notes

**Unconstrained problem:** \(\min_{x\in\mathbb{R}^n} f(x)\).

| Method | Search direction | Needs |
|---|---|---|
| Gradient descent | \(p_k = -\nabla f(x_k)\) | gradient |
| Newton | \(p_k = -[\nabla^2 f(x_k)]^{-1}\nabla f(x_k)\) | Hessian + linear solve |
| BFGS (quasi-Newton) | \(p_k = -H_k\nabla f(x_k)\) with rank-2 update of inverse Hessian approx. | gradients only + history |

**Line search (group-light version):** backtracking Armijo
\[
f(x_k+\alpha p_k) \le f(x_k) + c\,\alpha\,\nabla f(x_k)^\top p_k,
\]
with \(\alpha\leftarrow \gamma\alpha\) (as in standard course assignments). Enough for Mario/Bhuvi/Member 5.

**Benchmark:** Rosenbrock
\[
f(x,y)=(1-x)^2+100(y-x^2)^2
\]
— banana valley, classic for comparing methods (explicitly mentioned in the project brief).

### Applied model — planar \(n\)R arm IK

Forward kinematics (2D):
\[
p(\theta)=\sum_{i=1}^{n} \ell_i\begin{pmatrix}\cos(\sum_{j=1}^i\theta_j)\\\sin(\sum_{j=1}^i\theta_j)\end{pmatrix}.
\]

Least-squares objective (smooth, unconstrained first):
\[
f(\theta)=\tfrac12\|p(\theta)-p_{\mathrm{target}}\|^2.
\]

Gradient via Jacobian of FK (analytic or finite differences for a robustness experiment — *one* finite-difference check is fine; don’t make the project about numerical differentiation theory).

Optional soft joint limits via penalty (still unconstrained):
\[
f_{\mathrm{pen}}(\theta)=f(\theta)+\frac{\mu}{2}\sum_i\big(\max(0,\theta_i-\theta_i^{\max})^2+\max(0,\theta_i^{\min}-\theta_i)^2\big).
\]

### Pedro-only OOS block

Pick **one** deep slice (not all):

1. **BFGS theory:** secant condition \(H_{k+1}y_k=s_k\), curvature condition \(y_k^\top s_k>0\), proof sketch of hereditary positive-definiteness, expected superlinear convergence.  
2. **L-BFGS** for higher-DOF arms (\(n=10+\)) — memory-\(m\) two-loop recursion.  
3. **IK pathologies:** non-isolated minima (redundant arms), singularities, comparison to Jacobian-transpose / damped least-squares IK from robotics literature.  
4. **Strong Wolfe line search** vs pure Armijo — when it matters on Rosenbrock vs IK.

This is the “research flavor” the rest of the group does not need to study.

---

## Work packages (5 people)

| Package | Owner | In / out | Deliverable |
|---|---|---|---|
| WP1 — Rosenbrock + GD + Newton | Member 5 + Kai | Syllabus Newton + short notes | Working solvers, contour path plots |
| WP2 — Backtracking line search + experiments | Kai + Bhuvi | Short notes | Iteration counts, \(f\)-decrease plots, failure cases (bad \(\alpha\)) |
| WP3 — BFGS (+ optional L-BFGS) | **Pedro alone** | Suggested + **OOS depth** | BFGS code, theory appendix/slides |
| WP4 — Planar IK application | Mario + Bhuvi | Applied trigonometry | Arm demo, multi-target tests, method comparison table |
| WP5 — Oral + report | All | — | Storyboard: class Newton → quasi-Newton → robot |

Substantial for 5: three algorithms × two problem classes (analytic benchmark + robotics) × ablation on line search / init guesses.

---

## Experiments that score “insight”

1. Contour plots: GD zig-zag vs Newton vs BFGS on Rosenbrock.  
2. Table: iterations, gradient evaluations, wall time to \(\|\nabla f\|<\varepsilon\).  
3. IK: success rate over random targets inside/outside workspace.  
4. Init sensitivity: same target, 20 random \(\theta_0\).  
5. Cost of Hessian: show Newton’s per-iteration cost blowing up as \(n\) grows (motivates BFGS) — *computational* cost, not rounding-error theory.  
6. One “BFGS without line search” failure — teaches why step-size control is in the brief.

---

## Oral defense map

| Likely question | Who |
|---|---|
| How does Newton for minimization relate to Newton for \(F(x)=0\)? | Member 5 / Kai |
| What does BFGS store / update? | **Pedro** |
| Why not always use Newton? | Kai / Pedro |
| How is the IK loss defined? Gradient? | Mario / Bhuvi |
| What if the target is unreachable? | Mario |
| Show me the arm missing then converging. | Bhuvi (demo) |

---

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Bhuvi disengages from “optimization” label | Brand as *Newton variants + robots*; Bhuvi owns live demo & Q&A cards |
| BFGS bugs eat Pedro’s week | Start from a known pseudocode (e.g. TAMU CSCE450-style); validate on Rosenbrock before IK |
| Looks like a generic homework | Emphasize IK experiments, workspace edge cases, and a clear recommendation (“use BFGS when…”) |
| Another group picks quasi-Newton | Differentiate with robotics IK + L-BFGS stretch; claim early |

---

## Recommended stack & references

- Python + NumPy; Matplotlib animations of the arm  
- Nocedal & Wright *Numerical Optimization* (Pedro only, selected sections)  
- Course Newton / systems slides for the rest  
- Inspiration: TAMU IK+BFGS assignment; NTNU student IK+BFGS report  

---

## Verdict

Best pick if the group wants a **clear applied robotics demo**, likes **optimization / ML-adjacent** framing, and is comfortable letting Pedro carry BFGS theory. Slightly riskier socially than Proposal 1 only because of Bhuvi’s low unconstrained-opt rating — fixable with branding and role design.
