"""
Схема полного выбора.
"""


import numpy as np


def solve(A: np.array, b: np.array, interactive) -> np.array:
    """
    Solves A*x = b that is returns x-vector.
    """

    if interactive:
        print('Схема полного выбора:\n')
        input()

    # securing args:
    A = A.copy()
    b = b.copy()

    # this matrix is to restore order of values in x-vector
    # after the main algorithm:
    root_shifts = np.identity(len(A))


    # прямой ход:
    if interactive:
        print('Прямой ход:\n')
        input()

    for i in range(len(A)):

        # finding the element of the biggest absolute value
        # in the unprocessed submatrix of A:
        the_i, the_j = _abs_max(A, i)
        if interactive:
            print('''Element {0}x{1} is of the biggest absolute value 
            in the unproccessed part of A-matrix.\n'''.format(the_i, the_j))
            input()

        # swapping rows if needed:
        if i != the_i:
            A[[the_i, i]] = A[[i, the_i]]
            b[[the_i, i]] = b[[i, the_i]]

            if interactive:
                print('Rows {0} and {1} swapped.\n'.format(i, the_i))
                input()
        else:
            if interactive:
                print('No rows were swapped.\n')
                input()

        # swapping columns if needed:
        if i != the_j:
            A[:,[the_j, i]] = A[:,[i, the_j]]
            root_shifts[:, [the_j, i]] = root_shifts[:, [i, the_j]]

            if interactive:
                print('Columns {0} and {1} swapped.\n'.format(i, the_j))
                input()
        else:
            if interactive:
                print('No columns were swapped.\n')
                input()

        assert A[i, i] != 0

        _eliminate(A, b, i)
        if interactive:
            print('''Step {0} completed: the A-matrix and b-vector 
            are now:\n{1}\n{2}\n'''.format(i+1, A, b))
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


    # displaying the x-vector with swapped values:
    if interactive:
        print('''Current x-vector is {0} 
        but some values are swapped.'''.format(x))
        input()


    return root_shifts @ x


def _abs_max(A: np.array, index):
    """
    Returns the A-matrix coordinates of an element with the biggest
    absolute value in the submatrix of A whose 0-0 element is A's
    index-index element.
    """
    the_i, the_j = index, index

    for i in range(index, len(A)):
        for j in range(index, len(A)):
            if abs(A[i, j]) > abs(A[the_i, the_j]):
                the_i = i
                the_j = j

    return the_i, the_j


def _abs_max_fast(A: np.array, index):
    """
    Return the A-matrix coordinates of an element with the biggest
    absolute value in the submatrix of A whose 0-0 element is A's
    index-index element.

    Remark: optimized _abs_max.

    TODO: refine
    """

    maxind = numpy.argmax(abs(A[index:, index:]))
    return (index + maxind // (len(A) - index), index + maxind % (len(A) - index))


def _eliminate(A: np.array, b: np.array, index):
    """
    Eliminates index-index element of A-matrix
    from rows below the index row.
    """
    
    for i in range(index+1, len(A)):
        b[i] -= b[index] * (A[i, index]/A[index, index])
        A[i] -= A[index] * (A[i, index]/A[index, index])
