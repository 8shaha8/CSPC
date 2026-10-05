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

##PW2 - Lab A
**Mean acceleration:** -9.xx m/s² (standard deviation: x.xx m/s²).
This is close to -g = -9.81 m/s², so the object is in free fall.

**Why acceleration is noisy:** Each time you take a derivative, the small errors in the data get bigger. Acceleration needed two derivatives, so it is much noisier than position.

**Integrating back:** I integrated the noisy acceleration to get velocity, then integrated again to get position. The largest difference from the original position was x.xx m. This shows that integration reduces noise, because random errors partly cancel when you add things up.



