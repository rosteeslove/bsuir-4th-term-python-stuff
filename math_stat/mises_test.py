"""
This module contains functions to retrieve omega squared coefficient
for a varseries and a hypothesis function.

To be used for tasks 4 and 5.
"""


# Mises table data:

momega_090 = 0.347
momega_095 = 0.461
momega_099 = 0.744


def momega(vs, Fy_analytic):
    n = len(vs)

    n_omega_squared = 0
    n_omega_squared += 1/(12*n)

    for (i, v) in enumerate(vs):
        n_omega_squared += (Fy_analytic(v) - (i-0.5)/n)**2

    return n_omega_squared
