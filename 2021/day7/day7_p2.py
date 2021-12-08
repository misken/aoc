# Day 7 - Problem 2
import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt

from scipy.optimize import minimize_scalar

brute_force = True
test = True
if test:
    data_file = 'data/input_test_p1.txt'
else:
    data_file = 'data/input_p1.txt'



# 16,1,2,0,4,2,7,1,2,14
# Need to find alignment position that minimizes a function of the sum of abs differences
# Each step costs one more unit than the previous step.
# To from from 2 to 5 = 1 + 2 + 3 = 6 fuel units
# It's the sum of the integers from 1:abs(difference)

# Seems like the optimal position should be around the mean


def compute_fuel_cost(difference):
    total_cost = sum([i for i in range(1, abs(int(difference)) + 1)])
    return total_cost

with open(data_file, 'r') as file_input:
    line = file_input.readline()
    positions = line.split(',')
    positions = np.array([int(t) for t in positions])
    #print(positions)
    print(np.mean(positions))

    min_position = np.min(positions)
    max_position = np.max(positions)

if brute_force:
    fuel_used = {}
    min_fuel_use = 100000000
    optimal_position = 0
    for p in range(min_position, max_position):
        tot_cost = 0
        for c in positions:
            tot_cost += compute_fuel_cost((c - p))

        fuel_used[p] = tot_cost
        if fuel_used[p] < min_fuel_use:
            min_fuel_use = fuel_used[p]
            optimal_position = p

    print(f'Position {optimal_position} uses {min_fuel_use} fuel units')

    with open('fuel_used.csv', 'w') as f:
        w = csv.writer(f)
        w.writerows(fuel_used.items())

    fuel_used_df = pd.DataFrame.from_dict(fuel_used, orient='index', columns=['fuel_use'])
    fuel_used_df.reset_index(inplace=True, drop=False)

    plt.scatter(fuel_used_df['index'], fuel_used_df['fuel_use'])
    plt.show()

else:
    optimal_position = minimize_scalar(compute_fuel_cost, bracket=[min_position, max_position])
    print(optimal_position.x)



