# Day n - Problem 2

from pathlib import Path
import time

import re


def main(test=False):
    if test:
        data_file = Path('data/input_test.txt')
    else:
        data_file = Path('data/input.txt')

    # Read the two separate sections into a list as big strings
    with open(data_file, 'r') as f_in:
        sections = f_in.read().split('\n\n')

    # Split the strings on the newline
    stacks_sec = sections[0].splitlines()
    recipes_sec = sections[1].splitlines()

    # Get each move line as a list of strings
    recipes = []
    for r in recipes_sec:
        new_recipe = [m.strip() for m in r.split()]
        recipes.append(new_recipe)

    # Grab the ints specifying how many, from, and to for the move
    moves = [(int(r[1]), int(r[3]), int(r[5])) for r in recipes if len(r) > 5]

    # Determine number of stacks (assuming stacks are sequentially labeled starting with 1
    stack_nums = [int(n) for n in stacks_sec[-1].split()]
    num_stacks = max(stack_nums)

    # Initialize the stacks by filling and then reversing
    stacks = [[] for _ in range(num_stacks)] # Empty stacks to start
    for row in stacks_sec[:-1]:
        for i in range(num_stacks):
            # '[A] ' --> each box is four chars
            box = row[i * 4 + 1].rstrip()
            if len(box) > 0:
                stacks[i].append(box)
    # Reverse the stacks
    for stack in range(num_stacks):
        stacks[stack].reverse()

    # Process the move recipe - now multiple crates retain their order
    for move, fromstack, tostack in moves:
        if move == 1:
            # Need to convert to 0 index
            popped = stacks[fromstack - 1].pop()
            stacks[tostack - 1].append(popped)
        else:
            to_move = []
            for i in range(move):
                popped = stacks[fromstack - 1].pop()
                to_move.append(popped)
            to_move.reverse()
            stacks[tostack - 1].extend(to_move)

    # Create final string from top boxes
    top_boxes = ''.join([stacks[i].pop() for i in range(num_stacks)])

    if test:
        print(stacks_sec)
        print(moves)
        print(stacks)

    print(f'Part 1 (top_boxes): {top_boxes}')


if __name__ == '__main__':
    test = False
    t1 = time.perf_counter()
    main(test)
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")

