# Day 4 - Problems 1 and 2


from collections import Counter

"""
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

def parse_card(card):

    sections = card.split(':')
    numbers = sections[1].split('|')
    card_num = int(sections[0].split()[1])
    winning_numbers = numbers[0].split()
    your_numbers = numbers[1].split()
    return card_num, winning_numbers, your_numbers


def count_matches(winning, your):

    num_matches = sum([int(w == y) for w in winning for y in your])
    return num_matches


def day4_p1(data):
    with open(data, 'r') as f_in:
        cards = f_in.read().splitlines()

    values = []
    for card in cards:
        card_num, winning_numbers, your_numbers = parse_card(card)
        num_matches = count_matches(winning_numbers, your_numbers)
        if num_matches > 0:
            card_value = 2 ** (num_matches - 1)
        else:
            card_value = 0
        values.append(card_value)

    print(f'Part 1: Total value = {sum(values)}')


def day4_p2(data):
    with open(data, 'r') as f_in:
        card_lines = f_in.read().splitlines()

    card_counts = Counter({int(line.split(':')[0].split()[1]): 1 for line in card_lines})

    for card in card_lines:
        card_num, winning_numbers, your_numbers = parse_card(card)
        num_matches = count_matches(winning_numbers, your_numbers)

        # Increment number of cards for card_num+1:card_num+num_matches+1
        num_copies = card_counts[card_num]

        for cnum in range(card_num+1, card_num+num_matches+1):
            card_counts[cnum] += num_copies

    total_cards = card_counts.total()
    print(f'Part 2: Total cards = {total_cards}')


def main():
    TEST = False
    if TEST:
        data_file = 'data/input_test.txt'
    else:
        data_file = 'data/input.txt'

    day4_p1(data_file)
    day4_p2(data_file)


if __name__ == '__main__':
    main()
