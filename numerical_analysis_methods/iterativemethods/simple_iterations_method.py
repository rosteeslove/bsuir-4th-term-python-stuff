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
    # The following line of code is removed to match the optimization
    # level of Seidel method.  In other words this line is too fast
    # but the desired outcome is to have sim iteration and Seidel
    # iteration run in roughly the same time.

    # return B @ x + c

    new_x = c.copy()

    for i in range(len(B)):
        for j in range(len(B)):
            new_x[i] += B[i, j]*x[j]

    return new_x


def solve(A, b, precision):
    """
    Returns the x-vector solution to the A*x=b equation with error
    within the precision argument value.  Uses so called
    'simple iterations method'.
    """
    return bm.solve(A, b, precision, _iteration)
        