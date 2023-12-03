# Day 3 - Problem 2

# See https://github.com/st3fan/aoc/blob/master/2023/py/day3.py for a nice solution

import re
import numpy as np
import math

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


def is_position_star_adjacent(schematic, row, col):
    star_positions = [(x, y) for x in [row - 1, row, row + 1] for y in [col - 1, col, col + 1] if schematic[x, y] == '*']
    return star_positions


def is_number_star_adjacent(schematic, row, col_start, col_end):
    all_star_positions = []
    for j in range(col_start, col_end):
        star_positions = is_position_star_adjacent(schematic, row, j)
        if len(star_positions) > 0:
            all_star_positions.append(*star_positions)

    return set(all_star_positions)


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
adjacent_numbers = {}
for line in lines:
    # Find all numbers in line as re match
    number_matches = re.finditer(r'(\d+)', line)
    for match in number_matches:
        number = match.groups(1)[0]
        all_star_positions = is_number_star_adjacent(schematic, row + 1, match.start() + 1, match.end() + 1)
        if len(all_star_positions) > 0:
            print(number, all_star_positions)
            for position in all_star_positions:
                current_positions = adjacent_numbers.get(position, set())
                current_positions.add(int(number))
                adjacent_numbers[position] = current_positions

        else:
            if TEST:
                print(f'{number} is not adjacent to star')
    row += 1

total_gear_ratio = 0
for position, numbers in adjacent_numbers.items():
    if len(numbers) == 2:
        gear_ratio = math.prod(numbers)
        total_gear_ratio += gear_ratio

if TEST:
    print(adjacent_numbers)

print(f'Sum of gear ratios: {total_gear_ratio}')
