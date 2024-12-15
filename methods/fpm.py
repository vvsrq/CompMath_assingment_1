def false_position_method(func, a, b, tol=1e-6, max_iter=100):
    """
    Finds a root of a function using the false position method.

    Args:
        func: The function for which to find a root (should take a single float argument).
        a: The left endpoint of the interval.
        b: The right endpoint of the interval.
        tol: The tolerance for the root (when the difference between successive
            approximations is less than this value, the algorithm terminates).
        max_iter: The maximum number of iterations allowed.

    Returns:
        The approximate root of the function, or None if the method fails to converge.
    """
    if func(a) * func(b) >= 0:
        print("Error: f(a) and f(b) must have opposite signs.")
        return None

    for i in range(max_iter):
        fa = func(a)
        fb = func(b)
        # Calculate the x-intercept of the secant line using the secant formula
        c = b - fb * (b - a) / (fb - fa)
        fc = func(c)

        if abs(fc) < tol:
            return c  # Root found
        if fa * fc < 0:
            b = c  # Root in the left subinterval
        else:
            a = c  # Root in the right subinterval
    return None # Did not converge

if __name__ == '__main__':
    # Example function: f(x) = x^2 - 2
    def f(x):
        return x**2 - 2

    # Initial interval
    a = 1.0
    b = 2.0

    root = false_position_method(f, a, b)
    if root is not None:
        print("False Position method: Root:", root)
        print("Function value at the root:", f(root))
    else:
        print("False Position method: Did not converge or invalid interval")