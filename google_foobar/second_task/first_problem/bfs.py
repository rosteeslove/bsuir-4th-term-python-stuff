"""
This module contains a method (dist_map_bfs)
to solve the knight problem.

Probably the most elegant solution.
"""


KNIGHT_MOVES = [[-2, -1],
                [-2,  1],
                [-1, -2],
                [-1,  2],
                [ 1, -2],
                [ 1,  2],
                [ 2, -1],
                [ 2,  1]]


def _bfs_iteration(board, row, col):
    """
    Set distances for all possible positions the knight can
    move to from the row-col position if the distances are not
    yet set; Return the list of such positions afterwards.
    """
    q_appendix = []

    for move in KNIGHT_MOVES:
        new_row = row + move[0]
        new_col = col + move[1]

        if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]):
            if board[new_row][new_col] == -1:
                board[new_row][new_col] = board[row][col] + 1
                q_appendix.append((new_row, new_col))

    return q_appendix


def dist_map_bfs(row_num, col_num, row, col):
    """
    Return [row_num by col_num list]* of distances
    from row-col position to each position of the board.

    * i.e. the row_num-element list of col_num-element lists.
    """   
    # setting up the chessboard:
    board = [[-1 for i in range(col_num)] for j in range(row_num)]
    board[row][col] = 0

    # setting up the bfs queue:
    q = []
    q.append((row, col))

    # running the algorithm.
    for pos in q:
        q += _bfs_iteration(board, pos[0], pos[1])

    return board