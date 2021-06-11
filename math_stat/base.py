"""
This module contains some base functions for math statistics.
"""


def generate_varseries(get_rv, n):
    ys = []

    for _ in range(n):
        ys.append(get_rv())

    ys.sort()
    return ys
    