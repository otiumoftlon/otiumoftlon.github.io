import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import BarycentricInterpolator, CubicSpline


def f(x):

    return np.log(x) / (np.sin(2 * x) + 1.5)



start, end = 0.5, 10

x_dense = np.linspace(start, end, 500)
y_dense = f(x_dense)


node_counts = [8, 14, 20]


fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharey=True)


for i, N in enumerate(node_counts):


    x_nodes = np.linspace(start, end, N)
    y_nodes = f(x_nodes)

    poly_interpolator = BarycentricInterpolator(x_nodes, y_nodes)
    y_poly = poly_interpolator(x_dense)

    spline_interpolator = CubicSpline(x_nodes, y_nodes)
    y_spline = spline_interpolator(x_dense)

    ax = axes[i]

    ax.plot(
        x_dense, y_dense, "k--", linewidth=1.5, alpha=0.6, label="True Function f(x)"
    )


    ax.plot(x_dense, y_poly, "r-", linewidth=1.5, label=f"Polynomial")
    ax.plot(x_dense, y_spline, "b-", linewidth=1.5, label="Cubic Spline")
    ax.scatter(x_nodes, y_nodes, color="black", zorder=5, s=30, label="Nodes")

    ax.set_title(f"N = {N} Points")
    ax.set_xlabel("x")
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.set_ylim(-20, 20)


axes[0].legend(loc="upper left")
axes[0].set_ylabel("f(x)")

plt.suptitle(f"Comparison: Polynomial vs Spline Interpolation", fontsize=16)
plt.tight_layout()
plt.show()
