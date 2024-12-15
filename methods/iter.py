def iteration_method(g, x0, tol=1e-6, max_iter=100):
    """
    Finds a root of a function using the iteration (fixed-point iteration) method.

    Args:
        g: The function to iterate with (should take a single float argument).
             This function is derived from the original function f(x) = 0 in the form x=g(x)
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
        x_next = g(x)
        iterations.append(x_next)
        if abs(x_next - x) < tol:
            return x_next, iterations
        x = x_next
    return None, iterations
