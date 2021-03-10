
import numpy as np
import struct


MANTISSA_BIT_COUNT = 23
EXPONENT_BIT_COUNT = 8


class Float:

    @staticmethod
    def from_py_float(num):
        return (''.join(bin(ord(c)).replace('0b', '').rjust(8, '0') 
                for c in struct.pack('!f', num)))

    #def to_py_float(self):
        

    def __init__(self, num):
        self.binary = self.from_py_float(num)

    