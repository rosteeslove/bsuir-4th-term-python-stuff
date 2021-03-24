"""
This module contains the calculate_root method to find function f's
root on (a, b) interval using secant method.
"""


import numpy as np


MAX_ITERATION_COUNT = 1_000_000


def calculate_root(f, a, b, eps):
    """
    Return root (assuming there's one) of f function
    on the (a, b) interval using secant method
    and also return number of iterations.

    f's first two derivatives should be differentiable.
    """
    assert f(a)*f(b) < 0

    if f(a) > 0:
        f = -f

    while True:
        a += (b - a) / (f(b) - f(a)) * abs(f(a))
        if abs(f(a)) < eps:
            break

    return l
