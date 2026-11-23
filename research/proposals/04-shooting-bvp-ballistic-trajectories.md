# Proposal 4: Shooting Methods for Boundary-Value Trajectories (Ballistics / Soft Landing)

**One-line pitch:** Turn trajectory problems with conditions at two ends into IVPs plus rootfinding — reuse Runge–Kutta and Newton/secant from class — then aim a projectile (with drag) or soft-land a 1D thruster; Pedro alone adds multiple shooting or a light optimal-control TPBVP.

**Suggested-topic alignment:** Instructor explicitly says **boundary value problems will not be covered in class** but appear in the syllabus — hence ideal project material. Builds directly on IVPs (Euler / RK) and rootfinding already taught.

**Fit score (group):** ★★★★☆ — robotics/control is the strongest shared application band (min 6); IVP interest high for Kai/Pedro/Mario. Bhuvi’s low BVP score (3) is mitigated because *their* work is IVP integration + rootfinding + demo, not BVP theory.

---

## Why this fits the group

| Person | Fit | Why |
|---|---|---|
| **Pedro** | Excellent | BVP 8, IVP 8, robotics 9, research ceiling. Solo OOS: multiple shooting, or indirect optimal control (Pontryagin → TPBVP) for fuel-optimal soft landing — memorable and impactful. |
| **Kai** | Strong | IVP deep-dive 7, BVP 6, physics/engineering 8, robotics 6. Natural owner of RK order experiments and the shooting residual \(m(s)=y(b;s)-\beta\). Rigorous + explainable. |
| **Mario** | Strong | IVP/BVP 7, robotics 8, physics 7, wants real impact + great slides. Owns the cannon / landing narrative, parameter studies (drag, mass), and presentation polish. Short notes suffice for single shooting. |
| **Bhuvi** | Acceptable with role design | BVP rating **3**, IVP **3** — weakest method alignment. Compensate: Bhuvi never “studies BVP theory”; they implement/run RK4 they already saw, drive the live aiming demo, and answer “how do we adjust the guess?” with secant intuition (class rootfinding). Survey “idc” + Q&A priority 9 supports this. |
| **Member 5** | Good | Syllabus-only: RK2/RK4 integrator from lecture patterns; bisection/secant on the miss function; linear BVP where two shots suffice. No multiple shooting. |

**Avoided landmines:** Not biology, not education-demo kit, not error-chapter redux (focus on *miss residual* and *stability of shooting*, which is BVP content — frame as dynamics sensitivity, not FP). Not pure theory: every week ends in a trajectory plot.

---

## Project narrative (30 seconds)

> “Initial-value solvers march forward; many real trajectory problems specify conditions at *both* ends. The shooting method guesses the missing initial data, integrates with Runge–Kutta, and uses rootfinding to zero the miss at the far boundary. We hit a ballistic target with drag, study when single shooting becomes fragile, and (optional) show how multiple shooting stabilizes harder problems.”

Classroom vocabulary (RK + Newton) → new idea (BVP) → cool demo. Excellent oral arc.

---

## Mathematical core

### Shared — single shooting (short notes on top of class IVPs)

Second-order BVP:
\[
y''=f(x,y,y'),\qquad y(a)=\alpha,\quad y(b)=\beta.
\]

Guess \(s\approx y'(a)\), solve the IVP, define the **miss**
\[
m(s)=y(b;s)-\beta.
\]
Solve \(m(s)=0\) with bisection / secant / Newton (class tools). Each residual evaluation = one IVP integrate.

**Linear case insight (Member 5 talking point):** for linear ODEs, \(m(s)\) is affine → two shots determine the exact \(s\) (up to discretization error).

### Applied problem A — Cannon / baseball with drag (group default)

State \((x,y,v,\theta)\); drag \(\propto v^2\). Fix launch speed; unknown launch angle \(\theta_0\); require impact at a target range (and \(y=0\)).

Classic undergraduate demo (BYU ACME / computational physics courses). Two physical solutions often exist (low / high trajectory) — great for Q&A and for showing bracket selection.

### Applied problem B — 1D soft landing (alternative / stretch)

Vertical lander: \(h''=-g+u(t)/m\) with \(h(0)=h_0\), \(h'(0)=v_0\), and terminal conditions \(h(T)=0\), \(h'(T)=0\). Unknowns may include thrust profile parameters or final time. Still a small nonlinear system for shooting.

Robotics/control flavor without Mario’s biology veto.

### Pedro-only OOS block (pick one)

1. **Multiple shooting:** split \([a,b]\) into segments; unknown interface states; continuity defects as extras in the rootfinding system — more variables, better conditioning (Kelly trajectory notes).  
2. **Finite-difference BVP** as a competing method (matrix system) — comparison, still numerical methods.  
3. **Indirect optimal control:** fuel-optimal landing → adjoint equations → larger TPBVP solved by shooting (research flavor; cite Bryson-style notes). Keep the group’s oral at “single shooting works; here’s why we needed multiple shooting for the hard case.”

---

## Work packages (5 people)

| Package | Owner | In / out | Deliverable |
|---|---|---|---|
| WP1 — RK integrators + convergence checks | Member 5 + Kai | Syllabus IVP | Validated RK4 vs known ODE |
| WP2 — Shooting residual + rootfinders | Kai + Member 5 | Short notes BVP | `shoot(f, bc, s0)` API |
| WP3 — Cannon-with-drag application | Mario + Bhuvi | Applied physics | Demo, low/high trajectories, drag sweeps |
| WP4 — Multiple shooting or optimal-landing TPBVP | **Pedro alone** | **OOS** | Hard-case solve + comparison to single shooting |
| WP5 — Oral storyboard | All (Bhuvi demo lead) | — | Live “aim → miss → correct” animation |

Substantial for 5: method (shooting) + IVP accuracy study + nonlinear application + Pedro’s robustness/optimal-control extension.

---

## Experiments that play well orally

1. Animation: guess angle → trajectory → miss → updated angle → hit.  
2. \(m(s)\) plotted vs \(s\) (shows two roots).  
3. RK step-size vs hit accuracy (cost-vs-accuracy — not FP theory).  
4. High-drag / stiffish regime: single shooting struggles → motivates Pedro’s multiple shooting.  
5. Table: iterations of secant vs Newton on \(m(s)\); IVP calls as the true cost metric.

---

## Oral defense map

| Question | Who |
|---|---|
| How is a BVP different from an IVP? | Kai / Member 5 |
| What is the miss function? Which rootfinder? | Member 5 |
| Why RK4 inside the loop? Local truncation? | Kai |
| Show the demo and explain the two angles. | **Bhuvi / Mario** |
| When does single shooting break? | **Pedro** (+ Kai) |
| What did you add beyond the basic method? | **Pedro** |

---

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Bhuvi’s low BVP interest | Zero BVP textbook load for Bhuvi; demo + rootfinding ownership |
| “Just a physics toy” perception | Keep numerical questions central: residual, IVP cost, stability of shooting |
| Pedro’s optimal-control rabbit hole | Timebox: multiple shooting first; PMP only if WP4 ahead of schedule |
| Another group claims BVPs | Specialize title: *shooting for ballistic / soft-landing trajectories with drag*; claim early |

---

## Recommended stack & references

- NumPy/SciPy; Matplotlib animation  
- Course RK + rootfinding slides  
- Python Numerical Methods — shooting chapter; BYU ACME shooting / cannon lab  
- Matt Kelly “Transcription Methods for Trajectory Optimization” (Pedro, multiple shooting intuition)  

---

## Verdict

Best pick if the group wants a **live aiming demo**, maximum reuse of **class IVP + rootfinding**, and an official “not taught but in syllabus” topic. Use careful role design for Bhuvi. Pedro’s multiple-shooting / soft-landing control extension supplies the research punch without blocking the group deliverable.
