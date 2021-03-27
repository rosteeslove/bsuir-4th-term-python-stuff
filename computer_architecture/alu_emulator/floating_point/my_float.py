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

THINGS TO IMPLEMENT:

 PROPERTIES:
 + exponent (get&set the exponent 8-bit binstring)
 + mantissa_binary (get&set the mantissa 23-bit binstring)
 + mantissa (get the true mantissa 24-bit binstring)
 + sign_bit (get&set)

 IO BETWEEN MY TYPE AND THE ORIGINAL TYPE:
 + np.float32 -> my Float
 + my Float -> np.float32

 IS_*WHATEVER* BOOL METHODS:
 + is_zero
 + is_infinity
 + is_nan
 + is_normal
 + is_denormal

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
import arithmetic as arth


TOTAL_BIT_COUNT = 32
MANTISSA_BIT_COUNT = 23
EXPONENT_BIT_COUNT = 8


class Float:

    # io methods for this type <-> np.float32 conversion:

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

    @staticmethod
    def pos_infinity():
        """
        Return positive infinity instance of the Float type.
        """
        return Float(float('inf'))

    @staticmethod
    def neg_infinity():
        """
        Return negative infinity instance of the Float type.
        """
        return Float(float('-inf'))

    @staticmethod
    def nan():
        """
        Return NaN instance of Float type.
        """
        return Float(float('nan'))

    # standart methods for classes:

    def __init__(self, num: float):
        self.binary = self.float_to_bin(num)

    def __str__(self):
        """
        Return classical decimal string representation of float.
        """
        return str(self.bin_to_float(self.binary))

    # properties:

    @property
    def sign_bit(self):
        """
        Return '0' if the number is positive, '1' otherwise.
        """
        return self.binary[0]

    @sign_bit.setter
    def sign_bit(self, value: str):
        """
        Set the number's sign bit.
        """
        assert binstrings.is_valid(value) and len(value) == 1

        self.binary = value + self.binary[1:]

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

        self.binary = self.sign_bit + value + self.mantissa_binary

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

        self.binary = self.sign_bit + self.exponent + value

    @property
    def mantissa(self):
        """
        Return binstring of the number's mantissa including
        the implicit bit in the beginning.
        """
        return ('0' if self.is_denormal() else '1') + self.mantissa_binary

    # is_*whatever* methods:

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
                and set(self.mantissa_binary) == set('01'))

    # comparison operators:

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
            return self.sign_bit == other.sign_bit

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
        if self.is_nan() or other.is_nan():
            return False

        if self.is_zero() and other.is_zero():
            return False
            
        # compare by signs:
        if self.sign_bit != other.sign_bit:
            return self.sign_bit == '0'

        # compare by value for positives/ negatives:
        if self.sign_bit == '0':
            return binstrings.first_is_bigger(self.abs().binary,
                                              other.abs().binary)
        else:
            return binstrings.first_is_bigger(other.abs().binary,
                                              self.abs().binary)
        
    def __ge__(self, other):
        """
        Return True if self >= other, False otherwise.
        """
        return self > other or self == other

    def __lt__(self, other):
        """
        Return True if self < other, False otherwise.
        """
        if self.is_nan() or other.is_nan():
            return False

        return not (self >= other)

    def __le__(self, other):
        """
        Return True if self <= other, False otherwise.
        """
        if self.is_nan() or other.is_nan():
            return False
            
        return not (self > other)

    # unary arithmetic operators:

    def __neg__(self):
        """
        Return number with the opposite sign.
        """
        negged = deepcopy(self)
        negged.sign_bit = '1' if (negged.sign_bit == '0') else '0'
        return negged

    def abs(self):
        """
        Return the absolute value of the number.
        """
        abs_val = deepcopy(self)
        abs_val.sign_bit = '0'
        return abs_val

    # binary arithmetic operators:

    def __add__(self, other):
        """
        Return sum of two Floats.

        (works for random big and small pos and neg floats;
         to be tested w/ special cases;
         1 bit error sometimes - dunno why)
        """
        # step 1 (account for special cases):

        # a. NaNs:
        if self.is_nan() or other.is_nan():
            return Float(float('nan'))

        # b. two infinities:
        if self.is_infinity() and other.is_infinity():
            if self.sign_bit != other.sign_bit:
                return self.nan
            else:
                return deepcopy(self)
        
        # c. one infinity:
        if self.is_infinity():
            return deepcopy(self)
        elif other.is_infinity():
            return deepcopy(other)

        # d. one or two zeros:
        if self.is_zero():
            return deepcopy(other)
        elif other.is_zero():
            return deepcopy(self)

        # at this point any of the two arguments is
        # either normal or denormal
        # step 2: deconstructing arguments' binaries:

        bigger, smaller = (self, other) if (self.abs() >= other.abs()) else (other, self)

        biggers_sign = bigger.sign_bit
        smallers_sign = smaller.sign_bit

        biggers_exponent = bigger.exponent
        smallers_exponent = smaller.exponent
        
        biggers_mantissa = bigger.mantissa
        smallers_mantissa = smaller.mantissa

        # step 3: aligning the exponents:

        while biggers_exponent != smallers_exponent:
            # incrementing exponent of the smaller number and shifting
            # its mantissa to the right.
            smallers_exponent = basic.sum(smallers_exponent, '01')[0]
            smallers_mantissa = basic.logical_shift_right(
                                    smallers_mantissa)

            # if mantissa of the smaller one goes zero, return
            # the bigger operand copy.
            if binstrings.is_zero(smallers_mantissa):
                return deepcopy(bigger)

        # step 4: getting mantissas' sum and setting up
        # sum's sign, exponent and mantissa:

        sum_sign = biggers_sign
        sum_exponent = biggers_exponent
        sum_mantissa = (basic.sum(biggers_mantissa, smallers_mantissa)
                        if biggers_sign == smallers_sign
                        else basic.oc_sum(biggers_mantissa,
                                basic.invert_bits(smallers_mantissa)))

        # shifting mantissa to fit if neccesary:
        if type(sum_mantissa) is tuple:
            if sum_mantissa[1]:
                sum_mantissa = '1' + sum_mantissa[0][:-1]
                sum_exponent = basic.sum(sum_exponent, '01')[0]

                # if exponent overflows, return infinity:
                if sum_exponent == '1'*EXPONENT_BIT_COUNT:
                    return (Float(float('inf'))
                            if sum_sign == '0'
                            else Float(float('-inf')))
            else:
                sum_mantissa = sum_mantissa[0]

        # in case sum's mantissa is zero return zero Float.
        if (binstrings.is_zero(sum_mantissa)):
            return Float(0.)

        # step 5: normalize the number if possible.
        while sum_mantissa[0] == '0':
            sum_mantissa = basic.shift_left(sum_mantissa)
            # decrementing exponent:
            sum_exponent = basic.sum(sum_exponent, '11')[0]

            if sum_exponent == '0'*EXPONENT_BIT_COUNT:
                break

        # TODO: do this the normal way.
        sum_binary = sum_sign + sum_exponent + sum_mantissa[1:]
        sum_float = deepcopy(self)
        sum_float.binary = sum_binary
        return sum_float

    def __sub__(self, other):
        """
        Return difference of two Floats.
        """
        return self + (-other)

    def __mul__(self, other):
        """
        Return product of two Floats.

        (a draft; seems to be working with 1 bit error)
        """

        # step 1: account for special cases.
        # i.e. nans present -> nan
        #      zeros present -> zeros
        #      infs present -> signed inf
        #
        #     but also (this overrides what's above):
        #       inf * zero -> nan

        # TODO: implement what's above

        # interstep: setup.

        sign_one = self.sign_bit
        exponent_one = self.exponent
        mantissa_one = self.mantissa

        sign_two = other.sign_bit
        exponent_two = other.exponent
        mantissa_two = other.mantissa

        prod_sign = '0' if sign_one == sign_two else '1'

        # step 2: get exponents' sum.
        # 2a: get it:

        exponent_sum = basic.sum(exponent_one, exponent_two)
        exponent_sum = ('0'
                        + ('1' if exponent_sum[1] else '0')
                        + exponent_sum[0])
        exponent_sum = basic.sum(exponent_sum, '01')[0]
        exponent_sum = arth.dif(exponent_sum,
                                '0' + '1'*(EXPONENT_BIT_COUNT - 1))[0]

        # 2b: check the overflow or the underflow or whatever.
        #     (just whether exponents' sum fits in 8 bits)

        if set(exponent_sum[:2]) != set('0'):
            return (self.pos_infinity()
                    if (prod_sign == '0')
                    else self.neg_infinity())

        prod_exponent = exponent_sum[2:]

        # step 3: get mantissas' 48-bit product.

        # the following line is a bit crappy but it works as it should.
        prod_mantissa = arth.imul('0'+mantissa_one, '0'+mantissa_two)[2:]

        # step 4: normalize the result.
        # (if during normalization exponent goes zero, break the loop)

        while prod_mantissa[0] == '0':
            prod_mantissa = basic.shift_left(prod_mantissa)
            # decrementing exponent:
            prod_exponent = basic.sum(prod_exponent, '11')[0]

            if prod_exponent == '0'*EXPONENT_BIT_COUNT:
                break

        prod_mantissa = prod_mantissa[:(MANTISSA_BIT_COUNT + 1)]

        # finally return the result.
        prod_binary = prod_sign + prod_exponent + prod_mantissa[1:]
        prod = deepcopy(self)
        prod.binary = prod_binary

        return prod

    def __truediv__(self, other):
        """
        Return quotient of two Floats.
        """
        raise NotImplementedError
    