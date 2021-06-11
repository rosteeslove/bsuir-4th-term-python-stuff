"""
This module contains some extra functions for math statistics tasks.
"""


import math
import numpy as np


def optimal_bin_count(n):
    assert n > 0

    if n <= 100:
        return math.floor(np.sqrt(n))
    else:
        return 3*math.floor(np.log10(n))
    