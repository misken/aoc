# Day 10 - Problem 1
import numpy as np
from collections import Counter
from pprint import pprint

test = False

if test:
    data_file = 'data/example.txt'
else:
    data_file = 'data/input.txt'


with open(data_file, 'r') as file_input:
    lines = [line.rstrip() for line in file_input.readlines()]
    num_lines = len(lines)
    # print(lines)
    # print(num_lines)

openers = '([{<'
closers = ')]}>'
which_opener = {')': '(', ']': '[', '}': '{', '>': '<'}

value_bad = {')': 3, ']': 57, '}': 1197, '>': 25137}

tot_openers = Counter({'(': 0, '[': 0, '{': 0, '<': 0})
tot_closers = Counter({')': 0, ']': 0, '}': 0, '>': 0})

nopen = Counter({'(': 0, '[': 0, '{': 0, '<': 0})
nbad = Counter({')': 0, ']': 0, '}': 0, '>': 0})

line_num = 0
for line in lines:
    chars = []
    nopen.clear()
    for c in line:
        if c in openers:
            nopen[c] += 1
            tot_openers[c] += 1
            chars.append(c)
        elif c in closers:
            # If it's a closer, the last item in the chars list must be matching opener
            if chars[-1] != which_opener[c]:
                # Tried to close something that wasn't open
                nbad[c] += 1
                print(f'bad {c} in line {line_num}: {line}')
                break # Stop reading this line
            else:
                tot_closers[c] += 1
                nopen[which_opener[c]] -= 1
                # remove last item from list
                chars = chars[:-1]
        else:
            print(f'illegal char {c}')
            print(f'{line_num}: {line}')
            exit()

    line_num += 1
    #print(f'tot_openers is {tot_openers}')
    #print(f'tot_closers is {tot_closers}')

print(f'number bad: {nbad}')

tot_value_bad = sum([value_bad[k] * nbad[k] for k in nbad])
print(f'tot_value_bad: {tot_value_bad}')









