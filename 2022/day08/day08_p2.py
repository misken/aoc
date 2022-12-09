# Day 8: Treetop Tree House - Problem 2-

from pathlib import Path
import time
import numpy as np


def viewing_distance(tree_height, sorted_heights):
    """

    sorted_heights : array of int
        start searching from the top

    """

    tall_trees = np.where(sorted_heights >= tree_height)
    if len(tall_trees[0]) == 0:
        vd = len(sorted_heights)
    else:
        first_tall_tree = tall_trees[0][0]
        vd = first_tall_tree + 1
    return vd


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

    scenic_score = np.zeros(forest.shape)
    for r in range(1, num_rows - 1):
        for c in range(1, num_cols - 1):
            visible = 0
            # look left
            vd_left =  viewing_distance(forest[r, c], np.flip(forest[r, 0:c]))
            # look right
            vd_right = viewing_distance(forest[r, c], forest[r, c+1:])
            # look up
            vd_up = viewing_distance(forest[r, c], np.flip(forest[0:r, c]))
            # look down
            vd_down = viewing_distance(forest[r, c], forest[r+1:, c])

            sc = vd_left * vd_right * vd_up * vd_down
            scenic_score[r, c] = sc

            if test:
                print(f'r{r}c{c} left={vd_left}, right={vd_right}, up={vd_up}, down={vd_down}')
                print(f'scenic score = {sc}')

    if test:
        print(scenic_score)

    print(f'Part 2 (max of scenic_score): {scenic_score.max()}')


if __name__ == '__main__':
    test = False
    t1 = time.perf_counter()
    main(test)
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")

