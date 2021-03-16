"""
Схема единственного деления.
Aka 'naive Gaussian Elimination'

This algorithm is not exactly canonical*
but a slightly modified version.

Remarks:
* - for the canonical one see *genp*_as_it_is.
"""


import numpy as np


def solve(A: np.array, b: np.array, interactive) -> np.array:
    """
    Solves A*x = b that is returns x-vector.
    """

    if interactive:
        print('Схема единственного деления:\n')
        input()

    # securing args:
    A = A.copy()
    b = b.copy()


    # прямой ход:
    if interactive:
        print('Прямой ход:\n')
        input()

    for i in range(len(A)):
        assert A[i, i] != 0

        b[i] /= A[i, i]
        A[i] /= A[i, i]

        for j in range(i+1, len(A)):
            b[j] -= b[i]*A[j, i]
            A[j] -= A[i]*A[j, i]

        if interactive:
            print('''Step {0} completed: the A-matrix and b-vector are now:
            \n{1}\n{2}\n'''.format(i+1, A, b))
            input()


    # обратный ход:
    if interactive:
        print('Обратный ход:\n')
        input()

    x = b

    for k in range(len(A)-1, -1, -1):
        for m in range(len(A)-1, k, -1):
            x[k] -= (A[k, m]*x[m]) / A[k, k]

            if interactive:
                print('x[{0}] calculated: {1}'.format(k+1, x[k]))
                input()


    return x
