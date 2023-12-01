# Day 8 - Problem 1
import numpy as np


test = False

if test:
    data_file = 'data/example.txt'
else:
    data_file = 'data/input.txt'

num_unique = 0
with open(data_file, 'r') as file_input:
    for line in file_input:
        sig_out = line.split('|')
        signals = sig_out[0].strip().split(' ')
        outputs = sig_out[1].strip().split(' ')

        # How many outputs have length 2, 3, 4, or 7
        new_unique = sum([len(s) in [2, 3, 4, 7] for s in outputs])
        num_unique += new_unique
        # print(new_unique, num_unique)
        #
        # print(signals)
        # print(outputs)

print(num_unique)







