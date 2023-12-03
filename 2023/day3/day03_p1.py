# Day 3 - Problem 1

import re
import numpy as np

"""
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

TEST = False
NONSYMBOL = [str(i) for i in range(10)]
NONSYMBOL.append('.')

if TEST:
    data_file = 'data/input_test.txt'
else:
    data_file = 'data/input.txt'


def is_position_symbol_adjacent(schematic, row, col):
    if schematic[row - 1, col - 1] not in NONSYMBOL:
        return True
    if schematic[row - 1, col] not in NONSYMBOL:
        return True
    if schematic[row - 1, col + 1] not in NONSYMBOL:
        return True
    if schematic[row, col - 1] not in NONSYMBOL:
        return True
    if schematic[row, col + 1] not in NONSYMBOL:
        return True
    if schematic[row + 1, col] not in NONSYMBOL:
        return True
    if schematic[row + 1, col - 1] not in NONSYMBOL:
        return True
    if schematic[row + 1, col + 1] not in NONSYMBOL:
        return True

    return False

def is_number_symbol_adjacent(schematic, row, col_start, col_end):

    for j in range(col_start, col_end):
        if is_position_symbol_adjacent(schematic, row, j):
            return True

    return False


def pad(schematic, symbol='.'):
    nrows, ncols = schematic.shape
    schematic = np.insert(schematic, 0, np.full(ncols, symbol), axis=0)
    schematic = np.append(schematic, np.full((1, ncols), symbol), axis=0)
    nrows, ncols = schematic.shape
    schematic = np.insert(schematic, 0, np.full(nrows, symbol), axis=1)
    schematic = np.append(schematic, np.full((nrows, 1), symbol), axis=1)
    return schematic


possible = []
with open(data_file, 'r') as f_in:
    lines = [s.rstrip() for s in f_in.readlines()]
    # for line in lines:
    #     line.insert(0, '.')
    #     line.append('.')

schematic = np.array([[t for t in line] for line in lines])

# Pad the schematic
schematic = pad(schematic)
print(schematic.shape)

if TEST:
    for line in lines:
        print(line)
    print(schematic)
    print(NONSYMBOL)

# Iterate over lines

row = 0
adjacent_numbers = []
for line in lines:
    # Find all numbers in line as re match
    number_matches = re.finditer(r'(\d+)', line)
    for match in number_matches:
        number = match.groups(1)[0]
        symbol_adjacent = is_number_symbol_adjacent(schematic, row + 1, match.start() + 1, match.end() + 1)
        if symbol_adjacent:
            adjacent_numbers.append(int(number))
        else:
            if TEST:
                print(f'{number} is not adjacent to symbol')
    row += 1

print(f'Sum of part numbers: {sum(adjacent_numbers)}')
