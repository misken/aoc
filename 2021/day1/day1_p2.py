# Day 1 - Problem 2

test = False
if test:
    data_file = 'data/input_test_p1.txt'
else:
    data_file = 'data/input_p1.txt'

# Method 2 - list based
num_increases_list = 0
window_size = 3
with open(data_file, 'r') as file_input:
    lines = file_input.readlines()
    num_lines = len(lines)
    measurements = [float(line) for line in lines]
    sliding_windows = [[measurements[i + j] for j in range(0, window_size)]
                       for i in range(0, num_lines - window_size + 1)]
    increases = [sum(sliding_windows[i]) > sum(sliding_windows[i-1]) for i in range(1, len(sliding_windows))]
    num_increases_list = sum(increases)
    if test:
        print(sliding_windows)

print(f'Method 2: list based --> {num_increases_list} increases')