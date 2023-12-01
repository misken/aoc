# --- Day 10: Cathode-Ray Tube --- Part 1

from pathlib import Path
import time



def main(test=False):

    if test:
        data_file = Path('data/input_test.txt')
    else:
        data_file = Path('data/input.txt')

    cycles = {'noop': 1, 'addx': 2}
    xval = [1] # Starting register value
    xval_after = [1]

    with open(data_file, 'r') as f_in:
        commands = [m.rstrip() for m in f_in.readlines()]

    cur_cycle = 1
    for cmd in commands:
        if cmd == 'noop':
            xval.append(xval_after[cur_cycle - 1])
            xval_after.append(xval[cur_cycle])
            cur_cycle += 1

            if test:
                print(cur_cycle)

        else:
            xinc = int(cmd.split()[1])
            xval.append(xval_after[cur_cycle - 1])
            xval_after.append(xval[cur_cycle])
            cur_cycle += 1
            xval.append(xval_after[cur_cycle - 1])
            xval_after.append(xval[cur_cycle] + xinc)
            cur_cycle += 1

    signal_strengths = [xval[c] * c for c in range(20, 221, 40)]
    if test:
        print([xval[c] for c in range(20, 221, 40)])
        print([xval[c] for c in range(25)])
    if test:
        print(signal_strengths)

    tot_signal_strength = sum(signal_strengths)


    print(f'Part 1 (tot_signal_strength): {tot_signal_strength}')




if __name__ == '__main__':
    test = False
    t1 = time.perf_counter()
    main(test)
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")

