# Day 9 - Problem 1
import numpy as np
from pprint import pprint

test = True

if test:
    data_file = 'data/example.txt'
else:
    data_file = 'data/input.txt'


def adjacent(i, j):
    """Assumes matrix is padded with 9's all around"""

    adj = []

    up = i - 1, j
    down = i + 1, j
    left = i, j - 1
    right = i, j + 1

    adj.extend([up, down, left, right])

    return adj


def find_low_points(heights):

    nrows = heights.shape[0]
    ncols = heights.shape[1]

    _low_points = []
    for i in range(1, nrows - 1):
        for j in range(1, ncols - 1):
            adj = adjacent(i, j)
            if sum([heights[i, j] >= heights[a[0], a[1]] for a in adj]) == 0:
                _low_points.append((i, j))

    return _low_points


def find_basins(_heights, _low_points):

    _basins = {}

    for pt in _low_points:
        new_basin = {pt}
        to_check = new_basin.copy()

        while len(to_check) > 0:
            x, y = to_check.pop()
            adj = set(adjacent(x, y))
            for (i, j) in adj:
                # Can't be in basin if height is 9
                if _heights[i, j] < 9:
                    # Is neighbor higher than x, y?
                    if _heights[i, j] > _heights[x, y]:
                        new_basin.add((i, j))
                        to_check.add((i, j))

        # Found basin around this low point
        _basins[pt] = new_basin

    return _basins


with open(data_file, 'r') as file_input:

    # Read array of heights
    heights = np.array(np.genfromtxt(data_file, delimiter=1))

    # Pad the array with 9's to make edge cases easier
    heights = np.pad(heights, 1, 'constant', constant_values=9)
    #print(heights)

    # Find the low points and compute risk level (Part 1)
    low_points = find_low_points(heights)
    total_risk = sum([heights[a, b] + 1 for (a, b) in low_points])
    print(f'total risk: {total_risk} (Part 1)')

    # Find the basin around each low point
    basins = find_basins(heights, low_points)
    basin_sizes = [len(v) for k, v in basins.items()]
    basin_sizes.sort(reverse=True)
    # pprint(basins)
    # print(basin_sizes)
    print(basin_sizes[0], basin_sizes[1], basin_sizes[2])
    print(f'Part 2: {basin_sizes[0] * basin_sizes[1] * basin_sizes[2]}')

    # Alternative approach
    # https://www.reddit.com/r/adventofcode/comments/rcjgu6/despite_having_used_python_for_years_today_was/

    # Create boolean matrix where True means it's a local minimum
    minima = ((heights < np.roll(heights, 1, 0)) &
              (heights < np.roll(heights, -1, 0)) &
              (heights < np.roll(heights, 1, 1)) &
              (heights < np.roll(heights, -1, -1)))

    print(minima)

    # Extract the values using the boolean matrix from heights
    values = np.extract(minima, heights)
    print(sum([v + 1 for v in values]))










