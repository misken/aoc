# Day 8: Treetop Tree House - Problem 1

from pathlib import Path
import time
import queue


"""
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0
"""
def main(test=False):

    if test:
        data_file = Path('data/input_test.txt')
    else:
        data_file = Path('data/input.txt')

    num_rounds = 1

    with open(data_file, 'r') as f_in:
        monkey_blocks = [block.split('\n') for block in f_in.read().split('\n\n')]
        monkey_blocks = [[line.strip().split(':') for line in b] for b in monkey_blocks]

    if test:
        print(monkey_blocks)

    item_queues = []
    tossed_item_queues = {} # Key will be monkey, value will be list of items
    for round in range(num_rounds):
        for turn in monkey_blocks:
            # for step in turn:
            monkey_id = int(turn[0][0].split()[1])
            items_str = turn[1][1].split(',')
            items = [int(s.strip()) for s in items_str]
            q = queue.Queue()
            for item in items:
                q.put(item)

    for round in range(num_rounds):



    #print(f'Part 1 (num_visible): {num_visible_exterior}+{num_visible_interior}={num_visible}')


if __name__ == '__main__':
    test = True
    t1 = time.perf_counter()
    main(test)
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")

