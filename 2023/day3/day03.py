# Day 3 - Problems 1 and 2

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

NONSYMBOL = [str(i) for i in range(10)]
NONSYMBOL.append('.')


def is_position_symbol_adjacent(schematic, rownum, colnum):
    # Will keep all in case needed for part 2
    symbol_positions = [(x, y) for x in range(rownum - 1, rownum + 2) for y in range(colnum - 1, colnum + 2) if
                        schematic[x, y] not in NONSYMBOL]
    return symbol_positions


def is_number_symbol_adjacent(schematic, row, col_start, col_end):
    for j in range(col_start, col_end):
        if len(is_position_symbol_adjacent(schematic, row, j)) > 0:
            return True

    return False


def is_position_star_adjacent(schematic, row, col):
    star_positions = [(x, y) for x in [row - 1, row, row + 1] for y in [col - 1, col, col + 1] if
                      schematic[x, y] == '*']
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
    schematic = np.insert(schematic, 0, np.full(nrows + 2, symbol), axis=1)
    schematic = np.append(schematic, np.full((nrows + 2, 1), symbol), axis=1)
    return schematic


def day3_p1(data):
    with open(data, 'r') as f_in:
        lines = [s.rstrip() for s in f_in.readlines()]

    # Store schematic in numpy array
    schematic = np.array([[t for t in line] for line in lines])

    # Pad the schematic with dots all around to avoid bad indexing
    schematic = pad(schematic)

    # Iterate over lines
    adjacent_numbers = []
    for row, line in enumerate(lines):
        # Find all numbers in line as re match
        number_matches = re.finditer(r'(\d+)', line)
        for match in number_matches:
            number = match.group(1)
            symbol_adjacent = is_number_symbol_adjacent(schematic, row + 1, match.start() + 1, match.end() + 1)
            if symbol_adjacent:
                adjacent_numbers.append(int(number))

    print(f'Sum of part numbers: {sum(adjacent_numbers)}')


def day3_p2(data, test=False):
    with open(data, 'r') as f_in:
        lines = [s.rstrip() for s in f_in.readlines()]

    schematic = np.array([[t for t in line] for line in lines])
    schematic = pad(schematic)

    # Iterate over lines
    adjacent_numbers = {}
    for row, line in enumerate(lines):
        # Find all numbers in line as re match
        number_matches = re.finditer(r'(\d+)', line)
        for match in number_matches:
            number = match.group(1)
            all_star_positions = is_number_star_adjacent(schematic, row + 1, match.start() + 1, match.end() + 1)
            if len(all_star_positions) > 0:
                for position in all_star_positions:
                    current_positions = adjacent_numbers.get(position, set())
                    current_positions.add(int(number))
                    adjacent_numbers[position] = current_positions

    total_gear_ratio = 0
    for position, numbers in adjacent_numbers.items():
        if len(numbers) == 2:
            gear_ratio = math.prod(numbers)
            total_gear_ratio += gear_ratio

    print(f'Sum of gear ratios: {total_gear_ratio}')


def main():
    TEST = False
    if TEST:
        data_file = 'data/input_test.txt'
    else:
        data_file = 'data/input.txt'

    day3_p1(data_file)
    day3_p2(data_file)


if __name__ == '__main__':
    main()
