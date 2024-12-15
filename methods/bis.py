def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    """
    Finds a root of a function using the bisection method.

    Args:
        func: The function for which to find a root (should take a single float argument).
        a: The left endpoint of the interval.
        b: The right endpoint of the interval.
        tol: The tolerance for the root (when the interval becomes smaller than this value,
             the algorithm terminates).
        max_iter: The maximum number of iterations allowed.

    Returns:
        The approximate root of the function, or None if the method fails to converge.
    """
    iterations = [(a + b) / 2]
    if func(a) * func(b) >= 0:
        print("Error: f(a) and f(b) must have opposite signs.")
        return None, iterations

    for i in range(max_iter):
        c = (a + b) / 2  # Midpoint
        iterations.append(c)
        if abs(b - a) < tol:
            return c, iterations
        if func(c) == 0:
            return c, iterations  # Exact root found.
        if func(a) * func(c) < 0:
            b = c  # Root lies in the left half.
        else:
            a = c  # Root lies in the right half.

    return None, iterations