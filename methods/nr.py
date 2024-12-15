def newton_raphson_method(func, deriv, x0, tol=1e-6, max_iter=100):
    """
    Finds a root of a function using the Newton-Raphson method.

    Args:
        func: The function for which to find a root (should take a single float argument).
        deriv: The derivative of the function (should take a single float argument).
        x0: The initial guess for the root.
        tol: The tolerance for the root (when the difference between successive
             approximations is less than this value, the algorithm terminates).
        max_iter: The maximum number of iterations allowed.

    Returns:
        The approximate root of the function, or None if the method fails to converge.
    """
    iterations = [x0]
    x = x0
    for i in range(max_iter):
        fx = func(x)
        dfx = deriv(x)
        if abs(dfx) < 1e-12:
            return None, iterations  # Indicates a problem
        x_next = x - fx / dfx
        iterations.append(x_next)
        if abs(x_next - x) < tol:
            return x_next, iterations
        x = x_next
    return None, iterations