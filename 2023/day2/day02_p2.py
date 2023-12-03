# Day 2 - Problem 1

import re


"""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

def list_product(power_list):
    p = 1
    for power in power_list:
        p *= power
    return p

TEST = False

if TEST:
    data_file = 'data/input_test.txt'
else:
    data_file = 'data/input.txt'

power = []
with open(data_file, 'r') as f_in:
    games = [s.rstrip() for s in f_in.readlines()]

    # Process each game
    for game in games:
        needed = {'red': 0, 'green': 0, 'blue': 0}
        id_sets = game.split(':')
        game_id = int(id_sets[0].split(' ')[1])
        sets = [s.strip() for s in id_sets[1].split(';')]
        # Process each set
        for set in sets:
            color_groups = set.split(', ')
            for cg in color_groups:
                color = cg.split(' ')[1]
                number = int(cg.split(' ')[0])
                if number > needed[color]:
                    needed[color] = number

        game_power = list_product([val for key, val in needed.items()])
        power.append(game_power)
        if TEST:
            print(f'Game {game_id} power is {game_power}')

    total_power = sum(power)
    print(f'Total power: {total_power}')