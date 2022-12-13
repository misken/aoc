# Day 8: Treetop Tree House - Problem 1

from pathlib import Path
import time
from collections import Counter


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

def throw(item_queues, from_monkey, item_idx, to_monkey, new_worry_level):

    thrown_item = item_queues[from_monkey].pop(item_idx)
    item_queues[to_monkey].append(new_worry_level)
    return item_queues



def main(test=False):

    if test:
        data_file = Path('data/input_test.txt')
    else:
        data_file = Path('data/input.txt')

    num_rounds = 1
    inspections = []

    with open(data_file, 'r') as f_in:
        monkey_blocks = [block.split('\n') for block in f_in.read().split('\n\n')]
        monkey_blocks = [[line.strip().split(':') for line in b] for b in monkey_blocks]

    if test:
        print(monkey_blocks)

    item_queues = []
    op_test = []
    inspection_counts = []

    # Start by making pass to fill current items possessed by each monkey

    for turn in monkey_blocks:
        inspection_counts.append(0)
        monkey_id = int(turn[0][0].split()[1])
        items_str = turn[1][1].split(',')
        items = [int(s.strip()) for s in items_str]
        q = []
        for item in items:
            q.append(item)
        item_queues.append(q)

        operation = turn[2][1].split()
        if operation[4] == 'old':
            op, op_val = '^', 2
        else:
            op, op_val = operation[3], int(operation[4])
        op_test_dict = {'mid': monkey_id, 'op': op, 'op_val': op_val}

        test = turn[3][1].split()
        op_test_dict['test_div'] = int(test[-1])

        true_throw = turn[4][1].split()
        op_test_dict['true_throw'] = int(true_throw[-1])

        false_throw = turn[5][1].split()
        op_test_dict['false_throw'] = int(false_throw[-1])
        op_test.append(op_test_dict)

    if test:
        print(op_test)

    if test:
        for i in range(len(item_queues)):
            print(f'Monkey {i}: {item_queues[i]}')

    # Now let's play the rounds
    for round in range(num_rounds):
        #print(f'round {round}')
        for monkey in range(len(monkey_blocks)):
            # Monkey worry level escalation
            ot = op_test[monkey]
            item_idx = 0
            items = item_queues[monkey].copy()
            for item in items:
                inspection_counts[monkey] += 1
                worry_level = item
                if ot['op'] == '+':
                    worry_level += ot['op_val']
                elif ot['op'] == '*':
                    worry_level *= ot['op_val']
                elif ot['op'] == '^':
                    #continue
                    worry_level = worry_level ** ot['op_val']
                else:
                    raise ValueError

                # My worry level de-escalation
                # worry_level = worry_level // 3

                # Check divisibility
                is_divisible = (worry_level % ot['test_div']) == 0

                if is_divisible:
                    # Throw to True monkey
                    throw_to = ot['true_throw']
                else:
                    # Throw to False monkey
                    throw_to = ot['false_throw']

                item_queues = throw(item_queues, monkey, item_idx, throw_to, worry_level)
                #print(item_queues)
                #item_idx += 1

    #print(item_queues)
    print(inspection_counts)


    #print(f'Part 1 (num_visible): {num_visible_exterior}+{num_visible_interior}={num_visible}')


if __name__ == '__main__':
    test = True
    t1 = time.perf_counter()
    main(test)
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")

