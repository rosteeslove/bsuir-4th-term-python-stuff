"""
This module contains functions to retrieve chi squared coefficient
for a varseries and a hypothesis function.
"""


import scipy.stats as ss

import hist
import extras


def chi_squared(vs, hypo_F, bincount=None):
    n = len(vs)
    if not bincount:
        bincount = extras.optimal_bin_count(n)
    m = bincount

    # getting expected and observed data:
    hdata = hist.equalvar(vs, m, mode='частости')
    xs = [hd[0] for hd in hdata]
    ys = [hd[1] for hd in hdata]

    expected_ys = [hypo_F(xs[i+1]) - hypo_F(xs[i]) for i in range(m)]
    observed_ys = ys[:-1]

    # checking this weird condition from bsuir docs:
    assert abs(1 - sum(expected_ys)) <= 0.01

    # calculating the chi squared:
    summands = []
    for i in range(m):
        summand = ((observed_ys[i] - expected_ys[i])**2
                   / (expected_ys[i]))
        summands.append(summand)

    result = n*sum(summands)
    return result


def chi_critical(alpha, degrees_of_freedom):
    return ss.chi2.ppf(1-alpha, degrees_of_freedom)
    