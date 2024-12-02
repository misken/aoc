# Day 2 - Problem 1 and 2

def day01_p1(test=False):
    if test:
        data_file = 'data/input_test.txt'
    else:
        data_file = 'data/input.txt'

    with open(data_file, 'r') as f_in:
        reports = [[int(level) for level in r.split()] for r in f_in.readlines()]

    # Compute adjancent diffs
    num_safe = 0
    for report in reports:
        safe = check_safety(report)

        if safe:
            num_safe += 1

    print(f'Problem 1 total: {num_safe}')


def check_safety(report):
    rdiffs = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    is_safely_inc = [d >= 1 and d <= 3 for d in rdiffs]
    is_safely_dec = [d <= -1 and d >= -3 for d in rdiffs]

    safe = all(is_safely_inc) or all(is_safely_dec)

    if safe:
        return True
    else:
        return False


def day01_p2(test=False):
    if test:
        data_file = 'data/input_test.txt'
    else:
        data_file = 'data/input.txt'

    with open(data_file, 'r') as f_in:
        reports = [[int(level) for level in r.split()] for r in f_in.readlines()]

    # Compute adjancent diffs
    num_safe = 0
    for report in reports:

        safe = check_safety(report)

        if safe:
            num_safe += 1
        else:
            # Use the dampener
            for index in range(len(report)):
                damp_report =  report[:index] + report[index+1 :]
                safe = check_safety(damp_report)
                if safe:
                    num_safe += 1
                    break

    print(f'Problem 2 total: {num_safe}')

if __name__ == '__main__':
    test = False
    day01_p1(test)
    day01_p2(test)
