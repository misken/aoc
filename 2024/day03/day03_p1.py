# Day 3 - Problem 1 and 2
import re
def day03_p1(test=False):
    if test:
        data_file = 'data/input_test.txt'
    else:
        data_file = 'data/input.txt'

    with open(data_file, 'r') as f_in:
        corrupted_instructions = [r.strip() for r in f_in.readlines()]

    mul_instr_re = r'mul\([0-9]+,[0-9]+\)'
    get_operands_re = r'mul\(([0-9]+),([0-9]+)\)'

    instructions = []
    for line in corrupted_instructions:
        new_instructions = re.findall(mul_instr_re, line)
        instructions.extend(new_instructions)

    total = 0
    for i in instructions:
        op_match = re.match(get_operands_re, i)
        op1 = int(op_match.group(1))
        op2 = int(op_match.group(2))
        total += op1 * op2

    print(f'Problem 1 total: {total}')


def day03_p2(test=False):
    if test:
        data_file = 'data/input_test.txt'
    else:
        data_file = 'data/input.txt'

    with open(data_file, 'r') as f_in:
        corrupted_instructions = [r.strip() for r in f_in.readlines()]

    # Create one big instruction
    instruction = ''.join(corrupted_instructions)

    instr_re = r"don't\(\)|do\(\)|mul\(([0-9]+),([0-9]+)\)"

    ins_size = len(instruction)
    start_pos = 0

    total = 0
    enabled_mults = []
    do = True
    while start_pos < ins_size:
        token_match = re.search(instr_re, instruction[start_pos:])
        if token_match:
            item = token_match.group()
            if item == "don't()":
                do = False
                start_pos = start_pos + token_match.end()
            elif item == "do()":
                do = True
                start_pos = start_pos + token_match.end()
            else:
                if do:
                    enabled_mults.append(item)
                    op1 = int(token_match.group(1))
                    op2 = int(token_match.group(2))
                    total += op1 * op2
                start_pos = start_pos + token_match.end()
        else:
            start_pos = ins_size + 1

    print(f'Problem 2 total: {total}')



if __name__ == '__main__':
    test = False
    day03_p1(test)
    day03_p2(test)
