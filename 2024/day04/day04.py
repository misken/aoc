# Day 4 - Problem 1 and 2
import numpy as np

def day04_p1(test=False):
    if test:
        data_file = 'data/input_test.txt'
    else:
        data_file = 'data/input.txt'

    with open(data_file) as f:
        word_grid = [list(line.rstrip()) for line in f.readlines()]
    #word_grid = np.loadtxt(data_file)
    #print(word_grid)

    num_rows = len(word_grid)
    num_cols = len(word_grid[0])

    tot_words = 0
    for row in range(num_rows):
        for col in range(num_cols):
            num_words = num_word_from_pos(word_grid, 'XMAS', row, col)
            tot_words += num_words
            #print(row, col, num_words)


    print(f'Problem 1 total: {tot_words}')


def num_word_from_pos(word_grid, word, row, col):

    if word_grid[row][col] != word[0]:
        return 0
    else:
        word_len = len(word)
        num_rows = len(word_grid)
        num_cols = len(word_grid[0])


        # East
        east = ''.join([word_grid[row][col + i] for i in range(word_len) if col + i < num_cols])
        # South
        south = ''.join([word_grid[row + i][col] for i in range(word_len) if row + i < num_rows])
        # West
        west = ''.join([word_grid[row][col - i] for i in range(word_len) if col - i >= 0])
        # North
        north = ''.join([word_grid[row - i][col] for i in range(word_len) if row - i >= 0])

        # NE
        ne = ''.join([word_grid[row - i][col + i] for i in range(word_len) if col + i < num_cols if row - i >= 0])
        # SE
        se = ''.join([word_grid[row + i][col + i] for i in range(word_len) if col + i < num_cols if row + i < num_cols])

        # SW
        sw = ''.join([word_grid[row - i][col - i] for i in range(word_len) if col - i >= 0 if row - i >= 0])
        # NW
        nw = ''.join([word_grid[row + i][col - i] for i in range(word_len) if col - i >= 0 if row + i < num_cols])

        potential_words = [east, south, west, north, ne, se, sw, nw]

        num_words = sum([1 for w in potential_words if w == word ])

        return num_words

def num_x_from_pos(word_grid, row, col):
    num_rows = len(word_grid)
    num_cols = len(word_grid[0])

    if word_grid[row][col] != 'A' or row == 0 or row == num_rows - 1 or col == 0 or col == num_cols - 1:
        return 0
    else:
        # NW-SE
        nw = ''.join([word_grid[row - 1][col - 1], word_grid[row + 1][col + 1]])
        sw = ''.join([word_grid[row + 1][col - 1], word_grid[row - 1][col + 1]])

        if (nw == 'SM' or nw == 'MS') and (sw == 'SM' or sw == 'MS'):
            return 1
        else:
            return 0

def day04_p2(test=False):
    if test:
        data_file = 'data/input_test.txt'
    else:
        data_file = 'data/input.txt'

    with open(data_file) as f:
        word_grid = [list(line.rstrip()) for line in f.readlines()]

    num_rows = len(word_grid)
    num_cols = len(word_grid[0])

    tot_words = 0
    for row in range(num_rows):
        for col in range(num_cols):
            num_words = num_x_from_pos(word_grid, row, col)
            tot_words += num_words
            #print(row, col, num_words)


    print(f'Problem 2 total: {tot_words}')



if __name__ == '__main__':
    test = False
    day04_p1(test)
    day04_p2(test)
