# Day 6 - Problem 1

from pathlib import Path
import time

import re


def main(test=False):

    if test:
        data_file = Path('data/input_test.txt')
    else:
        data_file = Path('data/input.txt')

    window_len = 4

    with open(data_file, 'r') as f_in:
        stream = f_in.read().rstrip()

    stream_len = len(stream)

    for i in range(stream_len - window_len):
        data = stream[i:i + window_len]
        if test:
            print(data)
        if len(set(data)) == window_len:
            break

    if i < stream_len:
        print(f'Part 1: {i + window_len}')
    else:
        print('No valid data found')


if __name__ == '__main__':
    test = False
    t1 = time.perf_counter()
    main(test)
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")

