"""
https://www.python-course.eu/polynomial_class_in_python.php
"""


import numpy as np


def _zip_longest(iter1, iter2, fillvalue=None):
    """
    For using when adding and subtracting polynomials.
    """
    for i in range(max(len(iter1), len(iter2))):
        if i >= len(iter1):
            yield (fillvalue, iter2[i])
        elif i >= len(iter2):
            yield (iter1[i], fillvalue)
        else:
            yield (iter1[i], iter2[i])
        i += 1


def _remove_leading_zeros(a):
    """
    Removes leading zeros in the a string only leaving one
    if it's the only character in the string.
    """
    i = 0
    for i in range(len(a)):
        if a[i] != 0:
            break

    return a[i:]


class Polynomial:

    def __init__(self, *coefficients):
        """
        Input: coefficients are in the form a_n, ...a_1, a_0
        """
        self.coefficients = _remove_leading_zeros(list(coefficients))

    def __repr__(self):
        """
        Method to return the canonical string representation\
        of a polynomial.
        """
        return "polynomial" + str(tuple(self.coefficients))

    def __str__(self):

        def x_expr(degree):
            if degree == 0:
                res = ""
            elif degree == 1:
                res = "x"
            else:
                res = "x^"+str(degree)
            return res

        if self.is_zero():
            return "0"

        degree = len(self.coefficients) - 1
        res = ""

        for i in range(0, degree+1):
            coeff = self.coefficients[i]

            if abs(coeff) == 1 and i < degree:
                res += f"{'+' if coeff>0 else '-'}{x_expr(degree-i)}"
            elif coeff != 0:
                res += f"{coeff:+g}{x_expr(degree-i)}"

        return res.lstrip('+') # removing leading '+'

    def copy(self):
        return Polynomial(*(self.coefficients.copy()))

    def __call__(self, x):
        res = 0
        for coeff in self.coefficients:
            res = res * x + coeff
        return res

    """ 
    Alternative to the prior function:
    def __call__(self, x):
        res = 0
        for index, coeff in enumerate(self.coefficients[::-1]):
            res += coeff * x** index
        return res
    """

    def degree(self):
        """
        Returns the instance polynomial's degree.
        """
        return len(self.coefficients)

    def __neg__(self):
        return Polynomial(*[-c for c in self.coefficients])

    def __add__(self, other):
        if isinstance(other, (int, float, np.number)):
            return self+Polynomial(other)

        c1 = self.coefficients[::-1]
        c2 = other.coefficients[::-1]

        res = [sum(t) for t in _zip_longest(c1, c2, fillvalue=0)]
        return Polynomial(*res[::-1])

    def __sub__(self, other):
        if isinstance(other, (int, float, np.number)):
            return self-Polynomial(other)

        c1 = self.coefficients[::-1]
        c2 = other.coefficients[::-1]

        res = [t1-t2 for t1, t2 in _zip_longest(c1, c2, fillvalue=0)]
        return Polynomial(*res[::-1])

    def __mul__(self, other):
        if isinstance(other, (int, float, np.number)):
            return self*Polynomial(other)

        c1 = self.coefficients[::-1]
        c2 = other.coefficients[::-1]
        prod = (self.degree()+other.degree()-1) * [0]

        for i in range(len(c1)):
            for j in range(len(c2)):
                prod[i+j] += c1[i]*c2[j]

        return Polynomial(*prod[::-1])

    def __truediv__(self, other):
        if isinstance(other, (int, float, np.number)):
            return self/Polynomial(other)

        assert not other.is_zero()

        dividend = self.copy()
        divisor = other
        q = Polynomial(0)
        while (dividend.degree() >= divisor.degree() and 
               not dividend.is_zero()):

            k = dividend.coefficients[0] / divisor.coefficients[0]
            kp = Polynomial(k, *([0]*(dividend.degree()-divisor.degree())))
            subtrahend = divisor*kp
            dividend = dividend-subtrahend
            q = q+kp

        return q, dividend

    def derivative(self):
        derived_coeffs = []
        exponent = len(self.coefficients) - 1
        for i in range(len(self.coefficients)-1):
            derived_coeffs.append(self.coefficients[i] * exponent)
            exponent -= 1

        # adding leading zero so that
        # if the list is empty the polynomial is 0
        derived_coeffs.insert(0, 0) 
        return Polynomial(*derived_coeffs)

    def is_zero(self):
        return self.degree() == 1 and self.coefficients[0] == 0
