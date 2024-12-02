# Day 1 - Problem 1 and 2

def day01_p1(test=False):
    if test:
        data_file = 'data/input_test.txt'
    else:
        data_file = 'data/input.txt'

    list1 = []
    list2 = []

    with open(data_file, 'r') as f_in:
        for line in f_in:
            vals = line.split()
            list1.append(int(vals[0]))
            list2.append(int(vals[1]))

    # Sort the lists
    list1.sort()
    list2.sort()

    diffs = [abs(list1[i] - list2[i]) for i in range(len(list1))]

    print(f'Problem 1 total: {sum(diffs)}')


def day01_p2(test=False):
    if test:
        data_file = 'data/input_test.txt'
    else:
        data_file = 'data/input.txt'

    list1 = []
    list2 = []

    with open(data_file, 'r') as f_in:
        for line in f_in:
            vals = line.split()
            list1.append(int(vals[0]))
            list2.append(int(vals[1]))

    sim_score = 0
    for left_val in list1:
        num_right = list2.count(left_val)
        sim_inc = left_val * num_right
        sim_score += sim_inc

    print(f'Problem 2 total: {sim_score}')

if __name__ == '__main__':
    test = False
    day01_p1(test)
    day01_p2(test)
