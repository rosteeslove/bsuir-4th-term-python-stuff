"""
This module contains methods to produce data
to solve the knight problem [with reduced input set]*
with O(1) time complexity.

* in case of the original problem meaning for all posiible cases

TODO: fix bc it's not exactly right.
"""

import bfs


def preprocess_into_dict(row_num, col_num):
    """
    Return dictionary of answers for all possible position shifts knight
    can make when making a move on the row_num by col_num board.

    The answers are produced by the bfs method.
    """
    dist_map = bfs.dist_map_bfs(row_num, col_num, 0, 0)

    answers = dict()
    for i in range(0, row_num):
        for j in range(i, col_num):
            answers[(i, j)] = dist_map[i][j]

    return answers