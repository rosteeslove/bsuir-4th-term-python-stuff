"""
The explanation to be here for why this module exists:

...

"""


KNIGHT_MOVES = [[-2, -1],
                [-2,  1],
                [-1, -2],
                [-1,  2],
                [ 1, -2],
                [ 1,  2],
                [ 2, -1],
                [ 2,  1]]

TOO_MUCH = 256


def solution(row_num, col_num, cur_row, cur_col, dest_row, dest_col):
    move_num = 0

    old_row = cur_row
    old_col = cur_col

    while ((cur_row != dest_row or cur_col != dest_col)
           and move_num < TOO_MUCH):
        difs_sums = []
        coeffs = []
        valid_moves = []

        row_dif = abs(cur_row - dest_row)
        col_dif = abs(cur_col - dest_col)

        for move in KNIGHT_MOVES:
            new_row = cur_row + move[0]
            new_col = cur_col + move[1]

            if new_row == old_row and new_col == old_col:
                continue

            new_row_dif = abs(new_row - dest_row)
            new_col_dif = abs(new_col - dest_col)

            if (0 <= new_row < row_num and 0 <= new_col < col_num
                    and (new_row_dif <= row_dif or new_col_dif <= col_dif
                         or row_dif == 0 or col_dif == 0)):
                valid_moves.append((new_row, new_col))    
                difs_sums.append((new_row_dif + new_col_dif))

                if new_row_dif == 0 and new_col_dif == 0:
                    return move_num + 1
                elif new_row_dif < new_col_dif:
                    new_coeff = abs(new_row_dif / new_col_dif - 0.5)
                else:
                    new_coeff = abs(new_col_dif / new_row_dif - 0.5)

                coeffs.append(new_coeff)

        # choosing the best move.  Basically
        # among those w/ the smallest coeff
        # choose the one moving the knight towards the destination.
        smallest_coeffs_indices = []
        for i in range(len(coeffs)):
            if (smallest_coeffs_indices
                    and coeffs[i] < coeffs[smallest_coeffs_indices[0]]):
                smallest_coeffs_indices.clear()
                smallest_coeffs_indices.append(i)
            elif (not smallest_coeffs_indices
                      or coeffs[i] == coeffs[smallest_coeffs_indices[0]]):
                smallest_coeffs_indices.append(i)

        difs_sums_left = []
        for index in smallest_coeffs_indices:
            difs_sums_left.append(difs_sums[index])

        min_difs_index = difs_sums_left.index(min(difs_sums_left))
        min_coeff_index = smallest_coeffs_indices[min_difs_index]

        old_row = cur_row
        old_col = cur_col

        cur_row, cur_col = valid_moves[min_coeff_index]
        move_num += 1

    return 0 if move_num == 0 else -1

