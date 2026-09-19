import time
import decay
N0 = 200_000
lam = 0.4

start = time.perf_counter()
decay.simulate_loop(N0, lam)
loop_time = time.perf_counter() - start


start = time.perf_counter()
decay.simulate(N0, lam)
numpy_time = time.perf_counter() - start

print(f"loop : {loop_time:.4f} s")
print(f"numpy: {numpy_time:.4f} s")
print(f"speed-up: {loop_time / numpy_time:.1f}x faster")