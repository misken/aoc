# Day 1 - Problem 1

test = False
if test:
    data_file = 'data/input_test_p1.txt'
else:
    data_file = 'data/input_p1.txt'

# Method 1 - line by line
previous_measurement = -1
num_increases = 0
with open(data_file, 'r') as file_input:
    for line in file_input:
        measurement = float(line)
        if measurement > previous_measurement:
            if previous_measurement > 0:
                num_increases += 1
        previous_measurement = measurement

print(f'Method 1: Line by line --> {num_increases} increases')

# Method 2 - list based
num_increases_list = 0
with open(data_file, 'r') as file_input:
    lines = file_input.readlines()
    measurements = [float(line) for line in lines]
    increases = [measurements[i] > measurements[i-1] for i in range(1,len(lines))]
    num_increases_list = sum(increases)

print(f'Method 2: list based --> {num_increases_list} increases')

