# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n>/Lab <X>/.
## Setup
Create the environment for a given lab:
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc
---
## PW1 — Lab A: Reproducible Foundations
**What I built:**
Created the CSPC repository with a PW1/Lab A/ folder, an environment.yml, and a .gitignore.
Added decay.py and a pytest test file with three tests.
Used a lab-a-work branch merged back into main, then pushed everything to GitHub.

**Speed comparison (loop vs NumPy):**
loop  : 2.6891 s
numpy : 0.0003 s
speed-up: 8629.1x faster

**Tests:**
all passing? yes(3 passed)

**Conclusion:**
The Python loop was about 8600 times slower than the NumPy version, so NumPy is much better for big numbers. I also learned how to write pytest tests that check for errors and for close float values. The only problem I had was GitHub not accepting my password, which I fixed by using a token.
## Pw1 — Lab B
I plotted the data from `decay_observed.csv` and it matches the decay curve
N(t) = N0 · exp(−λt) with N0 = 5000 and λ = 0.3. The observed points and the
curve look the same, so the data follows the law.
`plot.py` makes `figure.png`. The `Snakefile` runs `plot.py` and only rebuilds
the figure when the data or the script changes.

## PW2 - Lab A
**Mean acceleration:** -9.xx m/s² (standard deviation: x.xx m/s²).
This is close to -g = -9.81 m/s², so the object is in free fall.

**Why acceleration is noisy:** Each time you take a derivative, the small errors in the data get bigger. Acceleration needed two derivatives, so it is much noisier than position.

**Integrating back:** I integrated the noisy acceleration to get velocity, then integrated again to get position. The largest difference from the original position was x.xx m. This shows that integration reduces noise, because random errors partly cancel when you add things up.
## PW2 - Lab B

**Part 2 (optimization methods).**

- On the easy function f(x), all three methods find x = 3. They agree.
- On the harder function g(x), they do not always agree. g has three flat points: a global minimum at x = -1.30, a maximum at x = 0.17 and a local minimum at x = 1.13.
- From x0=0, Newton found the maximum (x = 0.1699, g'' = -5.65, which is negative), not a minimum. Newton only looks for a flat point, so I have to check the sign of g''. Gradient descent and SLSQP found the global minimum (x = -1.30).
- From x0=2, Newton and gradient descent found the local minimum (x = 1.1309, g'' = 9.35), but SLSQP found the global minimum (x = -1.3006).
- So the starting point changes the result. The step size matters too: from x0=2, lr=0.1 ended at -1.3008, but lr=0.01 ended at 1.1309.
- Lesson: easy problems are simple, but on harder ones the starting point and the method matter.

**Part 3 (kinetics).** The fitted rate constant is k = 0.2618, which is close to the expected 0.25. The fitted curve passes through the data (see `PW2/Lab B/kinetics.png`).

**Part 4 (equilibrium).** Newton and SLSQP agree: x = 0.6638. At equilibrium H2 = 0.336 mol, I2 = 0.336 mol and HI = 1.328 mol (see `PW2/Lab B/equilibrium.png`).

**Part 5 (titration, bonus).** The equivalence point is at 50.0 mL, where the pH curve is steepest (see `PW2/Lab B/titration.png`).


