"""
This module contains the calculate_root method to approximate
polynomial's root in an interval using Newton's method.
"""


from numpy.polynomial.polynomial import Polynomial
from rootapprox import simple_iteration_method as sim


def calculate_root(f: Polynomial, a, b, eps):
    """
    Return root approximation calculated with Newton's method as well
    as number of iterations made to calculate it.

    Root of polynomial f is approximated in [a, b] interval until
    error is smaller than epsilon eps.
    """
    assert f(a)*f(b) < 0

    df = f.deriv()

    def newtons_lambda(x):
        return -1 / df(x)

    return sim.calculate_root(f, newtons_lambda, a, b, eps)
