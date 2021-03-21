"""
Solution variants:

1. bfs on each function call;
2. numerical approach (?);

3. answer preprocessing bc the input set is reduced;
"""


import bfs
import num_sol
import how_not_to_write_code as hntwc
import preproc

CHESSBOARD_SIZE = 8


# 1:
def solution1(src, dest):
    dist_map = bfs.dist_map_bfs(CHESSBOARD_SIZE,
                                CHESSBOARD_SIZE,
                                src // CHESSBOARD_SIZE,
                                src % CHESSBOARD_SIZE)

    return dist_map[dest // CHESSBOARD_SIZE][dest % CHESSBOARD_SIZE]


# 2:
def solution2(src, dest):
    cur_row, cur_col = _translate_to_rc(src)
    dest_row, dest_col = _translate_to_rc(dest)

    return hntwc.solution(CHESSBOARD_SIZE, CHESSBOARD_SIZE,
                          cur_row, cur_col, dest_row, dest_col)


# 3:
"""
An overview:

(before getting queries):
answers = preproc.preprocess_into_dict(CHESSBOARD_SIZE,
                                       CHESSBOARD_SIZE)

(the solution method then would be):
def solution3(src, dest):
    src_row, src_col = _translate_to_rc(src)
    dest_row, dest_col = _translate_to_rc(dest)

    row_shift = abs(src_row - dest_row)
    col_shift = abs(src_col - dest_col)

    smaller_shift = row_shift if row_shift < col_shift else col_shift
    bigger_shift = col_shift if col_shift > row_shift else row_shift

    return answers[(smaller_shift, bigger_shift)]

(haven't tested it though)
"""


def _translate_to_rc(pos_int):
    return pos_int // CHESSBOARD_SIZE, pos_int % CHESSBOARD_SIZE


def main():
    print(*bfs.dist_map_bfs(CHESSBOARD_SIZE, CHESSBOARD_SIZE, 2, 2), sep='\n')
    print('')
    # print(solution2(0, 14))

    for i in range(CHESSBOARD_SIZE):
        print(' ', end='')
        for j in range(CHESSBOARD_SIZE):
            print(solution2(2*CHESSBOARD_SIZE + 2, i*CHESSBOARD_SIZE + j), end=', ')
        print('')


if __name__ == "__main__":
    main()
