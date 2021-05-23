"""
This module contains the calculate_root method to find function f's
root on (a, b) interval using binary search algorithm.
"""


MAX_ITERATION_COUNT = 1_000


def calculate_root(f, a, b, eps):
    """
    Return root (assuming there's one) of f function
    on the (a, b) interval using binary search algorithm
    and also return number of iterations.
    """
    assert f(a)*f(b) < 0

    iter_count = 0
    middle = (a+b) / 2
    while (abs(b-a) > eps
           and iter_count < MAX_ITERATION_COUNT):
        if f(middle)*f(a) > 0:
            a = middle
        else:
            b = middle
        middle = (a+b) / 2
        iter_count += 1

    return middle, iter_count
