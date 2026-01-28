import time

import numpy as np

print("Matrix-Vector Multiplication Time Complexity Test")
print("-" * 90)
print(
    f"{'n':<8} | {'Loop Time (s)':<18} | {'NumPy @ Time (s)':<18} | {'Loop Ratio':<15}"
)
print("-" * 90)

n = 100
prev_loop_time = None

for _ in range(6):
    A = np.random.rand(n, n)
    x = np.random.rand(n, n)

    # ------------------------
    # 1. Python loops
    # ------------------------
    b = np.zeros((n, n))
    t0 = time.perf_counter()
    for k in range(n):
        for i in range(n):
            for j in range(n):
                b[i, k] += A[i, j] * x[j, k]

    t1 = time.perf_counter()
    loop_time = t1 - t0

    # ------------------------
    # 2. NumPy (BLAS)
    # ------------------------
    t0 = time.perf_counter()
    b = A @ x
    t1 = time.perf_counter()
    numpy_time = t1 - t0

    # ------------------------
    # Ratio
    # ------------------------
    if prev_loop_time is None:
        ratio = "N/A"
    else:
        ratio = f"{loop_time / prev_loop_time:.2f}"

    print(f"{n:<8} | {loop_time:<18.8f} | {numpy_time:<18.8f} | {ratio:<15}")

    prev_loop_time = loop_time
    n *= 2

print("-" * 90)
