# Day 2 - Problem 1

test = False
if test:
    data_file = 'data/input_test_p1.txt'
else:
    data_file = 'data/input_p1.txt'

# Method 1 - list of lists

position = 0
depth = 0
with open(data_file, 'r') as file_input:
    lines = file_input.readlines()
    instructions = [line.split() for line in lines]
    print(instructions)
    for inst in instructions:
        if inst[0] == 'forward':
            position += float(inst[1])
        elif inst[0] == 'up':
            depth -= float(inst[1])
        elif inst[0] == 'down':
            depth += float(inst[1])
        else:
            print(f'unknown instruction {inst}')
            exit(0)

pos_depth = position * depth
print(f'Method 1: list of lists --> position: {position}, depth: {depth}, product: {pos_depth}')

