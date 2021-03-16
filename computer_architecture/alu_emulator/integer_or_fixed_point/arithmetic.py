"""
Summary:
This module contains methods facilitating subtraction, multiplication and
division for 2s-complement binary strings.
"""


import basic_operations as basic


def _align(a, b):
    """
    Returns a tuple of a-arg and b-arg binary strings but
    changed so that their size equals to the size of the bigger one.

    To be used for some operations.
    """

    if len(a) < len(b):
        a = basic.translate(a, len(b))
    elif len(a) > len(b):
        b = basic.translate(b, len(a))

    return a, b


def dif(a, b):
    """
    Returns the difference between a-arg and b-arg 2s-complement 
    binary strings as well as the overflow bool.
    """

    a, b = _align(a, b)

    b = basic.neg(b)

    return basic.sum(a, b)


def mul(a, b):
    """
    Returns the unsigned product of a-arg and b-arg unsigned 
    binary strings as well as the overflow bool.

    Remark: the product is of the same bit number as the bigger argument 
    so this method is to be used with small numbers to avoid overflows.
    """

    p = '0'
    overflow = False
    a, b = _align(a, b)

    for bit in reversed(a):
        if bit == '1':
            p, ov = basic.sum(p, b)
            overflow = overflow or ov
        b = basic.shift_left(b)

    return p


def full_mul(a, b):
    """
    Returns the unsigned product of a-arg and b-arg unsigned 
    binary strings.
    """

    p = '0'

    for bit in reversed(a):
        if bit == '1':
            p = basic.sum(p, b)
        b += '0'

    return p


def imul(m, r):
    """
    Returns the product of m-arg and r-arg interpreting them as 2s-complement 
    binary strings.

    Remark: the Booth's algorithm is used 
    (https://en.wikipedia.org/wiki/Booth%27s_multiplication_algorithm).
    """

    if m == basic.neg(m):
        tmp = m
        m = r
        r = tmp

    x = len(m)
    y = len(r)

    A = m + (y+1)*'0'
    S = basic.neg(m) + (y+1)*'0'
    P = x*'0' + r + '0'

    for _ in range(y):
        two_last_bits_of_p = P[-2:]

        if two_last_bits_of_p == '01':
            P = basic.sum(A, P)
        elif two_last_bits_of_p == '10':
            P = basic.sum(S, P)

        P = basic.arithmetic_shift_right(P)

    return P[:-1]


def idiv(a, b):
    """
    Returns tuple of quotient and remainder of a-arg / b-arg.

    Remark: a-arg and b-arg are 2s-complement binary strings.
    """

    a, b = _align(a, b)
    M = b
    AQ = basic.translate(a, len(a)*2)
    A, Q = AQ[:len(a)], AQ[-len(a):]

    for _ in range(len(a)):
        AQ = basic.shift_left(A + Q)
        A, Q = AQ[:len(a)], AQ[-len(a):]

        old_A = A
        if M[0] == A[0]:
            A = dif(A, M)
        else:
            A = basic.sum(A, M)

        if old_A[0] == A[0] or A == Q == basic.translate('0', len(A)):
            Q = Q[:-1] + '1'
        else:
            Q = Q[:-1] + '0'
            A = old_A

    r = A
    q = Q if a[0] == b[0] else basic.neg(Q)

    return q, r
