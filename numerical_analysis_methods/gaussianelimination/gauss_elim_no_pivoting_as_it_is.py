"""
Схема единственного деления.
Aka 'naive Gaussian Elimination'

Remark: the module is called '*genp*_as_it_is' because it follows
the canonical algorithm of gaussian elimination with no pivoting
as opposed to slightly modified algorithm in *genp* module.
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
        assert A[i, i] != 0 and A[i, i] != 0.
        _eliminate(A, b, i)
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
            x[k] -= A[k, m]*x[m]
        x[k] /= A[k, k]

        if interactive:
            print('x[{0}] calculated: {1}'.format(k+1, x[k]))
            input()


    return x


def _eliminate(A: np.array, b: np.array, index):
    """
    Eliminates index-index element of A-matrix
    from rows below the index row.
    """

    for i in range(index+1, len(A)):
        b[i] -= b[index] * (A[i, index]/A[index, index])
        A[i] -= A[index] * (A[i, index]/A[index, index])
