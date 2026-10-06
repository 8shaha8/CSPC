"""
PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point.

titration.csv holds a titration curve: pH versus the volume of base added.
The equivalence point is the volume where the pH changes fastest (the steep
jump). Numerically, that is where the SLOPE of the pH curve is largest.
Run:  python titration.py
"""


# TODO 1: read titration.csv (columns volume_base, pH) into arrays V, pH.

# TODO 2: compute the slope of the pH curve with np.gradient(pH, V), and find
#         the volume where that slope is largest (np.argmax). That is the
#         equivalence point. Print it.

# TODO 3: make two plots side by side: (left) pH vs volume with a line at the
#         equivalence point; (right) the slope vs volume, showing it peaks
#         at the equivalence point. Save as titration.png.
import numpy as np
import matplotlib.pyplot as plt

V, pH = np.loadtxt("titration.csv", delimiter=",", skiprows=1, unpack=True)
slope = np.gradient(pH, V)
i = np.argmax(slope)
print(f"equivalence point: {V[i]:.1f} mL")

fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4))
a1.plot(V, pH); a1.axvline(V[i], color="r", ls="--")
a1.set_xlabel("volume base (mL)"); a1.set_ylabel("pH")
a2.plot(V, slope); a2.axvline(V[i], color="r", ls="--")
a2.set_xlabel("volume base (mL)"); a2.set_ylabel("dpH/dV")
plt.tight_layout()
plt.savefig("titration.png", dpi=150)