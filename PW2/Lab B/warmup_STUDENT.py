"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  python warmup.py
"""
import numpy as np
from scipy.optimize import newton, minimize

# ---------- 2A: easy convex function ----------
def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

# TODO 2A: minimise f three ways from x0=0 and print each result:
#   (1) gradient descent by hand (loop x = x - lr*df(x) until the step is tiny)
#   (2) scipy.optimize.newton(df, x0, fprime=d2f)
#   (3) scipy.optimize.minimize(f, x0, method="SLSQP")

# ---------- 2B: harder landscape ----------
def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

# TODO 2B: run the same three methods on g, from x0=0 AND from x0=2.
#   For Newton (which solves dg(x)=0), also check the sign of d2g at the answer:
#   d2g > 0 means a minimum, d2g < 0 means a maximum.
#   In your README note: do the methods agree? did Newton find a minimum or
#   another stationary point? how did the starting point change the result?
# ---------- the three methods ----------
def gradient_descent(dfunc, x0, lr=0.01, tol=1e-8, max_iter=100000):
    x = x0
    for _ in range(max_iter):
        step = lr * dfunc(x)
        x = x - step
        if abs(step) < tol:      # stop when the step is tiny
            break
    return x

def run_all(name, func, dfunc, d2func, x0, lr):
    gd = gradient_descent(dfunc, x0, lr=lr)
    nt = newton(dfunc, x0, fprime=d2func)
    sl = minimize(lambda v: func(v[0]), [x0], method="SLSQP").x[0]
    kind = "minimum" if d2func(nt) > 0 else "maximum"
    print(f"{name}, x0={x0}, lr={lr}")
    print(f"  gradient descent: x = {gd:.4f}, value = {func(gd):.4f}")
    print(f"  Newton:           x = {nt:.4f}, value = {func(nt):.4f}, "
          f"second derivative = {d2func(nt):.3f} -> {kind}")
    print(f"  SLSQP:            x = {sl:.4f}, value = {func(sl):.4f}")

# ---------- 2A ----------
run_all("2A f", f, df, d2f, 0.0, lr=0.1)

# ---------- 2B ----------
for x0 in (0.0, 2.0):
    run_all("2B g", g, dg, d2g, x0, lr=0.01)

# step-size experiment for your README (gradient descent only)
print("g, x0=2, lr=0.1 :", round(gradient_descent(dg, 2.0, lr=0.1), 4))
print("g, x0=2, lr=0.01:", round(gradient_descent(dg, 2.0, lr=0.01), 4))