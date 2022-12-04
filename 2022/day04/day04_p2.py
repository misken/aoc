# Day 4 - Problem 2

from pathlib import Path
import time


def main(test=False):
    if test:
        data_file = Path('data/input_test.txt')
    else:
        data_file = Path('data/input.txt')

    elf_pairs = []
    with open(data_file, 'r') as f_in:
        for line in f_in:
            raw_assignments = line.split(',')
            elf_sets = []
            for a in raw_assignments:
                a_list = list(map(int, a.split('-')))
                a_set = set(range(a_list[0], a_list[1] + 1))
                elf_sets.append(a_set)

            elf_pairs.append(elf_sets)

        num_overlaps = 0
        for elf_pair in elf_pairs:
            if len(elf_pair[0].intersection(elf_pair[1])) > 0:
                num_overlaps += 1

    if test:
        print(elf_pairs)

    print(f'Part 1 (num_overlaps): {num_overlaps}')


if __name__ == '__main__':
    test = False
    t1 = time.perf_counter()
    main(test)
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")

