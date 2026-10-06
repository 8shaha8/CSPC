"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# TODO 1: write k_imbalance(x) = (2x)^2/((a-x)(b-x)) - K.
#         It equals zero exactly at equilibrium.

# TODO 2 (method 1): use scipy.optimize.newton to find the root of k_imbalance
#         (start x0=0.5). This is root-finding.

# TODO 3 (method 2): use scipy.optimize.minimize to minimise k_imbalance(x)**2
#         (method "SLSQP", bounds [(0, 0.999)], x0=[0.5]). Print both answers
#         and confirm they agree.

# TODO 4: report the equilibrium amounts (H2, I2, HI), and plot how the three
#         amounts change with the extent x, marking the equilibrium. Save
#         equilibrium.png.
def k_imbalance(x):
    return (2*x)**2 / ((a - x) * (b - x)) - K

# 1) Newton (root-finding)
x_newton = newton(k_imbalance, 0.5)

# 2) SLSQP (minimise the squared imbalance)
res = minimize(lambda v: k_imbalance(v[0])**2, [0.5],
               method="SLSQP", bounds=[(0, 0.999)], tol=1e-12)
x_slsqp = res.x[0]

print(f"Newton x = {x_newton:.4f}")
print(f"SLSQP  x = {x_slsqp:.4f}")

# equilibrium amounts
x = x_newton
print(f"H2 = {a - x:.3f} mol, I2 = {b - x:.3f} mol, HI = {2*x:.3f} mol")

# plot
xs = np.linspace(0, 0.99, 200)
plt.plot(xs, a - xs, label="H2")
plt.plot(xs, b - xs, "--", label="I2")
plt.plot(xs, 2 * xs, label="HI")
plt.axvline(x, color="k", ls=":", label=f"equilibrium x = {x:.2f}")
plt.xlabel("extent x")
plt.ylabel("moles")
plt.legend()
plt.savefig("equilibrium.png", dpi=150)