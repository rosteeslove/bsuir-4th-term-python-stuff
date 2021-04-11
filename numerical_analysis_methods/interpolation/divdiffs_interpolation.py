"""
This module contains interpoly function to produce
Newton's or Hermite's interpolation polynomial for a list of
interpolation nodes.

NOTE: Hermite's interpolation algorithm is the generalized Newton's
interpolation algorithm hence the same function.
"""


import divided_differences as dd
from polynomial import Polynomial


def interpoly(nodes):
    """
    Return interpolation polynomial for a list of
    interpolation nodes.
    """
    xs, divdiffs = dd.divdiffs(nodes)

    poly_degree = len(xs) - 1

    result = Polynomial(0)
    for i in range(poly_degree + 1):
        x_product = Polynomial(1)
        for j in range(i):
            x_product *= Polynomial(1, -xs[j])

        result += x_product*divdiffs[0][i]

    return result
