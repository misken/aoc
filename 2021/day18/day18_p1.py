# Day 18: Snailfish  - Problem 1
import numpy as np
import re
import math


"""
Trajectory problem
"""

test = True

if test:

    data_file = f'data/example_00.txt'

else:
    data_file = 'data/input.txt'


def add_sf(_sf1, _sf2):
    return f'[{sf1},{sf2}]'


def regular_pair_magnitude(pair_tuple):

    return 3 * pair_tuple[0] + 2 * pair_tuple[1]


def exploder(_sf_sum, test=False):

    if test:
        _sf_sum = '[[[[[9,8],1],2],3],4]'
        _sf_sum = '[7,[6,[5,[4,[3,2]]]]]'
        _sf_sum = '[[6,[5,[4,[3,2]]]],1]'

    _pattern = r'(\d+),(\d+)\]'

    balance = 0
    pos = 0
    need_to_explode = False
    for s in _sf_sum:
        if s == '[':
            balance += 1
            if balance == 5:
                e1_pos = pos + 1
                need_to_explode = True
                break
        elif s == ']':
            balance -= 1
        pos += 1

    #ex_match = re.search(_pattern, _sf_sum)
    if need_to_explode:
        print(f'need to explode {_sf_sum} at {pos + 1}')

        ex_match = re.search(_pattern, _sf_sum[pos:])
        # Get capture groups
        e1 = int(ex_match.group(1))
        e2 = int(ex_match.group(2))
        print(e1, e2)

        e1_pos = pos + ex_match.start(1)
        e2_pos = pos + ex_match.end(2)

        # Find left number
        left_match = re.search(r'(\d+)(?!.*\d+)', _sf_sum[:e1_pos])
        #left_match = re.findall(r'(\d+)', _sf_sum[:e1_pos])
        left_num_span = None
        if left_match:
            # Found a left number
            left_num_span = left_match.span(1)
            left_num = int(left_match.group(1))
            print(f'left num {left_num} at {left_num_span}')

            new_left_num = left_num + e1

        # Find right number
        # left_match = re.match(r'(\d+)?!.*\d+', _sf_sum[:e1_pos])
        right_match = re.search(r'(\d+)', _sf_sum[e2_pos + 1:])
        right_num_span = None
        if right_match:
            # Found a right number
            right_num_span = right_match.span(1)
            right_num = int(right_match.group(1))
            right_num_pos = e2_pos + 1 + right_num_span[0]
            print(f'right num {right_num} at {right_num_span}')

            new_right_num = right_num + e2

        # Create the pieces to rebuild the exploded string
        if left_match:
            start_piece = _sf_sum[:left_num_span[0]]
            left_number_piece = str(new_left_num)
            left_num_to_exp_piece = _sf_sum[left_num_span[1]:e1_pos - 1]
        else:
            start_piece = _sf_sum[:e1_pos - 1]
            left_number_piece = ''
            left_num_to_exp_piece = ''

        exploded_pair = '0'

        if right_match:
            exp_to_right_num_piece = _sf_sum[e2_pos + 1:right_num_pos]
            right_number_piece = str(new_right_num)
            end_piece = _sf_sum[right_num_pos + 1:]
        else:
            exp_to_right_num_piece = ''
            right_number_piece = ''
            end_piece = _sf_sum[e2_pos + 1:]

        exploded_string = start_piece + left_number_piece + left_num_to_exp_piece + exploded_pair + \
                          exp_to_right_num_piece + right_number_piece + end_piece

    else:
        exploded_string = _sf_sum

    print(exploded_string)
    print(exploded_string == _sf_sum)
    return exploded_string


def splitter(_sf_sum, test=False):

    if test:
        _sf_sum = '[[[[9,8],10],2],3]'

    _pattern = r'(\d{2,})'

    ex_match = re.search(_pattern, _sf_sum)
    if ex_match:
        print(f'matched {_sf_sum}')
        print(ex_match)

        # Get capture group
        e1 = int(ex_match.group(1))

        print(e1)

        e1_span = ex_match.span(1)

        new_e1_1 = math.floor(e1 / 2)
        new_e1_2 = math.ceil(e1 / 2)

                # Create the pieces to rebuild the exploded string

        start_piece = _sf_sum[:e1_span[0]]

        split_element = f'[{str(new_e1_1)},{str(new_e1_2)}]'

        end_start = e1_span[0] + len(str(e1))
        end_piece = _sf_sum[end_start:]

        split_string = start_piece + split_element + end_piece

    else:
        split_string = _sf_sum

    print(split_string)
    print(split_string == _sf_sum)
    return split_string


with open(data_file, 'r') as file_input:

    lines = [line.rstrip() for line in file_input.readlines()]

    sf1_idx = 0
    sf1 = lines[sf1_idx]
    print(sf1)
    while sf1_idx < len(lines) - 1:

        sf2 = lines[sf1_idx + 1]
        print(sf2)
        sf_sum = add_sf(sf1, sf2)
        print(sf_sum)
        sf1 = sf_sum
        sf1_idx += 1

        # Reduce
        reduced = False
        while not reduced:
            sf_sum_post_ex = exploder(sf_sum, test=False)
            if sf_sum_post_ex == sf_sum: # No explosions
                sf_sum_post_split = splitter(sf_sum, test=False)
                if sf_sum_post_split == sf_sum:  # No splits or explosions
                    reduced = True
                else:
                    sf_sum = sf_sum_post_split
                    reduced = False
            else:
                reduced = False
                sf_sum = sf_sum_post_ex

        print(sf_sum)


        # # Find all the pairs
        # pair_pattern = r'\[(\d+),(\d+)\]'
        # all_pairs = re.findall(pair_pattern, sf_sum)
        # print(all_pairs)
        #
        # all_pairs_tuple = [(int(e1), int(e2)) for e1, e2 in all_pairs]
        # print(all_pairs_tuple)
        #
        # all_pair_magnitudes = [pair_magnitude(t) for t in all_pairs_tuple]
        # print(all_pair_magnitudes)
        #
        # # Find all the left regular numbers
        # left_regular = r'\[(\d+),\['
        # all_left_regular = re.findall(left_regular, sf_sum)
        # print(all_left_regular)
        #
        # left_regular = [int(e1) for e1 in all_left_regular]
        # print(left_regular)
        #
        # right_regular = r'],(\d+)\]'
        # all_right_regular = re.findall(right_regular, sf_sum)
        # print(all_right_regular)
        #
        # right_regular = [int(e1) for e1 in all_right_regular]
        # print(right_regular)
        #
        # final_sum = sum(all_pair_magnitudes) + sum(left_regular) + sum(right_regular)
        # print(final_sum)






