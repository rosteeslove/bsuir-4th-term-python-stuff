"""
Модуль с переменными и функциями для 14-го варианта лаб по ТВиМС.

To be used for tasks 4 and 5.
"""


import math
import random
import numpy as np


x_a = 0
x_b = math.pi / 4


def get_x():
    return  + random.random()*(x_b-x_a)


def phi_func(x):
    return math.tan(x)


y_a = phi_func(x_a)
y_b = phi_func(x_b)

assert y_a < y_b


def get_y():
    return phi_func(get_x())


# the following functions are found analytically for the task data:

def Fy_deduced(y):
    if y < 0:
        return 0
    elif y > 1:
        return 1
    else:
        return 4 / math.pi * math.atan(y)


def fy_deduced(y):
    if y < 0 or y > 1:
        return 0
    else:
        return 4 / (math.pi * (1 + y**2))
        