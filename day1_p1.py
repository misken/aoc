import numpy as np
import pandas as pd
import re

data = np.loadtxt('day1/input')

# Find the pair of numbers
pairs = [(a, b) for a in data for b in data if a <= b and a + b == 2020]
print(pairs)
# Multiply the two numbers
print(pairs[0][0] * pairs[0][1])