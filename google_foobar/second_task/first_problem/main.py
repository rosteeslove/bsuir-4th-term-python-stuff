"""
Solution variants:

1. bfs on each function call;
2. numerical approach (?);

3. answer preprocessing bc the input set is reduced;
"""


import bfs
import num_sol
import preproc

CHESSBOARD_SIZE = 9


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

    return num_sol.solution(CHESSBOARD_SIZE, CHESSBOARD_SIZE,
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
    print(*bfs.dist_map_bfs(CHESSBOARD_SIZE, CHESSBOARD_SIZE, 0, 0), sep='\n')
    #print(num_sol.solution(CHESSBOARD_SIZE, CHESSBOARD_SIZE, 0, 0, 0, 6))

    for i in range(6):
        for j in range(6):
            print('{0}'.format(num_sol.solution(CHESSBOARD_SIZE,
                                                CHESSBOARD_SIZE,
                                                0, 0,
                                                i, j)), end=', ')
        print('')



if __name__ == "__main__":
    main()
