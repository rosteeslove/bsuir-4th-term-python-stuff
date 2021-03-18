MAX_ITERATION_COUNT = 1024
MIN_EPS = 0.000000000001

def _middle(left, right):
    return (left+right) / 2


def calculate_root(f, left, right, eps):
    """
    Return root (assuming there's one) of f function
    on the [left, right] interval using binary search algorithm
    and also return number of iterations.
    """
    assert f(left)*f(right) <= 0

    if f(left) == 0:
        return left
    if f(right) == 0:
        return right

    iter_count = 0
    middle = _middle(left, right)
    while (abs(right-left) > eps
           and iter_count < MAX_ITERATION_COUNT
           and right-left > MIN_EPS):
        if f(middle)*f(left) > 0:
            left = middle
        else:
            right = middle
        middle = _middle(left, right)
        iter_count += 1

    return middle, iter_count
