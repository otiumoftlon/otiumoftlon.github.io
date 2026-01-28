import matplotlib.pyplot as plt
import numpy as np


def scanning_method(func, start, end, step):
    root_intervals = []

    x_values = np.arange(start, end + step, step)

    for i in range(len(x_values) - 1):
        a = x_values[i]
        b = x_values[i + 1]

        fa = func(a)
        fb = func(b)

        if fa * fb < 0:
            root_intervals.append((a, b))
            print(f"Root found in interval: [{a:.4f}, {b:.4f}]")

    return root_intervals


def bisection_method(func, x_n, x_l, tol=1e-5):

    iteration = 0
    while (x_l - x_n) / 2.0 > tol:
        iteration += 1
        midpoint = (x_n + x_l) / 2.0
        if func(midpoint) == 0:
            return midpoint
        elif func(x_n) * func(midpoint) < 0:
            x_l = midpoint
        else:
            x_n = midpoint

    return (x_n + x_l) / 2.0, iteration


def chords_method(func, x_n, x_n1, tol=1e-6):

    iteration = 0
    max_iter = 1000

    if func(x_n) == 0:
        return x_n, 0
    if func(x_n1) == 0:
        return x_n1, 0

    while True:
        iteration += 1

        f_xn = func(x_n)
        f_xn1 = func(x_n1)

        k = abs(f_xn) / abs(f_xn1)

        x_mid = (x_n + k * x_n1) / (1 + k)

        f_mid = func(x_mid)

        if abs(f_mid) < tol:
            return x_mid, iteration

        if np.sign(f_mid) == np.sign(f_xn):
            x_n = x_mid
        else:
            x_n1 = x_mid

        if iteration >= max_iter:
            print("Max iterations reached")
            break

    return x_mid, iteration


def newton_method(func, d_func, x0, tol=1e-6, max_iter=1000):
    iteration = 0
    x_n = x0

    while iteration < max_iter:
        iteration += 1
        f_xn = func(x_n)
        d_f_xn = d_func(x_n)

        if d_f_xn == 0:
            print("Derivative is zero. No solution found.")
            return None, iteration

        x_n1 = x_n - f_xn / d_f_xn

        if abs(x_n1 - x_n) < tol:
            return x_n1, iteration

        x_n = x_n1

    print("Max iterations reached")
    return x_n, iteration


def polynomial(x):

    return 0.1 * x**5 - 0.05 * x**4 - 1.95 * x**3 + 1.75 * x**2 + 5.18 * x - 2.14


def derivate_polynomial(x):
    return 5 * 0.1 * x**4 - 4 * 0.05 * x**3 - 3 * 1.95 * x**2 + 2 * 1.75 * x + 5.18


def transcendental(x):

    return ((x + 1) ** 2 * (x - 3) ** 2) / (x**3 + 2) + (x - 2) ** 3 * np.cos(x)


def derivative_transcendental(x):
    term1 = 2 * (x + 1) * (x - 3) ** 2 / (x**3 + 2)
    term2 = (x + 1) ** 2 * 2 * (x - 3) / (x**3 + 2)
    term3 = -3 * x**2 * ((x + 1) ** 2 * (x - 3) ** 2) / (x**3 + 2) ** 2
    term4 = 3 * (x - 2) ** 2 * np.cos(x)
    term5 = -((x - 2) ** 3) * np.sin(x)
    return term1 + term2 + term3 + term4 + term5


x_polynomial = np.linspace(-20.5, 5.62, 500)
y_polynomial = polynomial(x_polynomial)

x_transcendental = np.linspace(0, 15, 500)
y_transcendental = transcendental(x_transcendental)

plt.plot(x_polynomial, y_polynomial)
plt.title("Plot of the Polynomial Function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()

plt.plot(x_transcendental, y_transcendental)
plt.title("Plot of the Transcendental Function")
plt.xlabel("x")
plt.ylabel("g(x)")
plt.grid(True)
plt.show()

print("Polynomial Function Root Intervals:")
root_intervals_polynomial = scanning_method(polynomial, -5.42, 22.4, 0.6)


plt.plot(x_polynomial, y_polynomial)
for interval in root_intervals_polynomial:
    plt.axvline(x=interval[0], color="r", linestyle="--")
    plt.axvline(x=interval[1], color="r", linestyle="--")
plt.title("Plot of the Polynomial Function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()


print("Transcendental Function Root Intervals:")
root_intervals_trasncendental = scanning_method(transcendental, 0, 15, 0.6)

plt.plot(x_transcendental, y_transcendental)
for interval in root_intervals_trasncendental:
    plt.axvline(x=interval[0], color="r", linestyle="--")
    plt.axvline(x=interval[1], color="r", linestyle="--")
plt.title("Plot of the Transcendental Function")
plt.xlabel("x")
plt.ylabel("g(x)")
plt.grid(True)
plt.show()

print("##" * 20)

print("Bisection Method Results for Polynomial Function:")
for interval in root_intervals_polynomial:
    root, iterations = bisection_method(polynomial, interval[0], interval[1], tol=1e-6)
    print(f"Root: {root:.6f}, Iterations: {iterations}")

print("Bisection Method Results for Transcendental Function:")
for interval in root_intervals_trasncendental:
    root, iterations = bisection_method(
        transcendental, interval[0], interval[1], tol=1e-6
    )
    print(f"Root: {root:.6f}, Iterations: {iterations}")

print("##" * 20)
print("Chords Method Results for Polynomial Function:")
for interval in root_intervals_polynomial:
    root, iterations = chords_method(polynomial, interval[0], interval[1], tol=1e-6)
    print(f"Root: {root:.6f}, Iterations: {iterations}")

print("Chords Method Results for Transcendental Function:")
for interval in root_intervals_trasncendental:
    root, iterations = chords_method(transcendental, interval[0], interval[1], tol=1e-6)
    print(f"Root: {root:.6f}, Iterations: {iterations}")

print("##" * 20)
print("Newton Method Results for Polynomial Function:")
for interval in root_intervals_polynomial:
    x0 = (interval[0] + interval[1]) / 2
    root, iterations = newton_method(polynomial, derivate_polynomial, x0, tol=1e-6)
    print(f"Root: {root:.6f}, Iterations: {iterations}")

print("Newton Method Results for Transcendental Function:")
for interval in root_intervals_trasncendental:
    x0 = (interval[0] + interval[1]) / 2
    root, iterations = newton_method(
        transcendental, derivative_transcendental, x0, tol=1e-6
    )
    print(f"Root: {root:.6f}, Iterations: {iterations}")
