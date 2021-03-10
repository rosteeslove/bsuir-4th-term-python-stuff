import numpy as np

# метод хорд

def CalculateRoot(f, l, r, f_delta):
    assert f(l)*f(r) < 0
    # TODO: add assert to check derivatives' behavior

    if f(l) > 0:
        f = -f

    while True:
        l += (r - l) / (f(r) - f(l)) * abs(f(l))
        if abs(f(l)) < f_delta:
            break

    return l
