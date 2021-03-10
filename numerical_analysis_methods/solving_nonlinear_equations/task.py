import math
import numpy as np
import matplotlib.pyplot as plt

import polynomial as poly
import sturms_method as sm

import root_isolation.manual_method as ri_mm


l, r = -10, 10

a = -10.2374
b = -91.2105
c = 492.560

def one(x):
    return 0


def main():
    f1 = poly.Polynomial(1, 0, -1, 0)
    print(f1)

    print(sm.count_roots(f1, -10, 10))

    ri_mm.get_root_intervals_from_user(f1, -10, 10)


if __name__ == "__main__":
    main()
