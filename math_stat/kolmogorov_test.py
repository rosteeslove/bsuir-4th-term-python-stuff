"""
This module contains functions to retrieve 
Kolmogorov's lambda coefficient
for a varseries and a hypothesis function.

To be used for tasks 4 and 5.
"""


import math
import numpy as np


# Kolmogorov table data:

klambda_090 = 1.22
klambda_095 = 1.36
klambda_099 = 1.63


def max_deviation(vs, Fy_analytic):
    n = len(vs)

    a = min(vs)
    b = max(vs)

    # getting expected data:
    xs = np.linspace(a, b, 1000)
    expected_ys = [Fy_analytic(x) for x in xs]

    # getting observed data:
    observed_ys = [0]*len(xs)
    index = 0
    for (i, x) in enumerate(xs):
        while index < n and x > vs[index]:
            index += 1
        observed_ys[i] = index/n

    # getting the deviations:
    observed_ys = np.array(observed_ys)
    diffs = np.abs(expected_ys - observed_ys)
    
    return max(diffs)


def klambda(vs, Fy_analytic):
    n = len(vs)
    md = max_deviation(vs, Fy_analytic)
    return math.sqrt(n)*md
