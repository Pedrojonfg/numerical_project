# Anita — your part of the project

## In plain words

You build the **shared playground** so the others do not invent five incompatible setups.

That means:

- The common **practice problems** everyone measures on (smooth easy ones, plus a “always 1” check).
- The agreed way to **save numbers** into tables (CSV) and helpers to **draw pictures from those tables**.
- Keeping the project **installable** (dependencies file) and the “how do I run this?” instructions honest.

You stay on material close to the course. You do **not** have to learn the sparse fancy method.  
If someone wants an *extra* practice problem, **they add it themselves** — they must not dump that on you.

A good chunk of the playground is already started in the repo; your job is to own it, harden it, and extend the plotting/tables side.

---

## What “done” looks like for you

- [ ] Test problems stay correct and documented (`constant_one`, `smooth_product`, `genz_peak`).
- [ ] CSV helpers stay aligned with the locked columns; README “how to run” stays true.
- [ ] Plot helpers that read `results/` (usable with fake or real data).
- [ ] Report **tables** assembled from everyone’s CSV files (near the end).
- [ ] `requirements.txt` / dependency changes only through **you** (others ask via PR).
- [ ] Ready for oral: what the practice problems are; what the table columns mean; 1D classroom exactness angle with Kai if asked.

---

## What you need before you can start / finish

| Need | From | Status / how to unblock |
|---|---|---|
| Locked contracts | Pedro / group | Already done — follow [../contracts.md](../contracts.md) |
| Real experiment files | Kai, Mario, Pedro | Needed for final tables only; until then use `example_fake.csv` |
| Robot details | Mario | Not needed for your core toolkit |

**You can work immediately** on docs, plot polish, and small integrand/docs fixes via PR.

---

## What you unlock for others

| When you finish… | Who benefits | How |
|---|---|---|
| Stable test problems | Kai, Mario, Pedro | They all measure the same things → fair contest |
| CSV + plot tools | Bhuvi demo, Pedro comparison, your tables | Nobody invents a private file format |
| Dependency file | Whole group | One place to install |

Without your playground, people block each other. With it, they work in parallel.

---

## Files you own (write here; others only read / PR)

- `src/quad_project/integrands/`
- `src/quad_project/plotting/`
- `src/quad_project/results_io.py` (shared with contract — coordinate with Pedro if columns would change)
- `requirements.txt` (and related install metadata if you touch it)
- README run instructions (keep accurate)
- Report tables built from `results/`

**Branch:** `scope/scaffold` (or small focused PRs) → **PR into `main`**.

**Expansion rule (L4):** new practice problem → the person who wants it opens the PR and does the work.

---

## Suggested order of work

1. Read contracts; run `pytest`; skim existing integrands.
2. Improve docstrings / README bits that confuse newcomers.
3. Strengthen plotting helpers Bhuvi needs for the demo.
4. As CSVs arrive, build the report tables.
5. Prep a short oral card with Bhuvi on “what are our test problems?”

---

## Oral — you answer

- Where do the shared practice problems and CSV tables come from?
- (With Kai) Classroom meaning of exactness for the 1D rule.

---

## Links

- Contracts: [../contracts.md](../contracts.md)  
- Plan: [../../plan.md](../../plan.md)  
- Setup: [../../README.md](../../README.md)
