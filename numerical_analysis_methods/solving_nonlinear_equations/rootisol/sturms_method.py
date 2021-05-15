"""
This module contains the sturms_sequence method which generates
Sturm's sequence of polynomials for a given polynomial
and the count_roots method implementing Sturm's method of calculating
the number of roots of a given polynomial on a given interval.
"""

from numpy.polynomial import polynomial as poly
from numpy.polynomial.polynomial import Polynomial


def sturms_sequence(p: Polynomial):
    """
    Returns Sturm's sequence of a given polynomial.
    """
    # setting up the Sturm's sequence.
    sturms_seq = []
    sturms_seq.append(p)
    sturms_seq.append(p.deriv())

    # filling the Sturm's sequence list.
    f = -Polynomial(poly.polydiv(sturms_seq[-2].coef, sturms_seq[-1].coef)[1])
    while f.degree() != 0 or f.coef[0] != 0:
        sturms_seq.append(f.copy())
        f = -Polynomial(poly.polydiv(
            sturms_seq[-2].coef, sturms_seq[-1].coef)[1])

    return sturms_seq


def _evaluate_sturms_seq_at_x(seq, x):
    """
    Returns list of seq argument polynomials' values at x.
    """
    return [v(x) for v in seq]


def _num_of_sign_changes(seq):
    """
    Returns the number of sign changes in the seq list of numbers.
    """
    num = 0
    for i in range(len(seq)-1):
        if seq[i]*seq[i+1] < 0:
            num += 1

    return num


def count_roots(sturms_seq, left, right):
    """
    Returns the number of roots of the some polynomial on the
    [left, right] interval using the Sturm's polynomial sequence.
    """

    # evaluating the Sturm's sequence at the interval borders.
    sturms_seq_at_l = _evaluate_sturms_seq_at_x(sturms_seq, left)
    sturms_seq_at_r = _evaluate_sturms_seq_at_x(sturms_seq, right)

    # finding out the number of sign changes in both lists.
    nl = _num_of_sign_changes(sturms_seq_at_l)
    nr = _num_of_sign_changes(sturms_seq_at_r)

    # returning the difference between the former and the latter.
    return nl - nr
