import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def f1(x, y):
    return (x - 1) ** 2 + y - 10

def f2(x, y):
    return x**2 + y**2 + 4 * x * np.cos(x + y) - 40

def Z(func, x, y):
    X, Y = np.meshgrid(x, y, indexing="xy")
    Z_val = func(X, Y)
    return Z_val

x = np.arange(-10, 10, 0.1)
y = np.arange(-10, 10, 0.1)

Z1 = Z(f1, x, y)
Z2 = Z(f2, x, y)
Xg, Yg = np.meshgrid(x, y, indexing="xy")


fig = plt.figure(figsize=(16, 12))



def set_3d_axes(ax, title):
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.set_zlim(-30, 30)
    ax.view_init(elev=30, azim=45)



ax1 = fig.add_subplot(2, 2, 1, projection="3d")
ax1.plot_surface(Xg, Yg, Z1, alpha=0.4, color="blue", rstride=5, cstride=5)
ax1.contour(Xg, Yg, Z1, levels=[0], colors="darkblue", linewidths=2)
set_3d_axes(ax1, "1. Surface f1 (Blue)")


ax2 = fig.add_subplot(2, 2, 2, projection="3d")
ax2.plot_surface(Xg, Yg, Z2, alpha=0.4, color="red", rstride=5, cstride=5)
ax2.contour(Xg, Yg, Z2, levels=[0], colors="darkred", linewidths=2)
set_3d_axes(ax2, "2. Surface f2 (Red)")


ax3 = fig.add_subplot(2, 2, 3, projection="3d")

ax3.plot_surface(Xg, Yg, Z1, alpha=0.3, color="blue", rstride=5, cstride=5)
ax3.plot_surface(Xg, Yg, Z2, alpha=0.3, color="red", rstride=5, cstride=5)
ax3.contour(Xg, Yg, Z1, levels=[0], zdir="z", offset=-30, colors="blue", linewidths=2)
ax3.contour(Xg, Yg, Z2, levels=[0], zdir="z", offset=-30, colors="red", linewidths=2)
set_3d_axes(ax3, "3. Both Surfaces Intersection")
ax3.text2D(0.05, 0.95, "Contours projected at bottom", transform=ax3.transAxes)

ax4 = fig.add_subplot(2, 2, 4)
c1 = ax4.contour(Xg, Yg, Z1, levels=[0], colors="blue", linewidths=2)
c2 = ax4.contour(Xg, Yg, Z2, levels=[0], colors="red", linewidths=2)

ax4.clabel(c1, fmt="f1=0", inline=True)
ax4.clabel(c2, fmt="f2=0", inline=True)

ax4.set_xlabel("x")
ax4.set_ylabel("y")
ax4.set_title("4. Zero Contours (Solution Set)", fontsize=14, fontweight="bold")
ax4.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()
