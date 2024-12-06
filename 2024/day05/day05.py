# Day 5 - Problem 1 and 2
import re

def day05(test=False):
    if test:
        data_file = 'data/input_test.txt'
    else:
        data_file = 'data/input.txt'

    rules = []
    pageses = []

    with open(data_file) as f:
        for line in f:
            if '|' in line:
                rules.append(line.rstrip().split('|'))
            elif ',' in line:
                pageses.append(line.rstrip().split(','))

    num_violations = [0 for _ in range(len(pageses))]
    violations = [[] for _ in range(len(pageses))]

    rule_num = 0
    for rule in rules:
        p = 0
        for pages in pageses:
            if is_rule_broken(rule, pages):
                num_violations[p] += 1
                violations[p].append(rule)
            p += 1
        rule_num += 1

    no_violations = [pageses[i] for i in range(len(pageses)) if violations[i] == []]
    yes_violations = [pageses[i] for i in range(len(pageses)) if violations[i] != []]
    mid_nums_no_violations = [int(pages[len(pages) // 2]) for pages in no_violations]
    #print(no_violations)
    #print(yes_violations)
    #print(num_violations)
    #print(violations)
    #print(mid_nums)

    print(f'Problem 1 total: {sum(mid_nums_no_violations)}')

    # Now need to fix the ones out of order
    v = 0
    fixed_pageses = []
    for pages in yes_violations:
        broken = True
        while broken:
            for rule in rules:
                if is_rule_broken(rule, pages):
                    a, b = rule
                    # Try swapping these two elements
                    b_idx = pages.index(b)
                    a_idx = pages.index(a)
                    pages[a_idx] = b
                    pages[b_idx] = a

            if is_correctly_ordered(rules, pages):
                broken = False

        fixed_pageses.append(pages)

    mid_nums_fixed_violations = [int(pages[len(pages) // 2]) for pages in fixed_pageses]
    print(f'Problem 2 total: {sum(mid_nums_fixed_violations)}')

def is_rule_broken(rule, pages):
    a, b = rule
    if a in pages and b in pages:
        b_idx = pages.index(b)
        a_idx = pages.index(a)
        if b_idx < a_idx:
            return True
        else:
            return False

def is_correctly_ordered(rules, pages):

    ordered = True
    for rule in rules:
        if is_rule_broken(rule, pages):
            return False
    return True


if __name__ == '__main__':
    test = False
    day05(test)

