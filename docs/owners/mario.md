# Mario — your part of the project

## In plain words

You own two connected pieces:

1. **The random method** — instead of a careful fixed grid, you throw many random darts and average. It is the “control” in our story: honest and useful in high dimension, but **not** the hero of the talk (Kai’s grid story leads; your method is the baseline).
2. **The robot toy problem** — a simple two-joint arm. For each pair of joint settings you give a **smooth score** of “how close is the hand to the target?” Everyone else will treat that score like just another test function; they should not need to understand the robot insides.

You also shape the **overall slide story** (beginning → curse → contest → robot → recommendation).

---

## What “done” looks like for you

- [ ] Plain random method on the shared test problems (several random seeds so the band of luck is visible).
- [ ] Curves that show behaviour when dimension grows.
- [ ] CSV rows with `method=monte_carlo` and a `seed` column filled in.
- [ ] Two-joint arm + soft score function others can call (`robot_2r_soft`).
- [ ] Slide arc (even if figures arrive later).
- [ ] Your report section (random method + robot motivation).
- [ ] Ready for oral: why the random rate does not “explode with dimension” the same way grids do; why we chose this robot score.

**Not your job unless you volunteer and implement it yourself:** fancy variance tricks, animations, 3-joint arm (those are extras; if the group keeps them, Pedro may absorb them).

---

## What you need before you can start / finish

| Need | From | Status / how to unblock |
|---|---|---|
| Shared test problems + CSV format | Anita / contracts | Start the random method **now** on test problems |
| Domain \([-1,1]^d\) | Locked | Sample with \(X = 2U - 1\), scale by volume \(2^d\) — see contracts |
| Kai’s / Pedro’s code | — | **Not required** for your method |
| Soft score design choices (link lengths, target, width) | You | Autonomous — pick sensible defaults and document them |

**Robot and random method can advance in parallel.** Method owners will not wait on the robot for their main work.

---

## What you unlock for others

| When you finish… | Who benefits | How |
|---|---|---|
| Monte Carlo CSVs | Pedro comparison, Bhuvi demo, Anita tables | Files in `results/` |
| Published robot score function | Kai, Pedro (optional re-run), Bhuvi (live figure) | They only **call** your function |
| Slide story spine | Bhuvi (cards), whole oral | Everyone knows the narrative order |

---

## Files you own (write here; others only read)

- `src/quad_project/rules/monte_carlo.py`
- `src/quad_project/robot/` (including soft reach)
- Your notebooks / figures
- Main slide deck story under `slides/` (coordinate with Bhuvi’s Q&A folder)

**Branch:** `scope/mc` and/or `scope/robot` → PRs into `main`.

---

## Suggested order of work

1. Implement plain MC on `constant_one` (check you recover about \(2^d\)).
2. Run shared tests + multi-seed CSVs + high-dimension curves.
3. Implement 2R soft score (map box → joint angles → hand position → smooth score).
4. Run MC (and later ask others to re-run their methods) on `robot_2r_soft`.
5. Draft slide order; send Bhuvi the questions you want on your cards.

---

## Oral — you answer deeply

- Why people say the random method’s rate is “kind to dimension.”
- Why this robot score (smooth closeness), not a harsh yes/no map of the workspace.

---

## Links

- Contracts: [../contracts.md](../contracts.md) especially C1 (MC sampling) and C3 (robot)  
- Plan: [../../plan.md](../../plan.md)
