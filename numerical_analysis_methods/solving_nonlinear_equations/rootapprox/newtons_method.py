"""
This module contains the calculate_root method to approximate
polynomial's root in an interval using Newton's method.
"""


from rootapprox import simple_iteration_method as sim


def calculate_root(f, a, b, eps):
    """
    Return root approximation calculated with Newton's method as well
    as number of iterations made to calculate it.

    Root of polynomial f is approximated in [a, b] interval until
    error is smaller than epsilon eps.
    """
    assert f(a)*f(b) < 0

    def f_derivative(x):
        return f.derivative(x)

    return sim.calculate_root(f, 1/f_derivative, a, b, eps)
