"""
This module contains 'solve' method implementing an iterative method
of solving systems of linear equations known as Seidel or
Gauss-Seidel method.

The science behind all that follows is to be found here:
https://math.semestr.ru/optim/zeidel.php
"""


import numpy as np

import base_method as bm


def _iteration(B: np.array, x: np.array, c: np.array):
    """
    Completes one iteration of the method.
    """
    y = x.copy()

    for i in range(len(B)):
        y[i] = c[i]
        for j in range(len(B)):
            y[i] += B[i, j]*y[j]

    return y


def solve(A: np.array, b: np.array, precision):
    """
    Returns the x-vector solution to the A*x=b equation with error
    within the precision argument value.  Uses Gauss-Seidel method.
    """
    return bm.solve(A, b, precision, _iteration)