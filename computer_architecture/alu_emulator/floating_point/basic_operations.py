"""
Summary:
This module contains methods implementing basic operations
for working with binary strings (binstrings)
of some fixed bit size like ALU does.

The methods are:
- sum
- invert_bits
- neg
- expand_to_len
- shift_left
- logical_shift_right
- arithmetic_shift_right

TODO: move this module and bsio to alu_emulator directory somehow.
"""


import binary_string_io as bsio


def sum(a, b, rus_output=False):
    """
    Return sum of a and b binstrings and the overflow bool.
    """
    bigger_len = len(a) if len(a) > len(b) else len(b)
    a = expand_to_len(a, bigger_len)
    b = expand_to_len(b, bigger_len)

    if rus_output:
        print(('Считаем сумму следующих чисел в прямом коде:\n'
              '{0}(2) = {1}(10)\n'
              '{2}(2) = {3}(10)\n'
              ).format(a, bsio.binstring_to_int(a),
                       b, bsio.binstring_to_int(b)))
        print('| A | B | (e) | -> | S | (e) |\n' + '-'*34)

    c = ''
    extra_bit = False
    for a_bit, b_bit in zip(reversed(a), reversed(b)):
        old_extra_bit = extra_bit

        if bool(b_bit == '1') != extra_bit:
            if a_bit == '0':
                c = '1' + c
                extra_bit = False
            else:
                c = '0' + c
                extra_bit = True
        else:
            c = a_bit + c

        if rus_output:
            print(('| {0} | {1} | ({2}) | -> | {3} | ({4}) |'
                  ).format(a_bit, b_bit,
                           '1' if old_extra_bit else '0',
                           c[0],
                           '1' if extra_bit else '0'))

    if rus_output:
        print(('\nРезультат суммы в прямом коде:\n'
               'a + b = c\n'
               'a = {0}(2) = {1}(10)\n'
               'b = {2}(2) = {3}(10)\n'
               'c = {4}(2) = {5}(10)\n'
               'Переполнение для прямого кода '
               + ('есть' if extra_bit else 'отсутствует') + '.'
              ).format(a, bsio.binstring_to_int(a),
                       b, bsio.binstring_to_int(b),
                       c, bsio.binstring_to_int(c)))

    return c, extra_bit


def oc_sum(a, b):
    """
    Return one's complement sum of a and b.
    """
    s = sum(a, b)
    if s[1]:
        return sum(s[0], '01')[0]
    else:
        return s[0]


def oc_dif(a, b):
    """
    Return one's complement difference of a and b.
    """
    b = invert_bits(b)
    s = sum(a, b)
    if s[1]:
        return sum(s[0], '01')[0]
    else:
        return invert_bits(s[0])


def invert_bits(a):
    """
    Return inverted a-arg binary string. 
    """
    b = ''
    for c in a:
        b += '1' if c == '0' else '0'

    return b


def neg(a):
    """
    Return minus a-arg interpreting it
    as a 2s-complement binary string and return the error bool
    (True if there's an error).
    """
    b = invert_bits(a)
    d = sum(b, '01')[0]

    if a == d:
        return d, True
    else:
        return d, False
    

def expand_to_len(a, new_len):
    """
    Return a expanded to new length.
    """
    assert new_len >= len(a)

    return a[0]*(new_len-len(a)) + a


def shift_left(a, shift = 1):
    """
    Return a-arg binary string shifted left by shift-arg bits.
    """
    for _ in range(shift):
        a = a[1:] + '0'

    return a


def logical_shift_right(a, shift = 1):
    """
    Return a-arg binary string
    logically shifted right by shift-arg bits.
    """
    for _ in range(shift):
        a = '0' + a[:-1]

    return a


def arithmetic_shift_right(a, shift = 1):
    """
    Return a-arg binary string
    arithmetically shifted right by shift-arg bits.
    """

    for _ in range(shift):
        a = a[0] + a[:-1]

    return a
