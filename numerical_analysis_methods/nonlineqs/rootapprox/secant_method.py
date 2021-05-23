"""
This module contains the calculate_root method to find function f's
root on (a, b) interval using secant method.
"""


from numpy.polynomial.polynomial import Polynomial
import scipy.optimize as spo

MAX_ITERATION_COUNT = 1_000


def calculate_root(f: Polynomial, a, b, eps):
    """
    Return root (assuming there's one) of f function
    on the (a, b) interval using secant method
    and also return number of iterations.

    f's first two derivatives should be differentiable.
    """
    assert f(a)*f(b) < 0

    if f(a) > 0:
        f = -f

    if f(b)*f.deriv(2)(b) > 0:
        x = a
        c = b
    elif f(a)*f.deriv(2)(a) > 0:
        x = b
        c = a
    else:
        raise Exception()

    true_x = spo.brentq(f, a, b)

    iter_count = 0
    while abs(x - true_x) > eps and iter_count < MAX_ITERATION_COUNT:
        x -= (c - x) / (f(c) - f(x)) * f(x)
        iter_count += 1

    return x, iter_count
