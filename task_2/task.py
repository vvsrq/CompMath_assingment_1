from math import *
from methods import bis, s, nr, iter
import numpy as np
import matplotlib.pyplot as plt

def plot_results(f, iterations_dict, range_start, range_end, title="Root-Finding Methods"):
    """Plots the function and the iterations of different methods."""

    x = np.linspace(range_start, range_end, 400)  # generate x-values to evaluate function at
    y = f(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='f(x)', color='blue', lw=2)  # Plot the original function

    # add markers for each of the iterative steps for each method
    markers = ['o', 'x', '+', '*']  # Markers to use for different methods
    i = 0

    # plot the iteration points for each method.
    for method_name, iterations in iterations_dict.items():
        if iterations:
            plt.plot(iterations, [f(xi) for xi in iterations], marker=markers[i % 4], linestyle='--',
                     label=method_name)
            i = i + 1

    plt.axhline(0, color='black', lw=0.5)  # Add x-axis to graph
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()


def f(x):
    return np.cos(x) - x*np.exp(x)


def df(x):
    return -np.sin(x) - np.exp(x)*(1 + x)


def g(x):
    return np.cos(x) / np.exp(x)

a = 1
b = -2

root_bisection, iterations_bisection = bis.bisection_method(f, a, b)
if root_bisection is not None:
    print("Bisection method: Root:", root_bisection)
    print("Function value at the root:", f(root_bisection))
else:
    print("Bisection method: Did not converge or invalid interval")

print("========================")

root_secant, iterations_secant = s.secant_method(f, a, b)
if root_secant is not None:
    print("Secant method: Root:", root_secant)
    print("Function value at the root:", f(root_secant))
else:
    print("Secant method: Did not converge or invalid interval")

print("========================")

root_newton, iterations_newton = nr.newton_raphson_method(f, df, a)
if root_newton is not None:
    print("newton_raphson_method method: Root:", root_newton)
    print("Function value at the root:", f(root_newton))
else:
    print("newton_raphson_method: Did not converge or invalid interval")

print("========================")

root_iteration, iterations_iteration = iter.iteration_method(g, a)
if root_iteration is not None:
    print("Iter method: Root:", root_iteration)
    print("Function value at the root:", f(root_iteration))
else:
    print("Iter method: Did not converge or invalid interval")

print("========================")

# Print root if found
if root_secant is not None:
    print("Secant method: Root:", root_secant)
if root_iteration is not None:
    print("Iteration method: Root:", root_iteration)
if root_newton is not None:
    print("Newton-Raphson method: Root:", root_newton)
if root_bisection is not None:
    print("Bisection method: Root:", root_bisection)

iterations_dict = {"Secant":iterations_secant, "Iteration":iterations_iteration, "Newton-Raphson": iterations_newton, "Bisection":iterations_bisection}

plot_results(f, iterations_dict, -1, 3, title = "Root-Finding methods for f(x) = x - cos(x) ")