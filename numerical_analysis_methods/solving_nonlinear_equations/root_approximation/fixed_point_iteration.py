import numpy as np
import time

def iteration(f, l, x0):
    return x0 - l(x0)*f(x0)

# 'l' parameter is lambda-function which facilitates the convergence
def calculate_root(f, l, x0, f_delta):
    x = x0

    while True:
        x = iteration(f, l, x)
        print(x)
        time.sleep(0.5)
        if abs(f(x)) < f_delta:
            break

    return x
