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