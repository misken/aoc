# Day 17: Trick shot  - Problem 1
import numpy as np
import re


"""
Trajectory problem
"""



test = True

if test:
    data_file = f'data/example.txt'
else:
    data_file = 'data/input.txt'

def step(x, y, vx, vy):

    # Position change
    x += vx
    y += vy

    # Drag
    if vx > 0:
        vx -= 1
    elif vx < 0:
        vx += 1

    # Gravity
    vy -= 1

    return x, y, vx, vy

def in_target(x, y, x1, y1, x2, y2):
    if x in range(x1, x2 + 1) and y in range(y1, y2 + 1):
        return True
    else:
        return False



with open(data_file, 'r') as file_input:
    # Read target coordinates
    # target area: x=20..30, y=-10..-5
    line = file_input.readline()
    pattern = r'target area: x=([-]*\d+)\.\.([-]*\d+), y=([-]*\d+)\.\.([-]*\d+)'
    match = re.match(pattern, line)
    if match:
        x1 = int(match.group(1))
        x2 = int(match.group(2))
        y1 = int(match.group(3))
        y2 = int(match.group(4))

    print(x1, x2, y1, y2)
    height = np.zeros((1000, 1000))

    # Just brute force search to start
    s = 0
    for i in range(7, 8):
        for j in range(-1, 0):
            # x, y, vx, vy
            x, y = 0, 0
            maxy = y
            vx_start, vy_start = i, j

            vx = vx_start
            vy = vy_start

            while y >= y1:
                x, y, vx, vy = step(x, y, vx, vy)
                s += 1
                if y > maxy:
                    maxy = y
                print(x, y, vx, vy)
                if in_target(x, y, x1, y1, x2, y2):
                    print(f'({vx_start, vy_start}) In target after step {s + 1}. Max height was {maxy}')
                    height[vx_start, vy_start] = maxy


    print(np.max(height))
    print(np.unravel_index(height.argmax(), height.shape))