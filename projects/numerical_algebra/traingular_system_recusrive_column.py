import numpy as np


def triangular_recursive_column(L, b):
    n = len(b)
    y = b.astype(float).flatten().copy()

    def helper(k):
        if k >= n:
            return

        # Solve current variable
        if L[k, k] == 0:
            raise ZeroDivisionError(f"Zero diagonal at index {k}")

        y[k] /= L[k, k]

        # Update remaining block (down the column)
        for i in range(k + 1, n):
            y[i] -= L[i, k] * y[k]

        # Recurse to next column
        helper(k + 1)

    helper(0)
    return y


L = np.array([[2, 0, 0, 0], [-1, 2, 0, 0], [3, 1, -1, 0], [4, 1, -3, 3]])

b = np.array([[2], [3], [2], [9]])

y = triangular_recursive_column(L, b)
print("Solution y:", y)
