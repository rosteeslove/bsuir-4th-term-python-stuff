"""
This module is to contain methods to work w/ binstrings.
"""


def is_valid(some_string: str):
    """
    Return True if the string is binary, False otherwise.
    """
    return (set(some_string) == set('01')
            or set(some_string) == set('0')
            or set(some_string) == set('1'))


def is_zero(some_string: str):
    """
    Return True if the string contains only zeros, False otherwise.
    """
    assert is_valid(some_string)

    return set(some_string) == set('0')


def _align(a: str, b: str):
    """
    Return a and b aligned in length, same by value.
    """
    assert is_valid(a) and is_valid(b)

    while len(a) != len(b):
        if len(a) < len(b):
            a = '0' + a
        else:
            b = '0' + b

    return a, b


def first_is_bigger(a: str, b: str):
    """
    Return True if a is greater than b,
    False otherwise.
    """
    assert is_valid(a) and is_valid(b)

    a, b = _align(a, b)
    for a_bit, b_bit in  zip(a, b):
        if a_bit == '1' and b_bit == '0':
            return True
        elif a_bit == '0' and b_bit == '1':
            return False

    return False
