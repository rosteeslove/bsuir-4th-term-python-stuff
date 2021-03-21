"""
Summary:
This module contains methods facilitating conversion between 
python integer-type variables and binary strings of some bit number.
"""

import constants
import basic_operations as basic


def int_to_binstring(n, bits=constants.DEF_BIT_NUM):
    """
    Return non-negative n as a binary string.
    """
    assert n >= 0 and n < 2**bits

    n_str = ''
    for _ in range(bits):
        n_str = str(n % 2) + n_str
        n //= 2

    return n_str


def binstring_to_int(n_str):
    """
    Return non-negative python integer whose binstring is n_str.
    """
    n = 0
    for bit in n_str:
        if bit == '1':
            n = n*2 + 1
        else:
            n = n*2

    return n


def int_to_twos_comp_binary_string(n, bits=constants.DEF_BIT_NUM):
    """
    Return 2s-complement binary string of the n-arg's value and 
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
        return basic.neg(s)[0]


def twos_comp_binary_string_to_int(s):
    """
    Return the python integer-type value of the s-arg 2s-complement
    binary string.
    """
    pos = True
    if s[0] == '1':
        pos = False
        s = basic.neg(s)[0]

    n = 0
    for bit in s:
        if bit != '0' and bit != '1':
            continue
        n = n*2 + (1 if bit == '1' else 0)

    return n if pos else -n
