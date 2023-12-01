# Day n - Problem 1

test = False
if test:
    data_file = 'data/input_test.txt'
else:
    data_file = 'data/input.txt'

elfs = []
snacks = []
with open(data_file, 'r') as f_in:
    for line in f_in:
        if len(line.rstrip()) == 0:
            # new elf
            elfs.append(snacks)
            snacks = []
        else:
            snacks.append(int(line.rstrip()))

    # last elf
    elfs.append(snacks)

if test:
    print(elfs)

tot_calories = [sum(snacks) for snacks in elfs]
max_calories = max(tot_calories)
elf_max = tot_calories.index(max_calories)

# Part 2

tot_calories.sort(reverse=True)
tot_top3 = sum(tot_calories[:3])

if test:
    print(tot_calories, max_calories, elf_max)
    print(tot_top3)
else:
    print(f'max_calories: {max_calories} by elf {elf_max}')
    print(f'tot_top3: {tot_top3}')