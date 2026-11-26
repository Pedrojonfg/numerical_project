# Bhuvi — your part of the project

## In plain words

You make sure that on presentation day **nobody freezes**.

You build a **small live demo** that shows the pictures and numbers the group already saved (you should not have to re-code Kai’s or Pedro’s maths).  
You prepare **short answer cards** so each person knows what they own — and so everyone has a one-sentence backup for the others’ topics.  
You also prepare a **simple backup geometry picture** (like a doughnut / overlapping balls volume) in case we want a second visual that is not the robot.

Keep the theory light: your strength is clarity and calm Q&A, not inventing new methods.

---

## What “done” looks like for you

- [ ] Demo notebook/script that **loads CSV files** from `results/` (works already with `results/example_fake.csv`).
- [ ] Full Q&A card pack in `slides/qa_cards/` (one card per likely question).
- [ ] Cross-brief: every member can say a *surface* sentence about parts they do not own.
- [ ] One backup geometry figure/notebook.
- [ ] Comfort running the demo live (or screen-sharing the plots).

---

## What you need before you can start / finish

| Need | From | Status / how to unblock |
|---|---|---|
| CSV column meanings + fake example | Anita / repo | **Start now** with `example_fake.csv` and plotting helpers |
| Real method CSVs | Kai, Mario, Pedro | Demo improves as they merge; **do not block** — show whatever files exist |
| Robot figure | Mario | Nice for the finale; until then show test-problem plots |
| Deep theory | — | You only need surface cards; owners handle depth |

**You are almost never blocked.** Missing CSVs ⇒ plot a subset or keep using the fake file and label it “sample.”

---

## What you unlock for others

| When you finish… | Who benefits | How |
|---|---|---|
| Q&A cards | Whole group (70% of grade is oral) | People know who speaks and what the short backup is |
| Stable demo path | Presenter nerves | One command / notebook to open |
| Cross-brief | Anyone interrupted by the professor | Nobody is stranded on a teammate’s topic |

---

## Files you own (write here; others only read)

- `notebooks/demo_*` (replace the placeholder markdown with a real notebook when ready)
- `slides/qa_cards/`
- Backup geometry notebook under `notebooks/`

**Do not rewrite** method code in `rules/` — import or read results only.

**Branch:** `scope/demo` → PR into `main`.

---

## Suggested order of work

1. Open `results/example_fake.csv` with `plot_error_vs_nodes` (see contracts / README).
2. Draft Q&A cards from the table below; ping owners to fix wording.
3. Wire the demo to real CSVs as PRs land (paths, not copy-paste of numbers).
4. Add backup geometry using Anita’s test problems + any ready method.
5. Do one dry run with a teammate asking hard questions.

---

## Oral — you answer / coordinate

| Question | Deep owner | Your job |
|---|---|---|
| Why so many grid points? | Kai | Short card + maybe run the plot |
| Random method vs dimension | Mario | Short card |
| Sparse method internals | Pedro **only** | Card says “Pedro answers” |
| How do we run the demo? | **You** | Live |
| Where do tables come from? | Anita | Short card |

---

## Links

- Contracts: [../contracts.md](../contracts.md)  
- Fake data: [../../results/example_fake.csv](../../results/example_fake.csv)  
- Plan: [../../plan.md](../../plan.md)
