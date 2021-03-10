"""
This module contains the sturms_sequence method which generates
Sturm's sequence of polynomials for a given polynomial
and the count_roots method implementing Sturm's method of calculating
the number of roots of a given polynomial on a given interval.
"""


import polynomial as poly


def sturms_sequence(p):
    """
    Returns Sturm's sequence of a given polynomial.
    """

    # setting up the Sturm's sequence.
    sturms_seq = []
    sturms_seq.append(p)
    sturms_seq.append(p.derivative())

    # filling the Sturm's sequence list.
    f = -(sturms_seq[-2] / sturms_seq[-1])[1]
    while not f.is_zero():
        sturms_seq.append(f.copy())
        f = -(sturms_seq[-2] / sturms_seq[-1])[1]

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
            nr += 1

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
