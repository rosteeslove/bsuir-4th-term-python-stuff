"""

"""

import sys
import time
import random
from ast import literal_eval

import numpy as np

import my_float as mf


def test():
    random.seed(69)
    while True:
        a = np.float32(np.random.random())
        print(a)
        b = np.float32(np.random.random())
        print(b)
        sum = a + b

        my_a = mf.Float(a)
        my_b = mf.Float(b)
        my_sum = my_a + my_b

        print(sum)
        print(mf.Float.bin_to_float(my_sum.binary))
        print('')

        time.sleep(0.5)

test()