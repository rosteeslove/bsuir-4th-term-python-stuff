"""
Схема частичного выбора.
"""


import numpy as np


def solve(A: np.array, b: np.array, interactive) -> np.array:
    """
    Solves A*x = b that is returns x-vector.
    """

    if interactive:
        print('Схема частичного выбора:\n')
        input()

    # securing args:
    A = A.copy()
    b = b.copy()


    # прямой ход:
    if interactive:
        print('Прямой ход:\n')
        input()

    for i in range(len(A)):

        # choosing the element with the biggest absolute value
        # in the column:
        new_i = i
        for j in range(i+1, len(A)):
            if abs(A[i, j]) > abs(A[i, new_i]):
                new_i = j

        if interactive:
            print('''Column #{0}: element {1}x{2} is of the biggest 
            absolute value.\n'''.format(i, new_i, i))
            input()

        # swapping rows:
        if i != new_i:
            A[[i, new_i]] = A[[new_i, i]]
            b[[i, new_i]] = b[[new_i, i]]

            if interactive:
                print('Rows {0} and {1} swapped.\n'.format(i, new_i))
                input()
        else:
            if interactive:
                print('No rows were swapped.\n')
                input()

        assert A[i, i] != 0

        # eliminating column elements below the current main one:
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
