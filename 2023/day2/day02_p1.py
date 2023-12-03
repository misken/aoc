# Day 2 - Problem 1

import re

"""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

BAG = {'red': 12, 'green': 13, 'blue': 14}
TEST = False

if TEST:
    data_file = 'data/input_test.txt'
else:
    data_file = 'data/input.txt'

possible = []
with open(data_file, 'r') as f_in:
    games = [s.rstrip() for s in f_in.readlines()]

    # Process each game
    for game in games:
        id_sets = game.split(':')
        game_id = int(id_sets[0].split(' ')[1])
        sets = [s.strip() for s in id_sets[1].split(';')]
        # Process each set
        ispossible = True
        for set in sets:
            if ispossible:
                color_groups = set.split(', ')
                for cg in color_groups:
                    color = cg.split(' ')[1]
                    number = int(cg.split(' ')[0])
                    if number > BAG[color]:
                        ispossible = False
                        break
        if ispossible:
            possible.append(game_id)
            if TEST:
                print(f'{game_id} is possible')

    total_possible = sum(possible)
    print(total_possible)