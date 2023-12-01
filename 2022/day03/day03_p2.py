# Day 2 - Problem 1

from pathlib import Path
import time


def get_priority(item):

    if ord(item) >= ord('a'):
        return ord(item) - 96
    else:
        return ord(item) - 64 + 26

def main(test=False):

    if test:
        data_file = Path('data/input_test.txt')
    else:
        data_file = Path('data/input.txt')

    with open(data_file, 'r') as f_in:
        rucksacks = [r.strip() for r in f_in.readlines()]
        num_groups = len(rucksacks) // 3

        # Split into compartments
        priorities = []
        for group in range(num_groups):

            group = [set(rucksacks[e]) for e in range(3 * (group + 1) - 3, 3 * (group + 1))]

            # Use set intersection to find common item
            common_item = set.intersection(*group).pop()
            priority = get_priority(common_item)
            priorities.append(priority)
            tot_priority = sum(priorities)

        if test:
            print(group)


        print(f'Part 1 (tot_score): {tot_priority}')


if __name__ == '__main__':
    test = False
    t1 = time.perf_counter()
    main(test)
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")

