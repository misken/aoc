# Day n - Problem 1

# Ideas from https://aoc.just2good.co.uk/2022/1 who does Python walkthroughs
# https://github.com/derailed-dash/Advent-of-Code

from pathlib import Path
import time


def main(test=False):

    if test:
        data_file = Path('data/input_test.txt')
    else:
        data_file = Path('data/input.txt')

    with open(data_file, 'r') as f_in:
        # Instead of looping, just read and split on blank lines into list
        elf_meals = f_in.read().split('\n\n')
        #print(elf_meals) # ['1000\n2000\n3000', '4000', '5000\n6000', '7000\n8000\n9000', '10000\n']

        # Use map to convert each number from str to int and use splitlnes to get numbers
        # Doing in two steps just to see that map returns an iterator
        elf_calories = [map(int, e.splitlines()) for e in elf_meals]
        tot_elf_calories = [sum(ec) for ec in elf_calories]
        max_elf_calories = max(tot_elf_calories)
        print(f'Part 1 (max calories): {max_elf_calories}')

        # Part 2 - need sum of largest three calorie values
        tot_elf_calories.sort(reverse=True)
        tot_top3 = sum(tot_elf_calories[:3])
        print(f'Part 2 (sum top 3 calories): {tot_top3}')


if __name__ == '__main__':
    test = False
    t1 = time.perf_counter()
    main(test)
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")

