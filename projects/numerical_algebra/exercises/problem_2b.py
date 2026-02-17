import matplotlib.pyplot as plt
import numpy as np

def F(vars):
    x, y = vars
    f1 = (x - 1) ** 2 + y - 10
    f2 = x**2 + y**2 + 4 * x * np.cos(x + y) - 40
    return np.array([f1, f2])


def J(vars):
    x, y = vars

    df1_dx = 2 * (x - 1)
    df1_dy = 1.0

    df2_dx = 2 * x + 4 * np.cos(x + y) - 4 * x * np.sin(x + y)

    df2_dy = 2 * y - 4 * x * np.sin(x + y)

    return np.array([[df1_dx, df1_dy], [df2_dx, df2_dy]])


def newton_system(initial_guess, tolerance=1e-6, max_iter=100):
    x_current = np.array(initial_guess, dtype=float)
    path = [x_current.copy()] 

    for i in range(max_iter):
        F_val = F(x_current)
        J_val = J(x_current)

        if np.linalg.norm(F_val) < tolerance:
            print(f"Converged in {i} iterations.")
            return x_current, np.array(path)

        delta = np.linalg.solve(J_val, -F_val)
        x_current = x_current + delta
        path.append(x_current.copy())

    print("Did not converge.")
    return x_current, np.array(path)


initial_guess = [[2.0, 8.0], [-3, -6], [-1, 7], [5, -5]]

for guess in initial_guess:
    root, path = newton_system(guess)

    print(f"Root found at: x={root[0]:.4f}, y={root[1]:.4f}")
    print(f"Function values at root: {F(root)}")

    x_grid = np.arange(-10, 10, 0.1)
    y_grid = np.arange(-10, 10, 0.1)
    X, Y = np.meshgrid(x_grid, y_grid)

    Z1 = (X - 1) ** 2 + Y - 10
    Z2 = X**2 + Y**2 + 4 * X * np.cos(X + Y) - 40

    plt.figure(figsize=(10, 8))

    c1 = plt.contour(X, Y, Z1, levels=[0], colors="blue", linewidths=2)
    c2 = plt.contour(X, Y, Z2, levels=[0], colors="red", linewidths=2)
    plt.clabel(c1, fmt="f1=0", inline=True)
    plt.clabel(c2, fmt="f2=0", inline=True)

    plt.plot(
        path[:, 0],
        path[:, 1],
        "-o",
        color="green",
        label="Newton Path",
        linewidth=2,
        markersize=5,
    )
    plt.plot(root[0], root[1], "k*", markersize=15, label="Found Root")
    plt.plot(guess[0], guess[1], "ko", label="Start")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Newton Method Convergence\nStart: {guess} -> End: {np.round(root, 3)}")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.axis("equal")
    plt.show()
