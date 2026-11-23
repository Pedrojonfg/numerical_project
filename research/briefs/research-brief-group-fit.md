# Research Brief: Numerical Methods Final Project — Group Fit
**Depth**: deep  
**Date**: 2026-11-23  
**Course**: Numerical Methods (M. Vaquero), BAM Y2 — project 15% of grade (70% oral Q&A, 30% brief report), deadline 16 Dec  

## Executive Summary
Survey responses from four members (fifth assumed indifferent and syllabus-only) point to **multidimensional integration**, **robotics / geometry / ML numerics**, and **oral defendability** as the strongest shared constraints. Official project brief explicitly recommends Monte Carlo, multidimensional integration, and BVPs (not lectured). Four proposals below isolate any out-of-syllabus depth so **Pedro** can own it alone; everyone else stays on lecture + short notes / suggested-topic tutorials.

## Competitive / Constraint Landscape (course rules)
| Constraint | Implication |
|---|---|
| Oral = 70% | Prefer stories with a clear “why this method”, demo plots, and Q&A ownership per person |
| Group of 5 | Need substantial scope: method comparison + one real application + experiments |
| Unique topics (first-come) | Claim early; originality still scored even on suggested list |
| Not covered in class (explicit) | Monte Carlo, multidimensional integration, BVPs — green-light project topics |
| Suggested list | Quasi-Newton, orthogonal polynomials, unconstrained optimization, MC, smoothing splines, minimax, L2 approximation |

## Survey Synthesis
| Person | Beyond-class ceiling | Method highs | Hard avoids | Ideal “10” |
|---|---|---|---|---|
| **Pedro** | Research-flavor (9) | Opt 10, MC 9, multi-D 8, BVP/IVP 8 | Pure theory-only orientation | Deep method + impactful app |
| **Kai** | Textbook/adapt (8) | Multi-D **10**, orth. polys 8, opt 8, IVP 7 | Minimax 0, L2 poly 0, splines 1, education demos, error-centric narrative | Rigorous but fully masterable |
| **Mario** | Short notes (5) | MC 8, multi-D 7, BVP/IVP 7 | Biology; only-theory projects | Impact + strong slides |
| **Bhuvi** | Short notes (4) | Flat mid scores; finance lean | Wants easy live Q&A | Defendable answers |
| **Member 5** | Syllabus only (assumed) | Indifferent | No extra study | Clear, limited scope |

**Best consensus method**: Multidimensional integration (avg 7.8, min 6).  
**Best consensus apps**: Robotics/control (min 6), ML numerics (min 5), geometry (min 5).  
**Avoid as spine**: Smoothing splines, minimax-as-project, biology, didactic-demo framing, floating-point/error-theory deep dive.

## Four Proposals (detail in `research/proposals/`)
1. Multidimensional quadrature vs sparse grids vs MC — robot / geometry volumes  
2. Quasi-Newton (BFGS) for planar robot inverse kinematics  
3. Orthogonal polynomials → Gaussian quadrature → (Pedro) Chebyshev spectral collocation  
4. Shooting-method BVPs for ballistic / soft-landing trajectories  

## Sources
- Course PDF: `Numerical_Methods_TODO.pdf` (Final Project §, roadmap, suggested topics)  
- Intake CSV: Topic priorities survey (4 respondents)  
- Sparse grids / Smolyak notes; OpenTURNS Smolyak demo; sparse-grids.de  
- TAMU CSCE450 BFGS+IK assignment; NTNU IK+BFGS student project  
- BYU ACME Gaussian quadrature & shooting labs; Python Numerical Methods shooting chapter  
- Kelly transcription notes (multiple shooting / trajectory optimization)  
