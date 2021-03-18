"""
This module contains the get_root_intervals_from_user method
for root isolation.

Remark: this is kind of dumb.
"""


import numpy as np
import matplotlib.pyplot as plt


def _get_float(prompt):
    """
    Asks user for console input with the prompt message.
    Returns float if input can be interpreted as float,
    None otherwise.
    """
    try:
        return float(input(prompt))
    except ValueError:
        return None


def get_root_intervals_from_user(f, left, right):
    """
    Returns the list of root intervals of f function
    on the [left, right] interval deduced
    by the user judging by the function's plot.
    """

    # showing the plot.
    X = np.linspace(left, right, endpoint=True)
    F = f(X)
    plt.plot(X, F)
    
    def zero(x):
        return x*0

    Z = zero(X)
    plt.plot(X, Z)

    plt.show()

    # asking for the root intervals.
    print("Enter intervals' borders:\n")
    intervals = []
    while True:
        print('\tDefine the interval:')
        left = _get_float('\t\tEnter the left border: ')
        if left is None:
            break
        right = _get_float('\t\tEnter the right border: ')
        if right is None:
            break
        print('\n')

        intervals.append(left, right)

    return intervals