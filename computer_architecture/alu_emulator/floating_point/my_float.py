"""
This module contains the Float class
which is to be like IEEE 754 float.

TYPES:

16 bit (half precision):
    s - sign (1 bit)
    e - exponent (5 bits)
    m - mantissa (10 bits)

    s eeeee mmmmmmmmmm

32 bit (single precision):
    s - sign (1 bit)
    e - exponent (8 bits)
    m - mantissa (23 bits)

    s eeeeeeee mmmmmmmmmmmmmmmmmmmmmmm

The type to be implemented is the 32 bit one.

METHODS TO IMPLEMENT:

 PROPERTIES(?):
 + exponent (get the exponent 8-bit binstring)
 + mantissa_binary (get the mantissa 23-bit binstring)
 + mantissa (get the true mantissa 24-bit binstring)
 - (sign could be retrieved using number[0])

 IO BETWEEN MY TYPE AND THE ORIGINAL TYPE::
 + np.float32 -> my Float
 + my Float -> np.float32

 IS_*WHATEVER* BOOL METHODS:
 + is_zero
 + is_infinity
 + is_nan
 + is_normal

 COMPARISON OPERATORS:
 + ==
 + !=
 + >
 + >=
 + <
 + <=

 ARITHMETIC OPERATORS:
 + addition
 + subtraction
 + multiplication
 + division


SOME NOTES:

 Comparing NaNs in any way should yield a false value.
 Arithmetic operations with NaNs are to return a NaN.
 Infinities are compared as normal numbers.
 Arithmetic operations with infinities are to be considered
     special cases.
"""


from copy import deepcopy
import numpy as np
import struct

import binstrings
import basic_operations as basic


TOTAL_BIT_COUNT = 32
MANTISSA_BIT_COUNT = 23
EXPONENT_BIT_COUNT = 8


class Float:

    @staticmethod
    def float_to_bin(num):
        """
        Return the IEEE 754 binary string representation
        of the num float.
        """
        return (''.join(bin(c).replace('0b', '').rjust(8, '0')
                for c in struct.pack('!f', num)))

    @staticmethod
    def bin_to_float(b: str):
        """
        Return the float of b IEEE 754 representation.
        """
        f = int(b, 2)
        return np.float32(struct.unpack('f', struct.pack('I', f))[0])

    def __init__(self, num: float):
        self.binary = self.float_to_bin(num)

    @property
    def exponent(self):
        """
        Return binstring of the number's exponent.
        """
        return self.binary[1:(1+EXPONENT_BIT_COUNT)]

    @exponent.setter
    def exponent(self, value: str):
        """
        Set the number's exponent binstring.
        """
        assert binstrings.is_valid(value) and len(value) == EXPONENT_BIT_COUNT

        self.binary = self.binary[0] + value + self.mantissa_binary

    @property
    def mantissa_binary(self):
        """
        Return binstring of the number's mantissa.
        """
        return self.binary[(1+EXPONENT_BIT_COUNT):]

    @mantissa_binary.setter
    def mantissa_binary(self, value: str):
        """
        Set the number's mantissa binstring.
        """
        assert binstrings.is_valid(value) and len(value) == MANTISSA_BIT_COUNT

        self.binary = self.binary[0] + self.exponent + value

    @property
    def mantissa(self):
        """
        Return binstring of the number's mantissa including
        the implicit bit in the beginning.
        """
        return ('0' if self.is_denormal() else '1') + self.mantissa_binary

    def is_zero(self):
        """
        Return True if the number is zero, False otherwise.
        """
        return set(self.binary[1:]) == set('0')

    def is_infinity(self):
        """
        Return True if the number is infinity, False otherwise.
        """
        return (set(self.exponent) == set('1')
                and set(self.mantissa_binary) == set('0'))

    def is_nan(self):
        """
        Return True if the number is NaN, False otherwise.
        """
        return (set(self.exponent) == set('1')
                and set(self.mantissa_binary) == set('01'))

    def is_normal(self):
        """
        Return True if the number is normal, False otherwise.
        """
        return (set(self.exponent) == set('01')
                and set(self.mantissa_binary) == set('01'))

    def is_denormal(self):
        """
        Return True if the number is denormal (or subnormal),
        False otherwise.
        """
        return (set(self.exponent) == set('0')
                and set(self.mantissa_binary) == set('0', '1'))

    def __eq__(self, other):
        """
        Return True if numbers are equal, False otherwise.

        Remark: 0 and -0 to be considered equal.

        (to be tested)
        """
        if (self.is_normal() or other.is_normal()
                or self.is_denormal() or other.is_denormal()):
            return self.binary == other.binary

        if self.is_zero() and other.is_zero():
            return True

        if self.is_infinity() and other.is_infinity():
            return self.binary[0] == other.binary[0]

        return False

    def __ne__(self, other):
        """
        Return True if numbers are not equal, False otherwise.
        """
        return not (self == other)

    def __gt__(self, other):
        """
        Return True if self is greater than other, False otherwise.

        (to be tested #1)
        """
        # compare by signs:
        if self.binary[0] != other.binary[0]:
            return self.binary[0] == '0'

        # compare by value for positives:
        if self.binary[0] == '0':
            return binstrings.first_is_bigger(self.binary[1:],
                                              other.binary[1:])

        # compare by value for negatives:
        return binstrings.first_is_bigger(other.binary[1:],
                                          self.binary[1:])
        
    def __ge__(self, other):
        """
        Return True if self >= other, False otherwise.
        """
        return self > other or self == other

    def __lt__(self, other):
        """
        Return True if self < other, False otherwise.
        """
        return not self >= other

    def __le__(self, other):
        """
        Return True if self <= other, False otherwise.
        """
        return not self > other

    def __neg__(self):
        """
        Return number with the opposite sign.

        (not tested but I'm pretty sure this works)
        """
        bin_list = list(self.binary)
        bin_list[0] = '0' if bin_list[0] == '1' else '1'
        self.binary = ''.join(bin_list)

    def __add__(self, other):
        """
        Return sum of two Floats.

        (a draft; not tested)
        """
        self = deepcopy(self)
        other = deepcopy(other)
        # now self and other can be modified.

        if self.is_zero():
            return other
        elif other.is_zero():
            return self

        bigger, smaller = (self, other) if (self >= other) else (other, self)

        # aligning the exponents
        while binstrings.first_is_bigger(bigger.exponent, smaller.exponent):
            # incrementing exponent of the smaller number and shifting
            # its mantissa to the right.
            smaller.exponent = basic.sum(smaller.exponent, '01')[0]
            smaller.mantissa_binary = basic.logical_shift_right(
                smaller.mantissa_binary)

            # if mantissa of the smaller one goes zero, return
            # the bigger operand.
            if binstrings.is_zero(smaller.mantissa_binary):
                return bigger

        # summing mantissas (assuming we are summing 23-bit mantissas)
        # TODO: don't assume
        mantissa_one = (bigger.mantissa_binary if bigger.binary[0] == '0'
                        else basic.invert_bits(bigger.mantissa_binary))
        mantissa_two = (smaller.mantissa_binary if smaller.binary[0] == '0'
                        else basic.invert_bits(smaller.mantissa_binary))

        sum_sign = bigger.binary[0]
        sum_exponent = bigger.exponent
        sum_mantissa = basic.sum(mantissa_one, mantissa_two)

        # if mantissas' sum goes zero we are to return zero.
        if binstrings.is_zero(sum_mantissa[0]):
            # create zero Float and return it
            # TODO: create zero the normal way
            zero = deepcopy(bigger)
            zero.binary = '0'*TOTAL_BIT_COUNT
            return zero

        # if mantissas' sum isn't zero but the mantissa_sum binstring
        # is overflowed ...
        if sum_mantissa[1]:
            mantissa_two = basic.logical_shift_right(mantissa_two)
            sum_mantissa = basic.sum(mantissa_one, mantissa_two)
            sum_exponent = basic.sum(sum_exponent, '01')

            # check if exponent is overflowed
            if sum_exponent[1]:
                raise Exception # TODO: actually return infinity

        sum_mantissa = sum_mantissa[0]
        sum_exponent = sum_exponent[0]

        bigger.binary = sum_sign + sum_exponent + sum_mantissa
        return bigger

    def __sub__(self, other):
        """
        Return sum of two Floats.

        (a draft; not tested)
        """
        return self + (-other)


    