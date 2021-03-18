KNIGHT_MOVES = [[-2, -1],
                [-2,  1],
                [-1, -2],
                [-1,  2],
                [ 1, -2],
                [ 1,  2],
                [ 2, -1],
                [ 2,  1]]


def solution(row_num, col_num, cur_row, cur_col, dest_row, dest_col):
    move_num = 0
    while cur_row != dest_row or cur_col != dest_col:
        """
        print(cur_row)
        print(cur_col)
        print('')
        """
        
        difs_sums = []
        coeffs = []
        valid_moves = []

        row_dif = abs(cur_row - dest_row)
        col_dif = abs(cur_col - dest_col)

        for move in KNIGHT_MOVES:
            new_row = cur_row + move[0]
            new_col = cur_col + move[1]

            new_row_dif = abs(new_row - dest_row)
            new_col_dif = abs(new_col - dest_col)

            if (0 <= new_row < row_num and 0 <= new_col < col_num
                    and (new_row_dif < row_dif or new_col_dif < col_dif)):
                valid_moves.append((new_row, new_col))    
                difs_sums.append((new_row_dif + new_col_dif))

                try:
                    if new_row_dif < new_col_dif:
                        new_coeff = abs(new_row_dif / new_col_dif - 0.5)
                    else:
                        new_coeff = abs(new_col_dif / new_row_dif - 0.5)
                except Exception:
                    return move_num + 1

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

        cur_row, cur_col = valid_moves[min_coeff_index]
        move_num += 1

    return move_num

