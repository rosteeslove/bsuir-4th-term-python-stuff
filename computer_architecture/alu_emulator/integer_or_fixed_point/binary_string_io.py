"""
Summary:
This module contains methods facilitating conversion between 
python integer-type variables and binary strings of some bit number.
"""


import basic_operations as basic


def int_to_twos_comp_binary_string(n, bits = 16):
    """
    Returns 2s-complement binary string of the n-arg's value and 
    bits-arg bits.
    """

    # accounting for '-128'-like numbers:
    if n == -(2**(bits - 1)):
        return '1' + '0'*(bits - 1)

    s = ''

    # accounting for possible negative numbers:
    pos = True
    if n < 0:
        pos = False
        n *= -1

    # writing bits:
    for _ in range(bits - 1):
        bit = n % 2
        n //= 2
        s = str(bit) + s

    s = '0' + s

    # pos / neg:
    if pos:
        return s
    else:
        return basic.neg(s)


def twos_comp_binary_string_to_int(s):
    """
    Returns the python integer-type value of the s-arg 2s-complement
    binary string.
    """

    pos = True
    if s[0] == '1':
        pos = False
        s = basic.neg(s)

    n = 0
    for bit in s:
        if bit != '0' and bit != '1':
            continue
        n = n*2 + (1 if bit == '1' else 0)

    return n if pos else -n
