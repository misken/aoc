# Day 5 - Problem 1
import numpy as np
import pandas as pd
import re

test = False
if test:
    data_file = 'data/input_test_p1.txt'
    field_matrix = np.zeros((10, 10))
else:
    data_file = 'data/input_p1.txt'
    field_matrix = np.zeros((1000, 1000))

line_test = '1,1 -> 1,3'
pattern = r'(\d+),(\d+)\s->\s(\d+),(\d+)'



with open(data_file, 'r') as file_input:
    for line in file_input:
        line_match = re.match(pattern, line)
        if line_match:
            x1 = int(line_match.group(1))
            y1 = int(line_match.group(2))
            x2 = int(line_match.group(3))
            y2 = int(line_match.group(4))

            #print(f'({x1}, {y1})({x2}, {y2})')

            # Check if horizontal or vertical
            if x1 == x2 or y1 == y2:
                if x1 > x2:
                    x_range = range(x1, x2 - 1, -1)
                else:
                    x_range = range(x1, x2 + 1, 1)
                if y1 > y2:
                    y_range = range(y1, y2 - 1, -1)
                else:
                    y_range = range(y1, y2 + 1, 1)

                for x in x_range:
                    for y in y_range:
                        field_matrix[y, x] = field_matrix[y, x] + 1
                        #print(field_matrix)

print(field_matrix)
print(sum(sum(field_matrix >= 2)))







