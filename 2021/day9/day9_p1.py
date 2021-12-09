# Day 9 - Problem 1
import numpy as np


test = False

if test:
    data_file = 'data/example.txt'
else:
    data_file = 'data/input.txt'

def adjacent(i, j, nrows, ncols):

    adj = []
    if i == 0:
        up = None
        down = (i + 1, j)
        adj.append(down)
    elif i == nrows - 1:
        down = None
        up = (i - 1, j)
        adj.append(up)
    else:
        up = i - 1, j
        down = i + 1, j
        adj.append(down)
        adj.append(up)


    if j == 0:
        left = None
        right = i, j + 1
        adj.append(right)
    elif j == ncols - 1:
        right = None
        left = i, j - 1
        adj.append(left)
    else:
        left = i, j - 1
        right = i, j + 1
        adj.append(right)
        adj.append(left)

    return adj

def find_low_points(heights):
    nrows = heights.shape[0]
    ncols = heights.shape[1]

    print(nrows, ncols)
    low_points = []
    for i in range(nrows):
        for j in range(ncols):
            adj = adjacent(i, j, nrows, ncols)
            print(adj)
            if sum([heights[i, j] >= heights[a[0], a[1]] for a in adj]) == 0:
                low_points.append((i, j))

    print(low_points)

    total_risk = sum([heights[a[0], a[1]] + 1 for a in low_points])
    print(total_risk)



with open(data_file, 'r') as file_input:
    lines = [line.strip() for line in file_input.readlines()]
    heights = np.array([[int(t) for t in line] for line in lines])

    print(heights)

    find_low_points(heights)









