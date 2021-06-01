"""
This module contains some extra functions for math statistics tasks.

To be used for tasks 4 and 5.
"""


import math
import numpy as np


def optimal_bin_count(n):
    return math.floor(np.cbrt(n))
    