# Day 4 - Problem 1
import numpy as np

test = False
if test:
    data_file = 'data/input_test_p1.txt'
else:
    data_file = 'data/input_p1.txt'

# Method 1 - list of lists


def check_for_win(_board):
    row_sums = np.sum(_board, 1)
    col_sums = np.sum(_board, 0)

    if 0 in row_sums or 0 in col_sums:
        # Have a winner, return sum of unmarked squares
        sum_unmarked = np.sum(_board)
        return sum_unmarked
    else:
        return 0


with open(data_file, 'r') as file_input:
    draws = file_input.readline().split(',')
    draws = [int(d) for d in draws]
    print(draws)

    board = []
    all_boards = []
    for line in file_input:
        line = line.rstrip()
        if len(line) > 0:
            line = [int(v) for v in line.split()]
            board.append(line)
        else:
            # Finished reading board
            if np.sum(board) > 0:
                all_boards.append(np.array(board.copy()))
                board = []
    # Append last board
    all_boards.append(np.array(board.copy()))
    print(f'number of boards is {len(all_boards)}')

    game_over = False
    for draw in draws:
        # Mark all boards
        for board in all_boards:
            # print(board)
            # print(board.shape)
            #np.where(board == draw, 0, board)
            board[board == draw] = 0
            # Check if board is a winner
            winner = check_for_win(board)
            if winner > 0:
                final_score = winner * draw
                print(final_score)
                print(board)
                exit()




