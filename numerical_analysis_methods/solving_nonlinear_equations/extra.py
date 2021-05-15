"""
This module contains extra stuff.
"""


from numpy.polynomial.polynomial import Polynomial
from IPython.display import display, Math, HTML


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
