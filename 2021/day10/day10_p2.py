# Day 10 - Problem 2
import numpy as np
from collections import Counter

test = True

if test:
    data_file = 'data/example.txt'
else:
    data_file = 'data/input.txt'

with open(data_file, 'r') as file_input:
    lines = [line.rstrip() for line in file_input.readlines()]
    num_lines = len(lines)

openers = '([{<'
closers = ')]}>'
which_opener = {')': '(', ']': '[', '}': '{', '>': '<'}
which_closer = {v : k for k, v in which_opener.items()}
nbad = Counter({')': 0, ']': 0, '}': 0, '>': 0})
value_bad = {')': 3, ']': 57, '}': 1197, '>': 25137}
value_complete = {')': 1, ']': 2, '}': 3, '>': 4}

line_num = 0

completers_list = []
for line in lines:
    ignore = False
    chars = []
    for c in line:
        if c in openers:
            chars.append(c)
        elif c in closers:
            # If it's a closer, the last item in the chars list must be matching opener
            if chars[-1] != which_opener[c]:
                # Tried to close something that wasn't open
                nbad[c] += 1
                ignore = True
                break  # Stop reading this line
            else:
                # remove last item from list
                chars.pop()
        else:
            print(f'illegal char {c}')
            print(f'{line_num}: {line}')
            exit()

    if not ignore:
        # chars should contain the incomplete line with previously closed pairs removed
        completers = []
        while len(chars) > 0:
            completers.append(which_closer[chars[-1]])
            chars.pop()

        completers_list.append(completers)

    line_num += 1

# Part 1 - Compute bad value score
tot_value_bad = sum([value_bad[k] * nbad[k] for k in nbad])
print(f'Part 1 - tot_value_bad: {tot_value_bad}')

# Part 2 - Compute final autocompleter score
scores = []
for row in completers_list:
    score = 0
    for c in row:
        score = 5 * score + value_complete[c]
    scores.append(score)

middle_score = np.median(scores)
print(f'Part 2 - middle_score: {middle_score}')










