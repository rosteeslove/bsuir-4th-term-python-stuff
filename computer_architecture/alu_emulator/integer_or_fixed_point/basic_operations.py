"""
Summary:
This module contains methods implementing basic operations for working with 
binary strings of some fixed bit size* like ALU does.

The methods are:
- sum
- invert_bits
- neg
- translate
- shift_left
- logical_shift_right
- arithmetic_shift_right

Remarks:
* the bit size is not exactly fixed but the framework is provided to work
with the binary strings keeping their length constant to emulate 
the registers.

The whole system is flexible though and can be configured 
to avoid any overflows.
"""


import itertools


def sum(a, b):
    """
    Returns sum of a and b as well as the overflow bool.
    """

    c = ''
    extra_bit = False

    for a_bit, b_bit in itertools.zip_longest(reversed(a), reversed(b)):
        if bool(b_bit == '1') != extra_bit:
            if a_bit == '0' or a_bit is None:
                c = '1' + c
                extra_bit = False
            else:
                c = '0' + c
                extra_bit = True
        else:
            c = (a_bit if a_bit is not None else '0') + c

    return c, extra_bit


def invert_bits(a):
    """
    Returns inverted a-arg binary string. 
    """

    b = ''
    for c in a:
        b += '1' if c == '0' else '0'

    return b


def neg(a, exact = False):
    """
    Returns minus a-arg interpreting it as a 2s-complement binary string.
    
    If exact-arg is True then the result is exact 
    i.e. 0b1000 would neg into 0b01000 and not 0b1000 if the string size is 4.
    """
    
    b = invert_bits(a)
    d, _ = sum(b, '01')

    if exact and a == d:
        return '0' + d
    else:
        return d


def translate(a, bits):
    """
    Returns a-arg binary string translated into the one of bits-arg bits.

    Warning: if bits-arg's value is less than a-arg's length 
    data might be lost.

    To be used mainly to align binary strings when needed.
    """

    pos = True
    if a[0] == '1':
        pos = False
        a = neg(a, True)

    if bits <= len(a):
        a = a[-bits:]
    else:
        a = '0'*(bits - len(a)) + a

    if not pos:
        a = neg(a)

    return a


def shift_left(a, shift = 1):
    """
    Returns a-arg binary string shifted left by shift-arg bits.
    """

    for _ in range(shift):
        a = a[1:] + '0'

    return a


def logical_shift_right(a, shift = 1):
    """
    Returns a-arg binary string logically shifted right by shift-arg bits.
    """

    for _ in range(shift):
        a = '0' + a[:-1]

    return a


def arithmetic_shift_right(a, shift = 1):
    """
    Returns a-arg binary string arithmetically shifted right by shift-arg bits.
    """

    for _ in range(shift):
        a = a[0] + a[:-1]

    return a
