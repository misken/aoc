# Day 12: Transparent origami  - Problem 1
import numpy as np
import matplotlib.pyplot as plt

"""
Notes:

- seems like the folds are always exactly halfway - 1 and thus we always have
an odd number of rows and columns
- the fold row supposedly never has dots and will remain this way
- NO IDEA WHY I ENDED UP DOING THIS FOR FOLDS AT ANY PLACE, NOT JUST THE HALFWAY POINT!
"""
test = False
mini = False

if test:
    if mini:
        data_file = f'data/mini_example.txt'
    else:
        data_file = f'data/example.txt'
else:
    data_file = 'data/input.txt'

def fold_paper(_paper, axis, n):
    current_nrows, current_ncols = _paper.shape
    if axis == 'y':
        # fold horizontally on a row
        rows_below_fold = current_nrows - n - 1
        rows_above_fold = current_nrows - rows_below_fold - 1
        # nonoverlapping > 0 --> extract from top else extract from bottom
        nrows_nonoverlapping = rows_above_fold - rows_below_fold

        if nrows_nonoverlapping > 0:
            overlap_type = 1
            nonoverlapping = _paper[:nrows_nonoverlapping, :]
            folded_bottom = _paper[nrows_nonoverlapping:n, :]
            folded_top = np.flipud(_paper[n + 1:, :])

            overlapping = folded_bottom + folded_top
            overlapping[overlapping > 0] = 1

            folded_paper = np.concatenate((nonoverlapping, overlapping))

            # print(nonoverlapping)
            # print(folded_bottom)
            # print(folded_top)


        elif nrows_nonoverlapping < 0:
            overlap_type = -1

            nonoverlapping = np.flipud(_paper[nrows_nonoverlapping:, :])
            folded_bottom = _paper[:n, :]
            folded_top = np.flipud(_paper[n + 1:n + 1 + rows_above_fold, :])

            overlapping = folded_bottom + folded_top
            overlapping[overlapping > 0] = 1

            folded_paper = np.concatenate((nonoverlapping, overlapping))

        else:
            overlap_type = 0
            nonoverlapping = None
            folded_bottom = _paper[:n, :]
            folded_top = np.flipud(_paper[n + 1:, :])

            overlapping = folded_bottom + folded_top
            overlapping[overlapping > 0] = 1

            folded_paper = overlapping

        # print(overlap_type)
        # print(nonoverlapping)
        # print(folded_bottom)
        # print(folded_top)
        # print(overlapping)

        print(folded_paper.shape)
        return(folded_paper)


    else:
        folded_paper = fold_paper(np.transpose(_paper), 'y', n)
        return np.transpose(folded_paper)


with open(data_file, 'r') as file_input:
    lines = file_input.readlines()
    dots = [line.strip().split(',') for line in lines if ',' in line]
    dots = [[int(dot[0]), int(dot[1])] for dot in dots]
    folds = [line.strip().split('=') for line in lines if 'fold' in line]
    folds = [[fold[0][-1], int(fold[1])] for fold in folds]

    max_col_num = np.max([dot[0] for dot in dots])
    max_row_num = np.max([dot[1] for dot in dots])

    #print(dots)
    print(f'max_col_num={max_col_num}, max_row_num={max_row_num}')
    #print(folds)

    paper = np.zeros((max_row_num + 1, max_col_num + 1))
    #print(paper)
    print(paper.shape)

    for (x, y) in dots:
        paper[y, x] = 1

    print(paper)

    for fold in folds:
        print(fold)
        paper = fold_paper(paper, fold[0], fold[1])
        print(f'Num dots for {fold} is {np.sum(paper)}')

    print(paper)

    plt.matshow(paper)
    plt.show()





