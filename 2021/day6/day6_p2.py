# Day 6 - Problem 1
import numpy as np
import collections


test = False
if test:
    data_file = 'data/input_test_p1.txt'
else:
    data_file = 'data/input_p1.txt'

end_sim = 256
with open(data_file, 'r') as file_input:
    line = file_input.readline()
    timers = line.split(',')
    timers = [int(t) for t in timers]

    ages = collections.Counter(timers)
    print(ages)

    #ages_dict = dict(ages)
    #ages_dict[0] = 0
    #print(ages_dict)

# State of system is number of fish at each timer age
for _ in range(end_sim):
    new_age_counts = collections.Counter()
    for i in range(1, 9):
        new_age_counts[i - 1] = ages[i]

    new_age_counts[8] = ages[0]
    # Cycle the 0's to 6's
    new_age_counts[6] += ages[0]

    ages = new_age_counts.copy()
    print(ages)
    print(sum(ages.values()))



#print(f'There are {len(timers)} lanternfish after {end_sim} days')








