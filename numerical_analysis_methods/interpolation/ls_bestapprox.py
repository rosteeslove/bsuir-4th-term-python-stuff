"""
This module facilitates calculation of best approximation polynomials.
The method is least squares.
"""


import numpy as np

from polynomial import Polynomial


def bestapprox_alpha(nodes, m):
    """
    Return a polynomial of degree m which is the best
    approximation polynomial for a list of interpolation nodes.

    The algorithm from BSUIR documentation.
    """
    n = len(nodes) - 1
    assert m <= n

    xs = [node[0] for node in nodes]
    ys = [node[1] for node in nodes]

    # setting up b-vector:
    b = []
    for i in range(m+1):
        s = 0
        for j in range(n+1):
            s += (ys[j] * (xs[j]**(m-i)))

        b.append(s)

    # setting up A-matrix:
    A = []
    for i in range(m+1):
        a = []
        for j in range(m+1):
            s = 0
            for k in range(n+1):
                s += xs[k]**(2*m-i-j)
            a.append(s)
        A.append(a)

    # calculating the answer:
    result = np.linalg.solve(A, b)

    return Polynomial(*result.tolist())


def bestapprox_beta(nodes, m):
    """
    Return a polynomial of degree m which is the best
    approximation polynomial for a list of interpolation nodes.

    The algorithm from:
    https://textbooks.math.gatech.edu/ila/least-squares.html.
    """
    n = len(nodes) - 1
    assert m <= n

    xs = [node[0] for node in nodes]
    ys = [node[1] for node in nodes]

    # setting up b-vector:
    b = np.array(ys)

    # setting up A-matrix:
    A = []
    for x in xs:
        a = []
        for power in range(m, -1, -1):
            a.append(x**power)
        A.append(a)

    A = np.array(A)

    # calculating the result:
    AT = A.T

    ATA = AT @ A
    ATb = AT @ b

    result = np.linalg.solve(ATA, ATb)
    
    return Polynomial(*result.tolist())
