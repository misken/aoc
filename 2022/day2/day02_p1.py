# Day 2 - Problem 1

from pathlib import Path
import time


def main(test=False):

    if test:
        data_file = Path('data/input_test.txt')
    else:
        data_file = Path('data/input.txt')

    choice_val = {'X': 1, 'Y': 2, 'Z': 3}
    game_results = {'AX': 3, 'AY': 6, 'AZ': 0,
                    'BX': 0, 'BY': 3, 'BZ': 6,
                    'CX': 6, 'CY': 0, 'CZ': 3}

    with open(data_file, 'r') as f_in:
        games = [s.split() for s in f_in.readlines()]
        if test:
            print(games)

        scores = []
        for g in games:
            score = choice_val[g[1]] + game_results[f'{g[0]}{g[1]}']
            scores.append(score)

        tot_score = sum(scores)
        print(f'Part 1 (tot_score): {tot_score}')

if __name__ == '__main__':
    test = False
    t1 = time.perf_counter()
    main(test)
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")

