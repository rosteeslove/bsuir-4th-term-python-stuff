"""
This module contains 'solve' method implementing an iterative method
of solving systems of linear equations known as 'метод простых
итераций' - basically 'simple iterations method'.

The science behind all that follows is to be found here:
https://math.semestr.ru/optim/iter.php
"""


import numpy as np

import base_method as bm


def _iteration(B: np.array, x: np.array, c: np.array):
    """
    Completes one iteration of the method.
    """
    return B @ x + c


def solve(A, b, precision):
    """
    Returns the x-vector solution to the A*x=b equation with error
    within the precision argument value.  Uses so called
    'simple iterations method'.
    """
    return bm.solve(A, b, precision, _iteration)
        