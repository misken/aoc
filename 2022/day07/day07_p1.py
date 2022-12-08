# Day 7 - Problem 1

from pathlib import Path
import time


def main(test=False):

    if test:
        data_file = Path('data/input_test.txt')

        test_str = """
            $ cd /
            $ ls
            dir a
            14848514 b.txt
            8504156 c.dat
            dir d
            $ cd a
            $ ls
            dir e
            29116 f
            2557 g
            62596 h.lst
            $ cd e
            $ ls
            584 i
            $ cd ..
            $ cd ..
            $ cd d
            $ ls
            4060174 j
            8033020 d.log
            5626152 d.ext
            7214296 k"""
    else:
        data_file = Path('data/input.txt')

    with open(data_file, 'r') as f_in:
        # Read commands into a list
        cmds = f_in.readlines()

    # Process one command at a time
    cwd = ''
    cpath = '' # Keep track of path from root to cwd
    level = 0

    # Use list of dicts to hold file tree. Level is list index
    ftree = [{}]
    for cmd in cmds:
        cmd_details = cmd.split()
        if cmd_details[0] == 'cd':
            dir = cmd_details[1]
            if dir not in ftree[level]:

        elif cmd_details[0] == 'ls':
            pass
        elif cmd_details[0] == 'dir':
            pass
        else: # it's a file
            pass

        


if __name__ == '__main__':
    test = False
    t1 = time.perf_counter()
    main(test)
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")

