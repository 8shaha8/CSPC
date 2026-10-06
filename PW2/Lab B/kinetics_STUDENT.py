"""
PW2 Lab B Part 3 -- fit a reaction's rate constant to measured data.

A first-order reaction decays as  C(t) = C0 * exp(-k*t).  You have noisy
concentration-vs-time measurements; find the k that best matches them.
Complete the TODOs. Run:  python kinetics.py
"""


# TODO 1: read kinetics.csv (columns time, concentration) into arrays t, C.
#         Set C0 = the first concentration.

# TODO 2: write total_error(k) = sum of (measured - C0*exp(-k*t))^2.
#         This is the "how bad" number: small when the model matches the data.

# TODO 3: minimise total_error with scipy.optimize.minimize (method "SLSQP",
#         bounds [(0, 5)], start x0=0.5). Print the fitted k.

# TODO 4: plot the measured data (points) and your fitted curve (line) together.
#         Save as kinetics.png.
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

data = np.loadtxt("kinetics.csv", delimiter=",", skiprows=1)  # check whether there's a header row
t, C = data[:, 0], data[:, 1]
C0 = C[0]

def total_error(k):
    k = np.atleast_1d(k)[0]
    return np.sum((C - C0 * np.exp(-k * t))**2)

res = minimize(total_error, x0=[0.5], method="SLSQP", bounds=[(0, 5)])
k_fit = res.x[0]
print(f"fitted k = {k_fit:.4f}")

plt.scatter(t, C, label="data")
tt = np.linspace(t.min(), t.max(), 200)
plt.plot(tt, C0 * np.exp(-k_fit * tt), "r", label=f"fit, k={k_fit:.3f}")
plt.xlabel("time"); plt.ylabel("concentration"); plt.legend()
plt.savefig("kinetics.png", dpi=150)