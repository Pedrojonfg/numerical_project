# What this project is about (plain words)

**Course:** Numerical Methods · **Group:** Kai, Pedro, Mario, Bhuvi, Anita

This page is the shared story. For “what *I* do day to day,” open your name under [`owners/`](owners/README.md).

---

## The big idea in one minute

In class you saw a careful way to add up (integrate) a function by checking it at a few smart points — great when there is **one** variable.

We ask: what if there are **many** variables at once (2, 3, 4, 5…)?

A naïve answer is: “make a big grid and check every combination.” That shopping list of points **explodes**. The project shows that explosion, tries **better alternatives**, and ends with a small **robot-arm** example so the maths feels useful, not only abstract.

On presentation day we tell that story, show plots, and answer questions. The oral part matters most for the grade.

---

## The three ways we “add up” the function

Think of three teams estimating the same total:

| Nickname | Plain idea | Who builds it |
|---|---|---|
| **Careful grid** (tensor / product rule) | Reuse the classroom 1D rule in every direction; every combination of points | **Kai** |
| **Random darts** (Monte Carlo) | Throw many random points, average, scale by the size of the box | **Mario** |
| **Thinner clever grid** (sparse / Smolyak) | Still structured and mathematical, but with far fewer points than the full grid | **Pedro** (he alone must be able to explain the theory) |

We race them on the **same practice problems** so the comparison is fair.  
In the talk, the careful grid leads the “curse of dimension” story; random darts are the **honest baseline**, not the hero; the thinner grid is our advanced contestant.

---

## The shared playground (so we don’t block each other)

Before the contest, everyone agrees on:

1. **The same box** of inputs: each coordinate between \(-1\) and \(1\) (as in the course notes for Gauss).
2. **The same practice problems** — simple functions we all measure (including “the function that is always 1,” whose total we know exactly).
3. **The same table format** for saving results (CSV files in `results/`), so demos and the report can read numbers without rewriting code.

**Anita** owns that playground: practice problems, table helpers, plotting-from-tables, and the install/dependencies file.  
If someone wants an *extra* practice problem, **that person adds it themselves**.

Because of this playground, Kai, Mario, and Pedro can work **in parallel**. Nobody needs to wait for the robot to start their main method.

---

## The robot toy (why engineers might care)

**Mario** also builds a tiny **two-joint arm**.

For each pair of joint settings we do **not** ask a harsh yes/no “can you reach this pixel?”  
We ask a **soft** question: “how close is the hand to a target?” — a smooth score, high when close, low when far.

Then we add up that score over all joint settings (in our shared box).  
That single number is another function in the contest: every method can try it the same way.

Hard yes/no maps, three joints, animations, and similar polish are **optional extras**, not the core.

---

## How the presentation and report fit together

| Piece | Plain job | Who |
|---|---|---|
| Slide **story order** | Motivation → explosion with dimension → contest → robot → recommendation | **Mario** (arc) |
| **Live demo** | Open plots/tables that already exist; stay calm | **Bhuvi** |
| **Q&A cards** | Who answers what; short backup lines for everyone | **Bhuvi** (cards) + each owner for depth |
| Written **report** | Short Turnitin summary | **Pedro** (skeleton) · each person writes **their** section · **Anita** builds number tables from CSVs |
| Deep sparse-method theory | Only one person must go deep | **Pedro** |

Likely deep questions:

- Why does the full grid need so many points? → **Kai**
- What does “exact for polynomials up to …” mean in 1D? → **Kai** / **Anita**
- Why doesn’t random sampling explode the same way? → **Mario**
- What is the thinner grid doing? When does it lose? → **Pedro only**
- Why this robot score? → **Mario**
- How do we run the demo / read the plots? → **Bhuvi**
- Where do the practice problems and tables come from? → **Anita**

---

## Who does what (map)

```text
Anita ── shared practice problems, CSV/plots toolkit, dependencies
          │
          ▼
   ┌──────┼──────────────┐
   ▼      ▼              ▼
  Kai   Mario         Pedro
  grid  random darts  thinner grid
         + robot score   + compare-all notebook
                         + report skeleton
                         + extras if we keep them
          │
          ▼
        Bhuvi
        demo + Q&A cards (+ backup geometry picture)
```

**Pull requests:** each person works on their own area, then opens a PR into `main`. Do not casually edit someone else’s files.

**If something must be cut:** optional extras go first; Pedro breaks ties. The group can reopen that list if a core piece is at risk. If load spills, **Pedro absorbs the extra**, not the others.

---

## What success looks like for the group

We can show:

1. Pictures of the grid exploding with dimension.  
2. A fair contest on shared practice problems (at least careful grid vs random darts; thinner grid if ready).  
3. The robot soft-score example.  
4. A clear recommendation: which idea fits which situation.  
5. Everyone able to answer questions about the shared story; specialists ready for their deep parts.

---

## Where to go next

| If you want… | Open |
|---|---|
| Your personal checklist | [`owners/`](owners/README.md) |
| Locked technical agreements | [`contracts.md`](contracts.md) |
| Full planning detail | [`../plan.md`](../plan.md) |
| How to install / run | [`../README.md`](../README.md) |
