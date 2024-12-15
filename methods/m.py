import numpy as np
def muller_method(func, x0, x1, x2, tol=1e-6, max_iter=100):
    """
    Finds a root of a function using Muller's method.

    Args:
        func: The function for which to find a root (should take a single float argument).
        x0, x1, x2: Initial guesses for the root.
        tol: The tolerance for the root (when the difference between successive
             approximations is less than this value, the algorithm terminates).
        max_iter: The maximum number of iterations allowed.

    Returns:
        The approximate root of the function, or None if the method fails to converge.
    """

    for i in range(max_iter):
        f0 = func(x0)
        f1 = func(x1)
        f2 = func(x2)
        h1 = x1 - x0
        h2 = x2 - x1
        delta1 = (f1 - f0) / h1
        delta2 = (f2 - f1) / h2
        a = (delta2 - delta1) / (h2 + h1)
        b = a * h2 + delta2
        c = f2
        discriminant = b**2 - 4 * a * c
        if discriminant >= 0:
            if b > 0:
              x3 = x2 + (-2*c)/(b + np.sqrt(discriminant))
            else:
              x3 = x2 + (-2*c)/(b - np.sqrt(discriminant))
        else:
          if b > 0:
            x3 = x2 + (-2*c)/(b + np.sqrt(discriminant))
          else:
            x3 = x2 + (-2*c)/(b - np.sqrt(discriminant))

        if abs(x3 - x2) < tol:
            return x3
        x0 = x1
        x1 = x2
        x2 = x3

    return None  # Method failed to converge


if __name__ == '__main__':
    # Example function: f(x) = x^2 - 2
    def f(x):
        return x**2 - 2

    # Initial guesses
    x0 = 0.0
    x1 = 1.0
    x2 = 2.0

    root = muller_method(f, x0, x1, x2)
    if root is not None:
        print("Muller's method: Root:", root)
        print("Function value at the root:", f(root))
    else:
        print("Muller's method: Did not converge")