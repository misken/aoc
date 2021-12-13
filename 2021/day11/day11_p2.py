# Day 11 - Problem 1
import numpy as np
from collections import Counter

test = False

if test:
    data_file = 'data/example.txt'
else:
    data_file = 'data/input.txt'


def adjacent(i, j):
    """

    :param i:
    :param j:
    :return:
    """

    adj = []

    north = i - 1, j
    northwest = i - 1, j - 1
    northeast = i - 1, j + 1
    south = i + 1, j
    west = i, j - 1
    east = i, j + 1
    southwest = i + 1, j - 1
    southeast = i + 1, j + 1

    adj.extend([north, northwest, northeast,
                east, west,
                south, southwest, southeast])

    return adj


# Read array of energy
energy = np.array(np.genfromtxt(data_file, delimiter=1, dtype=np.int32))
# Pad the array with -Inf s to make edge cases easier
energy = np.pad(energy, 1, 'constant', constant_values=np.iinfo(np.int32).min)
flashed = energy.copy()
flashed = False


nrows = energy.shape[0]
ncols = energy.shape[1]

num_steps = 10000
num_flashes = 0
num_flashes_sum = 0


for step in range(num_steps):
    # Increase energy level by 1
    energy += 1
    # Check for flashes
    flashed = energy == 10
    newly_flashed = list(np.argwhere(energy == 10))
    num_flashes += len(newly_flashed)

    # Process the newly flashed
    while len(newly_flashed) > 0:
        dumbo_i, dumbo_j = newly_flashed.pop()
        adj = adjacent(dumbo_i, dumbo_j)
        for (i, j) in adj:
            energy[i, j] += 1
            if energy[i, j] == 10:
                newly_flashed.append(np.array([i, j]))
                num_flashes += 1
                flashed[i, j] = True

    # Reset all flashed dumbos to 0
    energy[flashed] = 0
    num_flashes_sum += np.sum(energy == 0)
    if np.all(flashed[1:-1, 1:-1]):
        print(f'All flashed on step {step + 1}')
        break

    # if step in (193, 194, 195, 196):
    #     print(f'Step {step + 1}')
    #     print(energy[1:-1, 1:-1])


    flashed = False
    # print(f'Step {step + 1}')
    # print(energy[1:-1, 1:-1])

print(f'{num_flashes} after {num_steps} steps')
print(f'{num_flashes_sum} after {num_steps} steps')














