# Day 8: Treetop Tree House - Problem 1

from pathlib import Path
import time
import numpy as np


def main(test=False):

    if test:
        data_file = Path('data/input_test.txt')
    else:
        data_file = Path('data/input.txt')

    with open(data_file, 'r') as f_in:
        forest_rows = [row.rstrip() for row in f_in.readlines()]
        forest = [[int(c) for c in row] for row in forest_rows]

        forest = np.array(forest)

    print(forest.shape)
    if test:
        print(forest)

    num_rows = forest.shape[0]
    num_cols = forest.shape[1]

    num_visible_interior = 0
    for r in range(1, num_rows - 1):
        for c in range(1, num_cols - 1):
            visible = 0
            # look left
            if max(forest[r, 0:c]) < forest[r, c]:
                visible += 1
            # look right
            if max(forest[r, c+1:]) < forest[r, c]:
                visible += 1
            # look up
            if max(forest[0:r, c]) < forest[r, c]:
                visible += 1
            # look down
            if max(forest[r+1:, c]) < forest[r, c]:
                visible += 1

            if test:
                print(f'r{r}c{c} visible={visible}')

            if visible > 0:
                num_visible_interior += 1

    num_visible_exterior = num_cols * 2 + (num_rows - 2) * 2

    num_visible = num_visible_exterior + num_visible_interior
    print(f'Part 1 (num_visible): {num_visible_exterior}+{num_visible_interior}={num_visible}')


if __name__ == '__main__':
    test = False
    t1 = time.perf_counter()
    main(test)
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")

