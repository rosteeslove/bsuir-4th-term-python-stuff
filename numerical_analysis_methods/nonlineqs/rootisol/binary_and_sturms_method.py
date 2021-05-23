"""
This module contains the isolate_roots method for polynomials only.
"""


from rootisol import sturms_method as sm


MIN_RADIUS = 0.001


def _iteration(sturms_seq, left, right, eps):
    """
    Returns the list of root intervals of some polynomial with
    sturms_seq Sturm's sequence in the [left, right] interval.

    eps sets precision.

    Works recursively.
    """
    if sm.count_roots(sturms_seq, left, right) == 0:
        return []
    elif right - left <= eps:
        return [(left, right)]
    else:
        return (_iteration(sturms_seq, left, (left+right) / 2, eps)
                + _iteration(sturms_seq, (left+right) / 2, right, eps))


def isolate_roots(p, left, right, eps=MIN_RADIUS):
    """
    Returns the list of root intervals of p polynomial
    in [left, right] interval using a combination of
    binary search algorithm and Sturm's method.

    eps sets precision.
    """
    sturms_seq = sm.sturms_sequence(p)

    return _iteration(sturms_seq, left, right, eps)
