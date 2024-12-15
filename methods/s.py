def secant_method(func, x0, x1, tol=1e-6, max_iter=100):
    """
    Finds a root of a function using the secant method.

    Args:
        func: The function for which to find a root (should take a single float argument).
        x0: The first initial guess for the root.
        x1: The second initial guess for the root.
        tol: The tolerance for the root (when the difference between successive
             approximations is less than this value, the algorithm terminates).
        max_iter: The maximum number of iterations allowed.

    Returns:
        The approximate root of the function, or None if the method fails to converge.
    """
    iterations = [x0, x1]  # store the initial points and subsequent iterations
    for i in range(max_iter):
        fx0 = func(x0)
        fx1 = func(x1)
        if abs(fx1 - fx0) < 1e-12:
            return None, iterations  # Indicates a problem
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        iterations.append(x2)
        if abs(x2 - x1) < tol:
            return x2, iterations
        x0 = x1
        x1 = x2
    return None, iterations