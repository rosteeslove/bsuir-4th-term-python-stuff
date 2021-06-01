"""
This module contains some base functions for math statistics.

To be used for tasks 4 and 5.
"""


def generate_varseries(get_rv, n):
    ys = []

    for _ in range(n):
        ys.append(get_rv())

    ys.sort()
    return ys
    