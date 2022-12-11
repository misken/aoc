# --- Day 10: Cathode-Ray Tube --- Part 2

from pathlib import Path
import time

import numpy as np
import matplotlib.pyplot as plt

def draw_advance_crt(sprite_pos, crt_pos, crt):
    xpos = crt_pos[1]
    if xpos in sprite_pos:
        crt[crt_pos[0], crt_pos[1]] = '#'
    else:
        crt[crt_pos[0], crt_pos[1]] = '.'

    if xpos == 39:
        crt_pos = (crt_pos[0] + 1, 0)
    else:
        crt_pos = (crt_pos[0], crt_pos[1] + 1)

    return crt_pos


def update_sprite_pos(sprite_pos, xval_after):
    sprite_pos[0] = xval_after[-1] - 1
    sprite_pos[1] = xval_after[-1]
    sprite_pos[2] = xval_after[-1] + 1
    return sprite_pos

def crt_tostring(crt):
    rows = []


def main(test=False):

    if test:
        data_file = Path('data/input_test.txt')
    else:
        data_file = Path('data/input.txt')

    cycles = {'noop': 1, 'addx': 2}
    xval = [1] # Starting register value
    xval_after = [1]
    sprite_pos = np.array([0, 1, 2])

    crt = np.empty((6, 40), dtype=str)
    crt_pos = (0, 0)

    with open(data_file, 'r') as f_in:
        commands = [m.rstrip() for m in f_in.readlines()]

    cur_cycle = 1
    for cmd in commands:
        if cmd == 'noop':
            xval.append(xval_after[cur_cycle - 1])
            crt_pos = draw_advance_crt(sprite_pos, crt_pos, crt)
            xval_after.append(xval[cur_cycle])
            cur_cycle += 1

            if test:
                print(cur_cycle)

        else:
            xinc = int(cmd.split()[1])
            xval.append(xval_after[cur_cycle - 1])
            crt_pos = draw_advance_crt(sprite_pos, crt_pos, crt)
            xval_after.append(xval[cur_cycle])
            cur_cycle += 1
            xval.append(xval_after[cur_cycle - 1])
            crt_pos = draw_advance_crt(sprite_pos, crt_pos, crt)
            xval_after.append(xval[cur_cycle] + xinc)
            sprite_pos = update_sprite_pos(sprite_pos, xval_after)
            cur_cycle += 1

    signal_strengths = [xval[c] * c for c in range(20, 221, 40)]
    if test:
        print([xval[c] for c in range(20, 221, 40)])
        print([xval[c] for c in range(25)])
    if test:
        print(signal_strengths)

    tot_signal_strength = sum(signal_strengths)


    print(f'Part 2 (tot_signal_strength): {tot_signal_strength}')

    for i in range(6):
        for j in range(40):
            print(crt[i, j], end='')
        print()
    # FGCUZREC
    #plt.matshow(crt)




if __name__ == '__main__':
    test = False
    t1 = time.perf_counter()
    main(test)
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")

