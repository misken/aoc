# --- Day 9: Rope Bridge --- Part 1

from pathlib import Path
import time
from enum import Enum
import numpy as np
import math

class Direction(Enum):
    L = -1
    R = 1
    U = 1
    D = -1


def move_head(head_pos, head_move):

    new_head_pos = (head_pos[0] + head_move[0], head_pos[1] + head_move[1])
    return new_head_pos

def move_tail(head_pos, tail_pos):

    dist_to_head_x = head_pos[0] - tail_pos[0]
    dist_to_head_y = head_pos[1] - tail_pos[1]

    sign_to_head_x = np.sign(dist_to_head_x)
    sign_to_head_y = np.sign(dist_to_head_y)

    absdist_to_head_x = abs(dist_to_head_x)
    absdist_to_head_y = abs(dist_to_head_y)

    if head_pos[1] == tail_pos[1] and absdist_to_head_x > 1:
        tail_move_x = sign_to_head_x
        tail_move_y = 0
    elif head_pos[0] == tail_pos[0] and absdist_to_head_y > 1:
        tail_move_y = sign_to_head_y
        tail_move_x = 0
    elif not are_neighbors(head_pos[0], head_pos[1], tail_pos[0], tail_pos[1]):
        tail_move_x = sign_to_head_x
        tail_move_y = sign_to_head_y
    else:
        tail_move_y = 0
        tail_move_x = 0

    new_tail_pos = (tail_pos[0] + tail_move_x, tail_pos[1] + tail_move_y)
    return new_tail_pos

def are_neighbors(head_x, head_y, tail_x, tail_y):

    if abs(head_x - tail_x) <= 1 and abs(head_y - tail_y) <= 1:
        return True
    else:
        return False


def main(test=False):

    if test:
        data_file = Path('data/input_test.txt')
    else:
        data_file = Path('data/input.txt')

    with open(data_file, 'r') as f_in:
        moves = [m.rstrip().split() for m in f_in.readlines()]
        moves = [(m[0], int(m[1])) for m in moves]
        if test:
            print(moves)

    head_pos = (0, 0)
    tail_pos = (0, 0)
    direction = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}
    tail_positions = set()

    for dir, steps in moves:
        if test:
            print(head_pos)

        for step in range(steps):
            head_pos = move_head(head_pos, direction[dir])
            tail_pos = move_tail(head_pos, tail_pos)
            tail_positions.add(tail_pos)

            if test:
                print(head_pos, tail_pos)


    if test:
        print(tail_positions)

    print(f'Part 1 (number of tail positions: {len(tail_positions)}')




if __name__ == '__main__':
    test = False
    t1 = time.perf_counter()
    main(test)
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")

