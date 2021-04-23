"""
This module contains the solution function.

Full task description is in readme.txt.

Short task description:

Given a number of bricks, compute a number of ways
a staircase can be built. A valid staircase consists of
at least 2 steps of some positive height, each of the steps
being lower than the previous one, the sum of steps' heights
being the number of bricks.
"""


def solution(x):
    """Return a number of ways to build a staircase
    of a given number of bricks.

    The rules are in the readme.txt and succintly in the
    module docstring.

    Args:
        x (int): number of bricks (3 <= x <= 200).
    """
    table = [[0 for _ in range(x+1)] for __ in range(x+1)]
    table[2][1] = 1
    for m in range(3, x):
        for n in range(1, x):
            if n >= m:
                for i in range(1+n-m, m):
                    table[m][n] += table[i][n-i]
            else:
                table[m][n] = 1 + table[n][n]

            if table[m][n] == 0:
                break

    result = 0
    for i in range(1, x):
        result += table[i][x - i]

    return result
