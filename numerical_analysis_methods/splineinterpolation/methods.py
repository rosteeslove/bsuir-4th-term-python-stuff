"""
This module contains functions implementing spline interpolation
methods.

NOTE: all the following methods accepting nodes as an argument assume
the list of nodes is sorted.
"""

import bisect
import copy
import numpy as np
from numpy.polynomial.polynomial import Polynomial
from IPython.display import display, Math, HTML


def spline_coeffs_alpha(nodes):
    """
    Return a list of coefficients of cubic splines interpolating
    a list of nodes.

    Args:
        nodes (list of tuples): a list of interpolation nodes.

    Source: http://www.alexeypetrov.narod.ru/C/spline_about.html
    """
    xs = [node[0] for node in nodes]
    ys = [node[1] for node in nodes]
    n = len(nodes)

    # setting up some coefficients:
    hs = [0]*n
    for i in range(1, n):
        hs[i] = xs[i] - xs[i-1]

    ls = [0]*n
    for i in range(1, n):
        ls[i] = (ys[i]-ys[i-1]) / hs[i]

    deltas = [0]*n
    deltas[1] = -hs[2] / (2*(hs[1]+hs[2]))
    for i in range(3, n):
        deltas[i-1] = -hs[i] / (2*hs[i-1] + 2*hs[i] + hs[i-1]*deltas[i-2])

    lambdas = [0]*n
    lambdas[1] = 3*(ls[2] - ls[1]) / (2*(hs[1] + hs[2]))
    for i in range(3, n):
        lambdas[i-1] = ((3*ls[i] - 3*ls[i-1] - hs[i-1]*lambdas[i-2])
                        /
                        (2*hs[i-1] + 2*hs[i] + hs[i-1]*deltas[i-2]))

    # calculating bs, cs and ds:
    cs = [0]*n
    cs[n-1] = 0
    for i in range(n-1, 1, -1):
        cs[i-1] = deltas[i-1]*cs[i] + lambdas[i-1]

    bs = [0]*n
    ds = [0]*n
    for i in range(1, n):
        bs[i] = ls[i] + (2*cs[i]*hs[i] + hs[i]*cs[i-1])/3
        ds[i] = (cs[i] - cs[i-1]) / (3*hs[i])

    result = [[y, b, c, d]
              for (y, b, c, d) in zip(ys[1:], bs[1:], cs[1:], ds[1:])]

    return result


def tridiag_solve(A, b):
    """
    Return x-vector solution to a A*x = b matrix equation.

    Args:
        A (2d list): n-by-n tridiagonal matrix.
        b (list): n-by-1 vector.

    Source: https://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm
    """
    A = copy.copy(A)
    b = copy.copy(b)
    n = len(A)

    # forward sweep:
    A[0][1] /= A[0][0]
    for i in range(1, n-1):
        A[i][i+1] /= (A[i][i] - A[i][i-1]*A[i-1][i])

    b[0] /= A[0][0]
    for i in range(1, n):
        b[i] = (b[i] - A[i][i-1]*b[i-1]) / (A[i][i] - A[i][i-1]*A[i-1][i])

    # backward sweep (back substitution):
    x = np.zeros(n)
    x[-1] = b[-1]
    for i in range(n-2, -1, -1):
        x[i] = b[i] - A[i][i+1]*x[i+1]

    return x


def setup_system(as_, hs):
    """
    Return a matrix-vector system to solve with Thomas's algorithm
    to retrieve vector of 'c' coefficients.

    Args:
        as_ (list): a list of 'a' coefficients of splines.
        hs (list): a list of 'h' coefficients of splines.

    Source: https://ru.wikipedia.org/wiki/%D0%9A%D1%83%D0%B1%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D1%81%D0%BF%D0%BB%D0%B0%D0%B9%D0%BD
    """
    size = len(hs) - 2  # matrix size is num of nodes minus 2
    matrix = np.zeros((size, size))

    # setting up the vector for the system:
    vector = np.array([3*((as_[i+1]-as_[i])/hs[i+1]
                      - (as_[i]-as_[i-1])/hs[i]) for i in range(1, 1+size)])

    # setting up the first row of the matrix:
    matrix[0][0] = 2*(hs[1] + hs[2])
    matrix[0][1] = hs[2]

    # setting up the middle rows of the matrix:
    for i in range(1, size-1):
        row = matrix[i]

        row[i-1] = hs[i+1]
        row[i] = 2*(hs[i+1] + hs[i+2])
        row[i+1] = hs[i+2]

    # setting up the last row of the matrix:
    matrix[-1][-2] = hs[-2]
    matrix[-1][-1] = 2*(hs[-2] + hs[-1])

    return matrix, vector


def spline_coeffs_beta(nodes):
    """
    Return a list of coefficients of cubic splines interpolating
    a list of nodes.

    Args:
        nodes (list of tuples): a list of interpolation nodes.

    Source: https://ru.wikipedia.org/wiki/%D0%9A%D1%83%D0%B1%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D1%81%D0%BF%D0%BB%D0%B0%D0%B9%D0%BD
    """
    spline_count = len(nodes) - 1

    xs = [node[0] for node in nodes]
    ys = [node[1] for node in nodes]
    hs = [0] + [xs[i+1] - xs[i] for i in range(spline_count)]

    matrix, vector = setup_system(ys, hs)
    cs = tridiag_solve(matrix, vector).tolist()
    cs = [0] + cs + [0]  # c[0] and c[n] are zero (see source).

    bs = []
    for i in range(1, spline_count+1):
        bs.append((ys[i] - ys[i-1]) / hs[i] + hs[i]*(2*cs[i] + cs[i-1]) / 3)

    ds = []
    for i in range(1, spline_count+1):
        ds.append((cs[i] - cs[i-1]) / (3*hs[i]))

    result = [[a, b, c, d] for (a, b, c, d) in zip(ys[1:], bs, cs[1:], ds)]
    return result


def splines_alpha(nodes):
    """
    Return a list of cubic splines interpolating a list of nodes.

    Args:
        nodes (list of tuples): a list of interpolation nodes.
    """
    splines_coeffs = spline_coeffs_alpha(nodes)

    polys = [Polynomial(abcd) for abcd in splines_coeffs]

    return polys


def splines_beta(nodes):
    """
    Return a list of cubic splines interpolating a list of nodes.

    Args:
        nodes (list of tuples): a list of interpolation nodes.
    """
    splines_coeffs = spline_coeffs_beta(nodes)

    polys = [Polynomial(abcd) for abcd in splines_coeffs]

    return polys


def latex_print(poly: Polynomial):
    """
    Print a numpy's Polynomial LaTeX(ish)ly.

    Args:
        poly (Polynomial): a polynomial to be printed in LaTeX
        or whatever this is.
    """
    result = ''

    coeffs = poly.coef[::-1]
    coeffs_num = len(coeffs)
    for (p, coeff) in enumerate(coeffs):
        power = coeffs_num - 1 - p
        if coeff:
            sign = '+' if coeff > 0 else ''

            result += sign
            result += str(round(coeff, 4))

            if power:
                result += 'x'
                if power > 1:
                    result += f'^{{{power}}}'

    result = result.lstrip('+')

    display(Math(result))


def approx(nodes, spline_func):
    """Return a function approximating a given nodelist using
    a spline-producing function.

    Args:
        nodes (list of tuples): a list of interpolation nodes.
        spline_func (function): a function producing splines
        using a node list.
    """
    xs = [node[0] for node in nodes]
    polys = spline_func(nodes)

    def approximation(x):
        if x < xs[0]:
            return None

        if x > xs[-1]:
            return None

        index = bisect.bisect_left(xs, x)

        if index == 0:
            return polys[0](x - xs[1])
        else:
            return polys[index - 1](x - xs[index])

    return approximation


def approx_beta(nodes):
    """
    Return a function approximating a given node list using
    the beta-algorithm of this module.

    Args:
        nodes (list of tuples): a list of interpolation nodes.
    """
    return approx(nodes, splines_beta)


def easy_derivative(x1, y1, x2, y2, x3, y3):
    """Return easy derivative at x2.

    Easy derivative = arithmetic mean of (y2-y1) / (x2-x1)
    and (y3-y2) / (x3-x2).
    """
    d1 = (y2-y1) / (x2-x1)
    d2 = (y3-y2) / (x3-x2)

    return (d1+d2) / 2


def hermitian_coeffs(x2, y2, d2, x1, y1, d1):
    """Return a, b, c, d cubic Hermitian spline coeffs
    in [x1, x2] interval with function being y1 and y2 in
    x1 and x2 respectively and derivative being d1 and d2 in
    x1 and x2 respectively.
    """
    A = np.array([[0**3, 0**2, 0, 1],
                  [(x2-x1)**3, (x2-x1)**2, (x2-x1), 1],
                  [3*0**2, 2*0, 1, 0],
                  [3*(x2-x1)**2, 2*(x2-x1), 1, 0]])
    b = np.array([y1, y2, d1, d2])

    return np.linalg.solve(A, b)[::-1]


def hermitian_spline_coeffs(nodes):
    """Return a list of coefficients of Hermitian cubic splines
    (defect = 2) for a list of interpolation nodes.

    Args:
        nodes (list of tuples): list of interpolation nodes.
    """
    assert len(nodes) >= 3

    coeffs = []

    xs = [node[0] for node in nodes]
    ys = [node[1] for node in nodes]

    coeffs.append(hermitian_coeffs(xs[0], ys[0], 0,
                                   xs[1], ys[1], easy_derivative(
                                   xs[0], ys[0], xs[1], ys[1], xs[2], ys[2])))

    for i in range(1, len(nodes)-2):
        coeffs.append(hermitian_coeffs(
            xs[i], ys[i], easy_derivative(
                xs[i-1], ys[i-1], xs[i], ys[i], xs[i+1], ys[i+1]),
            xs[i+1], ys[i+1], easy_derivative(
                xs[i], ys[i], xs[i+1], ys[i+1], xs[i+2], ys[i+2])))

    coeffs.append(hermitian_coeffs(xs[-2], ys[-2], easy_derivative(
        xs[-3], ys[-3], xs[-2], ys[-2], xs[-1], ys[-1]),
        xs[-1], ys[-1], 0))

    return coeffs


def hermitian_splines(nodes):
    """Return a list of cubic splines of defect 2
    interpolating a list of nodes.

    Args:
        nodes (list of tuples): a list of interpolation nodes.

    Source: https://www.nbrb.by/bv/articles/10644.pdf
    """
    splines_coeffs = hermitian_spline_coeffs(nodes)

    polys = [Polynomial(abcd) for abcd in splines_coeffs]

    return polys


def hermitian_approx(nodes):
    """
    Return a function approximating a given node list using
    the hermitian cubic splines.

    Args:
        nodes (list of tuples): a list of interpolation nodes.
    """
    return approx(nodes, hermitian_splines)


def interpolation_error(true_func, nodes, approx_method, shift=0):
    """Return max error of spline interpolation of a function.

    Args:
        true_func (function): a function being interpolated.
        nodes (list of tuples): a list of interpolation nodes.
        approx_method (function): a function to produce splines
        from a list of nodes.
        shift (integer): number of nodes on the each side
        of the domain, between which the error is NOT to be calculated
        (I hope this makes sense).
    """
    assert len(nodes) > 2*shift

    approx = approx_method(nodes)

    def diff(x):
        return abs(true_func(x) - approx(x))

    a = nodes[shift][0]
    b = nodes[-(shift+1)][0]

    return max([diff(x) for x in np.linspace(a, b, 1_000)])
