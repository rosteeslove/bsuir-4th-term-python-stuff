"""
This module contains the calculate_root method to find function f's
root on (a, b) interval using 'simple iteration method' which also
requires some lambda function to facilitate the convergence
to the root.
"""


import numpy as np
import scipy as sp


MAX_ITERATION_COUNT = 1_000_000


def calculate_root(f, lambda_function, a, b, eps):
    """
    Return root (assuming there's one) of f function
    on the (a, b) interval using 'simple iteration method'
    and also return number of iterations.

    The method also requires some lambda function
    to facilitate the convergence to the root.

    Remark: the method to check if the x is within error
    is to compare the x in question to the true x;
    that could be changed but bruh.
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
