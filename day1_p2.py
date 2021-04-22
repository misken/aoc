import numpy as np
import pandas as pd
import re

data = np.loadtxt('day1/input')

# Find the pair of numbers
trips = [(a, b, c) for a in data for b in data for c in data if a <= b <= c and a + b + c == 2020]
print(trips)
# Multiply the two numbers
print(trips[0][0] * trips[0][1] * trips[0][2])