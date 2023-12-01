# Day 1 - Problem 1 and 2

import re


def day01_p1(test=False):
    if test:
        data_file = 'data/input_test.txt'
    else:
        data_file = 'data/input.txt'

    with open(data_file, 'r') as f_in:
        calibrations = [s.rstrip() for s in f_in.readlines()]

    values = []
    for c in calibrations:
        # find leftmost digit
        left_val = re.search('(\d)', c).group(1)
        right_val = re.search('(\d)', c[::-1]).group(1)

        val = int(f'{left_val}{right_val}')
        if test:
            print(val)
        values.append(val)

    print(f'Problem 1 total: {sum(values)}')


def day01_p2(test=False):
    if test:
        data_file = 'data/input_test_p2.txt'
    else:
        data_file = 'data/input.txt'

    with open(data_file, 'r') as f_in:
        calibrations = [s.rstrip() for s in f_in.readlines()]

    # Create token value dictionaries
    num_str_vals = {str(i): i for i in range(1, 10)}
    name_vals = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    name_vals = name_vals | num_str_vals
    name_rev_vals = {'eno': 1, 'owt': 2, 'eerht': 3, 'ruof': 4, 'evif': 5, 'xis': 6, 'neves': 7, 'thgie': 8, 'enin': 9}
    name_rev_vals = name_rev_vals | num_str_vals

    # Create regular expressions
    re_valnames = "|".join(name_vals.keys())
    re_valnames_rev = "|".join(name_rev_vals.keys())

    values = []
    for c in calibrations:
        left_val = name_vals[re.search(f'({re_valnames})', c).group(0)]
        right_val = name_rev_vals[re.search(f'({re_valnames_rev})', c[::-1]).group(0)]
        val = int(f'{left_val}{right_val}')
        values.append(val)

    print(f'Problem 2 total: {sum(values)}')


if __name__ == '__main__':
    day01_p1()
    day01_p2()
