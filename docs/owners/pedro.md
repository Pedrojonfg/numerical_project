# Pedro — your part of the project

## In plain words

The usual “check every combination on a big grid” becomes impossible when there are many directions.  
Your special job is the **clever thinner grid**: still careful and mathematical, but with far fewer points. You learn it, code it, and explain it on presentation day — the others are *not* expected to master that theory.

You also hold the **glue**: the skeleton of the written report, the notebook that puts everyone’s numbers side by side, and any extra ideas the group keeps if they would overload someone else.

If work piles up unevenly, **you take the extra**, not Kai / Mario / Bhuvi / Anita.

---

## What “done” looks like for you

- [ ] Sparse / Smolyak-style rule runs on the **same shared test problems** as everyone else.
- [ ] Fair comparison pictures: your method vs their CSV numbers (nodes vs accuracy).
- [ ] You can defend in Q&A: what it combines, when it wins, when random sampling still wins.
- [ ] Report skeleton in `report/` with headings; others fill their sections.
- [ ] Cross-method comparison notebook (`notebooks/compare_*.ipynb`).
- [ ] Contracts stay stable (`docs/contracts.md`); you are the decider if something must change.
- [ ] Optional extras (`~`) only if the group keeps them — and then **you** implement them.

---

## What you need before you can start / finish

| Need | From | Status / how to unblock |
|---|---|---|
| Shared test problems | Anita (scaffolded) | Start coding against them **now** |
| Locked contracts | You + group | Already locked — [../contracts.md](../contracts.md) |
| Kai’s / Mario’s CSV files | Kai, Mario | Needed for the **comparison** notebook, **not** to invent your method. Build your method first; comparison fills in as PRs land |
| Robot problem | Mario | Optional re-run later; do not wait |

**You can start today** on Smolyak against test problems.

---

## What you unlock for others

| When you finish… | Who benefits | How |
|---|---|---|
| Working sparse method + CSV | Bhuvi demo, Anita tables, oral “third competitor” | Drop `results/smolyak_*.csv` |
| Report skeleton | Everyone | They know where to paste their section |
| Comparison notebook | Mario slides, Bhuvi demo | One place that tells the tournament story |
| Clear cut decisions if we must shrink | Whole group | You break ties; reopen cut list with the group if a must-have is at risk |

---

## Files you own (write here; others only read)

- `src/quad_project/rules/smolyak.py`
- `docs/contracts.md` (changes only with a real reason + notice)
- `notebooks/compare_*`
- `report/` skeleton
- Optional `~` experiments you absorb

**Branch:** `scope/smolyak` (and separate PRs for report/compare if cleaner).

---

## Suggested order of work

1. Spike: get *one* sparse level working in 2D on `constant_one` / `smooth_product`.
2. Generalize; write CSVs on the shared tests.
3. Open comparison notebook that reads whatever CSVs exist (partial OK).
4. Draft report headings; ping others to fill sections.
5. Prep your oral deep-dive card (only you own Smolyak Q&A).

---

## Oral — you answer deeply

- What is the sparse construction actually combining?
- When would you *not* use it (and prefer plain grids or random sampling)?

---

## Links

- Contracts: [../contracts.md](../contracts.md)  
- Plan: [../../plan.md](../../plan.md)  
- Your overflow rule is in the plan header (you absorb extras).
