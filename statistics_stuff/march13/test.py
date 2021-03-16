import math

from random import seed
from random import random
import matplotlib.pyplot as plt


def F(R, r, d):
    return 2 * math.acos((R**2 - r**2 + d**2) / (2 * R * d))

def S(R, F):
    return R**2 * (F - math.sin(F)) / 2

def s_intersection(r1, r2, d):
    return S(r1, F(r1, r2, d)) + S(r2, F(r2, r1, d))

seed(69)

R1 = 1
R2 = 0.5
r = 0.5

anses = []
tests_count = 10_000
for _ in range(tests_count):
    while True:
        x = 2 * random() - 1
        y = 2 * random() - 1
        if (x**2 + y**2 <= R1**2):
            break
    if (x**2 + y**2 <= (R2-r)**2):
        anses += [math.pi * r**2]
    elif (x**2 + y**2 >= (R2+r)**2):
        anses += [0]
    else:
        d = math.sqrt(x**2 + y**2)
        anses += [s_intersection(R2, r, d)]

anses.sort()

plt.plot(anses, range(1, tests_count + 1))
plt.show()

