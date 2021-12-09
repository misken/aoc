# Day 9 - Problem 1
import numpy as np
from pprint import pprint

test = True

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

    low_points = []
    for i in range(nrows):
        for j in range(ncols):
            adj = adjacent(i, j, nrows, ncols)
            if sum([heights[i, j] >= heights[a[0], a[1]] for a in adj]) == 0:
                low_points.append((i, j))

    return low_points


def find_basins(_heights, _low_points, nrows, ncols):

    basins = {}

    for pt in _low_points:
        new_basin = set([pt])
        to_check = new_basin.copy()

        while len(to_check) > 0:
            check = to_check.pop()
            adj = set(adjacent(check[0], check[1], nrows, ncols))
            for a in adj:
                # Check if a is part of the basin
                i, j = a[0], a[1]
                # Can't be in basin if height is 9
                if _heights[i, j] < 9:
                    if _heights[i, j] > _heights[check[0], check[1]]:
                        new_basin.add(a)
                        to_check.add(a)

        # Found basin around this low point
        basins[pt] = new_basin

    return basins


with open(data_file, 'r') as file_input:
    lines = [line.strip() for line in file_input.readlines()]
    heights = np.array([[int(t) for t in line] for line in lines])
    nrows = heights.shape[0]
    ncols = heights.shape[1]

    low_points = find_low_points(heights)
    print(low_points)
    basins = find_basins(heights, low_points, nrows, ncols)
    basin_sizes = [len(v) for k, v in basins.items()]
    basin_sizes.sort(reverse=True)
    pprint(basins)
    print(basin_sizes)
    print(basin_sizes[0], basin_sizes[1], basin_sizes[2])
    print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])









