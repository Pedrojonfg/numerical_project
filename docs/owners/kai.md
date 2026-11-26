# Kai — your part of the project

## In plain words

Imagine you have a recipe that works great when you cook **one** ingredient.  
Your job is to show what happens when you try the same recipe in **many** directions at once (2, 3, 4, 5…): the shopping list of “points to check” explodes, and the computer gets slower or less accurate unless you are clever.

You build that “many directions at once” version of the classroom method, draw clear pictures of the explosion, and save your numbers in the shared results folder so the others can compare without rewriting your work.

You are **not** in charge of the random-sampling method (that is Mario) or the fancy sparse method (that is Pedro).

---

## What “done” looks like for you

- [ ] The 1D classroom rule works on the shared box \([-1,1]\) (starter helper already exists).
- [ ] The product / grid version works for dimensions 2 through 5 on the **shared test problems**.
- [ ] Plots that show: more dimensions → many more points; error vs effort.
- [ ] CSV rows in `results/` for your method (`method=tensor`, …).
- [ ] A short write-up of *your* section for the report + readiness for oral questions about “why so many points?”
- [ ] (Optional consult) Glance at Pedro’s theory wording if he asks — not a merge gate.

---

## What you need before you can start / finish

| Need | From | Status / how to unblock |
|---|---|---|
| Shared test problems + how to call them | Anita (already scaffolded) | Use `quad_project.integrands` now |
| Agreed box \([-1,1]^d\) and CSV columns | Whole group (locked) | Read [../contracts.md](../contracts.md) |
| Robot arm problem | Mario | **Not required** for your main plots — use test problems first; re-run later if you want |
| Pedro’s or Mario’s methods | — | **Not required** — you ship your own CSVs |

**You can start today** on test problems. Nothing from Mario/Pedro blocks you.

---

## What you unlock for others

| When you finish… | Who benefits | How |
|---|---|---|
| Tensor results CSV | Pedro, Bhuvi, Anita, Pedro’s comparison notebook | They read your file; they do not need your notebook open |
| Clear “curse” figures | Mario (slide story), Bhuvi (demo) | Drop figures / paths they can point to |
| Solid oral answers on product grids | Whole group | Bhuvi will make a *short* backup card; you own the deep answer |

---

## Files you own (write here; others only read)

- `src/quad_project/rules/gauss1d.py` (starter exists — improve as you like)
- `src/quad_project/rules/tensor.py` (**your main implementation**)
- Your notebooks under `notebooks/` (e.g. `notebooks/kai_tensor_curse.ipynb`)
- Your figure outputs / CSVs you generate under `results/` (e.g. `results/tensor_*.csv`)

**Do not edit:** Mario’s `monte_carlo.py` / `robot/`, Pedro’s `smolyak.py`, Anita’s integrand registry (unless you add a *new* test problem yourself via PR).

**Branch:** `scope/tensor` → PR into `main`.

---

## Suggested order of work

1. Run `pytest` and try `get_integrand("smooth_product")` on random points in \([-1,1]^d\).
2. Finish product rule in `tensor.py`.
3. Sweep dimensions and node counts → write CSV.
4. Make the two key plots (error vs nodes; cost vs dimension).
5. Write your report paragraph + tell Bhuvi the 2–3 questions you want on your Q&A card.

---

## Oral — you answer deeply

- Why does the product rule need on the order of \(n^d\) points?
- What does “exact for polynomials up to degree …” mean in 1D (with Anita for the syllabus angle)?

---

## Links

- Contracts: [../contracts.md](../contracts.md)  
- Plan: [../../plan.md](../../plan.md)  
- Setup: [../../README.md](../../README.md)
