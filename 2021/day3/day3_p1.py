# Day 3 - Problem 1
import numpy as np

test = False
if test:
    data_file = 'data/input_test_p1.txt'
else:
    data_file = 'data/input_p1.txt'

# Method 1 - list of lists

with open(data_file, 'r') as file_input:
    lines = file_input.readlines()
    lines = [line.rstrip() for line in lines]
    num_lines = len(lines)
    codelen = len(lines[0])

    counts = []
    for i in range(codelen):
        num_ones = sum([int(line[i]) for line in lines])
        counts.append(num_ones)

    gamma_string = ''.join([str(int(round(count / num_lines))) for count in counts])
    epsilon_string = ''.join([str(abs(int(s) - 1)) for s in gamma_string])

    gamma = int(gamma_string, 2)
    epsilon = int(epsilon_string, 2)

    #print(counts)
    #print([count / num_lines for count in counts])
    #print([int(round(count / num_lines)) for count in counts])
    print(gamma_string)
    print(epsilon_string)
    print(gamma, epsilon, gamma * epsilon)



