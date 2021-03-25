"""
This script exists to perform tests on operations w/ my float type.

The point is:
    1. to generate random float arguments for an operation
        that's being tested.
    2. to produce identical arguments of my float type.
    3. to produce the float operation result res.
    4. to produce my float operation result my_res.
    5. to check whether res and my_res are the same thing. 
"""

import random

import numpy as np

from my_float import Float


def test():
    random.seed(69)
    while True:
        a = np.float32(np.random.uniform(-1000000.0, 1000000.0))
        b = np.float32(np.random.uniform(-1000000.0, 1000000.0))
        
        my_a = Float(a)
        my_b = Float(b)
        
        print('{0} + {1} = {2}'.format(a, b, a+b))
        print('{0} + {1} = {2}'.format(my_a, my_b, my_a+my_b))
        print('{0} + {1} = {2}'.format(Float.float_to_bin(a),
                                       Float.float_to_bin(b),
                                       Float.float_to_bin(a+b)))
        print('{0} + {1} = {2}'.format(my_a.binary,
                                       my_b.binary,
                                       (my_a+my_b).binary))
        print('-'*50)



test()