import random

import numpy as np


MAX_ABS_VAL = 100
DEFAULT_SPARSITY_COEFFICIENT = 0.9

random.seed(42)


# example 1:
k = 14
C = np.array([[0.01, 0., -0.02, 0., 0.],
              [0.01, 0.01, -0.02, 0., 0.],
              [0., 0.01, 0.01, 0., -0.02],
              [0., 0., 0.01, 0.01, 0.],
              [0., 0., 0., 0.01, 0.01]])
D = np.array([[1.33, 0.21, 0.17, 0.12, -0.13],
              [-0.13, -1.33, 0.11, 0.17, 0.12],
              [0.12, -0.13, -1.33, 0.11, 0.17],
              [0.17, 0.12, -0.13, -1.33, 0.11],
              [0.11, 0.67, 0.12, -0.13, -1.33]])

b = np.array([1.2, 2.2, 4.0, 0.0, -1.2])
A = k*C + D


# example 2 (strictly diagonally dominant matrix):
E = np.array([[15.,    0.6,   -10.],
              [-9,     128.,   42.],
              [0.888,  0.01,   505.]])

e = np.array([64., 13., 3.])


# example 3 (unsolvable):
F = np.array([[0., 0., -0.],
              [68., 43., 45.],
              [0., 0.784, 101.66]])

f = np.array([10., 839., 404.0])


# example 4 (no convergence):
G = np.array([[40.33874062, 75.88713314, 63.44086045],
              [60.47679707, 93.38465001, 18.31687119],
              [96.01020406, 75.5593533,  79.24759332]])

g = np.array([94.70078561, 16.95188974, 67.37242174])


# example 5 (convergence not guaranteed
# but occurs in simple iteration method):
H = np.array([[ 62.47231779, -25.47252759,  -3.95942641],
              [ 70.68295302,  31.3283195,    3.42379872],
              [-42.14711076, -49.22973004,  63.57119008]])

h = np.array([47.92749791, -11.23318861, -78.26542853])


# example 6 (convergence not guaranteed but occurs in Seidel method):
K = np.array([[-39.03990499,  12.13030569,  31.852455  ],
              [-68.77717219, -28.49888675,  10.33679812],
              [  6.73733667,  43.41802009,  45.69676219]])

k = np.array([-95.28111069, 80.71488567,  97.72330938])


# example 7 (convergence not guaranteed but occurs in both methods)
M = np.array([[ 75.36229012,  50.63735751,  63.1825777 ],
              [ -9.13676363,  36.82750536, -56.9036931 ],
              [-22.08539748,  -6.98078997, -92.94923527]])

m = np.array([5.9346564,   66.11055296, -79.31284799])


def random_sparse_matrix(size):
    """
    Generate random sparse matrix which is supposed to be used as the
    A-matrix for the 'A*x = b' system of linear equations.

    The score* (or sparsity) of the matrix is roughly equal
    to DEFAULT_SPARSITY_COEFFICIENT defined in this module.

    Remarks: the matrix should meet this package's base_method's
    convergence criteria i.e. the check_convergence method should
    return True.
    *https://machinelearningmastery.com/sparse-matrices-for-machine-learning/#:~:text=A%20matrix%20is%20sparse%20if,Matrices%2C%20Second%20Edition%2C%202017.
    """
    assert (1 - DEFAULT_SPARSITY_COEFFICIENT) * size**2 > size

    res = np.zeros((size, size))
    desired_nonzero_elements_count = ((1 - DEFAULT_SPARSITY_COEFFICIENT)
                                      * (size**2))

    for i in range(size):
        res[i, i] = (MAX_ABS_VAL
                     * random.uniform(0.5, 1.)
                     * (1 if random.random() < 0.5 else -1))

    desired_nonzero_elements_count -= size

    res_zeros = []
    for i in range(len(res)):
        for j in range(len(res)):
            if i != j:
                res_zeros.append((i, j))

    while desired_nonzero_elements_count > 0:
        index = random.randint(0, len(res_zeros)-1)
        i, j = res_zeros[index]
        res_zeros.pop(index)

        res[i, j] = (MAX_ABS_VAL
                     * random.uniform(0., 0.5/size)
                     * (1 if random.random() < 0.5 else -1))
        desired_nonzero_elements_count -= 1

    return res

