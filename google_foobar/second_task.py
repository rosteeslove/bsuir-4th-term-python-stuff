"""
Solution variants:

1. bfs on each function call;
2. numerical approach (?);

3. answer preprocessing;
"""


CHESSBOARD_SIZE = 8
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
    yet set; Return the list of such positions.
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


def _dist_map_bfs(size, row, col):
    """
    Return size by size map of distances from row-col position
    to each position of the board.
    """
    q_index = 0
    q = []
    q.append((row, col))

    board = [[-1 for i in range(size)] for j in range(size)]
    board[row][col] = 0

    while True:
        q += _bfs_iteration(board, q[q_index][0], q[q_index][1])
        q_index += 1
        if q_index == len(q):
            break

    return board


def solution1(src, dest):
    dist_map = _dist_map_bfs(CHESSBOARD_SIZE,
                             src // CHESSBOARD_SIZE,
                             src % CHESSBOARD_SIZE)

    return dist_map[dest // CHESSBOARD_SIZE][dest % CHESSBOARD_SIZE]


def main():
    print(solution1(0, 63))


if __name__ == "__main__":
    main()
