# Day 14 - Extended Polymerization - Problem 1
from collections import Counter
import re
import numpy as np

test = True
if test:
    data_file = 'data/example.txt'
else:
    data_file = 'data/input.txt'

line_test = 'CH -> B'
pattern = r'(\w+)\s->\s(\w)'

insertion_pairs = {}

num_steps = 10
with open(data_file, 'r') as file_input:
    polymer_template = list(file_input.readline().rstrip())
    for line in file_input:
        line_match = re.match(pattern, line)
        if line_match:
            insertion_pairs[line_match.group(1)] = line_match.group(2)

print(polymer_template)

print(insertion_pairs)

for s in range(num_steps):
    pos = 0
    num_insertions = 0
    new_template = polymer_template.copy()
    while pos < len(new_template):
        key = ''.join(new_template[pos:pos + 2])
        if key in insertion_pairs.keys():
            char_to_insert = insertion_pairs[key]
            polymer_template.insert(pos + num_insertions + 1, char_to_insert)
            num_insertions += 1
            #print(polymer_template)

        pos += 1

    #print(f'step {s + 1} --> {"".join(polymer_template)}')

letter_counts = Counter(polymer_template)
print(letter_counts)
most_common_count = letter_counts.most_common(1)[0][1]
least_common_count = letter_counts.most_common()[-1][1]
print(most_common_count, least_common_count, most_common_count - least_common_count)