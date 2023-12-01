# Day 6 - Problem 1
import numpy as np


test = True
if test:
    data_file = 'data/input_test_p1.txt'
else:
    data_file = 'data/input_p1.txt'

end_sim = 80
with open(data_file, 'r') as file_input:
    line = file_input.readline()
    timers = line.split(',')
    timers = [int(t) for t in timers]


for _ in range(end_sim):
    #timers_now = timers.copy()
    #timers = []
    # Hmm, can we append on the fly to timers and avoid copying the list?
    num_new_fish = 0
    for i in range(len(timers)):
        if timers[i] == 0:
            timers[i] = 6
            num_new_fish += 1
        else:
            timers[i] -= 1

    # new lanternfish
    new_timers = [8] * num_new_fish

    # Append the new fish
    timers.extend(new_timers)
    print(len(timers))

print(f'There are {len(timers)} lanternfish after {end_sim} days')








