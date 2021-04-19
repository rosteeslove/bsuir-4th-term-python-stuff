"""
This module contains functions implementing spline interpolation
methods.
"""

import numpy as np
from numpy.polynomial.polynomial import Polynomial
from IPython.display import display, Math, HTML


def interpolate(nodes):
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


def splines(nodes):
    """
    Return a list of cubic splines interpolating a list of nodes.

    Args:
        nodes (list of tuples): a list of interpolation nodes.
    """
    splines_coeffs = interpolate(nodes)

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
