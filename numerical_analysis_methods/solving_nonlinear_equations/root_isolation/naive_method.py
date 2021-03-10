"""
This module contains the isolate_roots method for root isolation
for any function.  The method iterates the main interval with the
same step to find intervals in which the function crosses the x-axis.
"""


DEFAULT_STEP = 0.01


def isolate_roots(f, left, right):
    """
    Returns the list of root intervals of f function
    in the [left, right] interval using the most naive
    approach i.e. iterating the main interval to find
    where the function line crosses the x-axis.
    """
    root_intervals = []
    current_pos = left
    while right > current_pos:
        if f(current_pos) == 0:
            root_intervals.append(current_pos, current_pos)
        elif f(current_pos)*f(current_pos + DEFAULT_STEP) < 0:
            root_intervals.append(current_pos, current_pos+DEFAULT_STEP)

        current_pos += DEFAULT_STEP

    return root_intervals
