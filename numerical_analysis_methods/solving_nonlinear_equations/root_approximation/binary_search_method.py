MAX_ITERATION_COUNT = 128


def _middle(left, right):
    return (left+right) / 2


def calculate_root(f, left, right, eps):
    """
    Returns the root (assuming there's one) of f function
    on the [left, right] interval using binary search algorithm.
    """

    assert f(left)*f(right) <= 0

    if f(left) == 0:
        return left
    if f(right) == 0:
        return right

    iter_count = 0
    middle = _middle(left, right)
    while abs(right-left) > eps and iter_count < MAX_ITERATION_COUNT:
        if f(middle)*f(left) > 0:
            left = middle
        else:
            right = middle
        middle = _middle(left, right)
        iter_count += 1

    return middle
