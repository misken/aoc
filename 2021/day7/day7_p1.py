# Day 7 - Problem 1
import numpy as np
import math


test = False
if test:
    data_file = 'data/input_test_p1.txt'
else:
    data_file = 'data/input_p1.txt'

# 16,1,2,0,4,2,7,1,2,14
# Need to find alignment position that minimizes sum of abs differences
# between alignment position and individual positions

# - could brute force search
# - formulate as optimization problem

with open(data_file, 'r') as file_input:
    line = file_input.readline()
    positions = line.split(',')
    positions = np.array([int(t) for t in positions])
    print(positions)
    print(np.mean(positions))

    min_position = np.min(positions)
    max_position = np.max(positions)

fuel_used = {}
min_fuel_use = 100000000
optimal_position = 0
for i in range(min_position, max_position):
    fuel_used[i] = sum(abs(positions - i))
    if fuel_used[i] < min_fuel_use:
        min_fuel_use = fuel_used[i]
        optimal_position = i

print(f'Position {optimal_position} uses {min_fuel_use} fuel units')


