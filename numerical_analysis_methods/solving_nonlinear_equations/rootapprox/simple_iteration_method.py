"""
This module contains the calculate_root method to approximate
polynomial's root in an interval using simple iteration method.
"""


import numpy as np
import scipy as sp


MAX_ITERATION_COUNT = 1_000_000


def calculate_root(f, lambda_function, a, b, eps):
    """
    Return root approximation calculated with simple iteration method
    as well as number of iterations made to calculate it.

    Root of polynomial f is approximated in [a, b] interval until
    error is smaller than epsilon eps using lambda function to
    facilitate convergence.
    """
    assert f(a)*f(b) < 0

    def phi_function(some_x):
        return some_x + lambda_function(some_x)*f(some_x)

    x = a
    true_x = sp.optimize.brentq(f, a, b)

    iter_count = 0
    while iter_count < MAX_ITERATION_COUNT:
        x = phi_function(x)

        if abs(x - true_x) < eps:
            break

        iter_count += 1

    return x, iter_count
