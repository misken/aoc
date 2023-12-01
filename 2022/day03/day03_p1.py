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

        # Split into compartments
        priorities = []
        for r in rucksacks:
            num_items = int(len(r)/2)
            compartments = (r[:num_items], r[num_items:])

            # Use set intersection to find common item
            common_item = set(compartments[0]).intersection(set(compartments[1]))
            for item in common_item:
                priority = get_priority(item)
                priorities.append(priority)
                tot_priority = sum(priorities)

        if test:
            print(priorities)


        print(f'Part 1 (tot_score): {tot_priority}')


if __name__ == '__main__':
    test = False
    t1 = time.perf_counter()
    main(test)
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")

