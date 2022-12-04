# Day 2 - Problem 2

from pathlib import Path
import time


def main(test=False):
    if test:
        data_file = Path('data/input_test.txt')
    else:
        data_file = Path('data/input.txt')

    choice_val = {key: ord(key) - 64 for key in 'ABC'}
    game_results = {'AA': 3, 'AB': 6, 'AC': 0,
                    'BA': 0, 'BB': 3, 'BC': 6,
                    'CA': 6, 'CB': 0, 'CC': 3}

    game_strategy = {'AX': 'C', 'AY': 'A', 'AZ': 'B',
                     'BX': 'A', 'BY': 'B', 'BZ': 'C',
                     'CX': 'B', 'CY': 'C', 'CZ': 'A'}

    with open(data_file, 'r') as f_in:
        games = [s.split() for s in f_in.readlines()]
        if test:
            print(games)

        scores = []
        for g in games:
            strategy = game_strategy[f'{g[0]}{g[1]}']
            score = choice_val[strategy] + game_results[f'{g[0]}{strategy}']
            scores.append(score)

        tot_score = sum(scores)
        print(f'Part 2 (tot_score): {tot_score}')


if __name__ == '__main__':
    test = True
    t1 = time.perf_counter()
    main(test)
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
