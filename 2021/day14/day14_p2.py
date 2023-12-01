# Day 14 - Extended Polymerization - Problem 2
from collections import Counter
import re

test = False
if test:
    data_file = 'data/example.txt'
else:
    data_file = 'data/input.txt'

pattern = r'(\w+)\s->\s(\w)'
insertion_pairs = {}

num_steps = 40
with open(data_file, 'r') as file_input:
    polymer_template = list(file_input.readline().rstrip())
    for line in file_input:
        line_match = re.match(pattern, line)
        if line_match:
            insertion_pairs[line_match.group(1)] = line_match.group(2)

# Create initial pair counter
pair_counter = Counter([polymer_template[i] + polymer_template[i + 1] for i in range(len(polymer_template) - 1)])
# Create initial letter counter
letter_counts = Counter(polymer_template)

for s in range(num_steps):
    new_pair_counter = pair_counter.copy()
    for key in pair_counter:
        if key in insertion_pairs.keys():
            new_key_found = True
            char_to_insert = insertion_pairs[key]
            new_key_1 = key[0] + char_to_insert
            new_key_2 = char_to_insert + key[1]
            new_pair_counter[key] -= pair_counter[key]
            new_pair_counter[new_key_1] += pair_counter[key]
            new_pair_counter[new_key_2] += pair_counter[key]
            letter_counts[char_to_insert] += pair_counter[key]

    pair_counter = new_pair_counter.copy()

most_common_count = letter_counts.most_common(1)[0][1]
least_common_count = letter_counts.most_common()[-1][1]
print(most_common_count, least_common_count, most_common_count - least_common_count)

