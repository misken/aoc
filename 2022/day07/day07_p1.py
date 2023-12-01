# Day 7 - Problem 1

from pathlib import Path
import time

def dir_size(dir, tree):

    size = 0
    for key, node in tree.items():
        if node['parent'] == dir:
            size += node['size']

    return size


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
        cmds = [c.rstrip() for c in f_in.readlines()]

    # Process one command at a time
    cwd = ''
    # cpath = '' # Keep track of path from root to cwd
    # level = 0

    dirs = ['/']

    # Use list of dicts to hold file tree. Level is list index
    ftree = {'/': {'type': 'dir', 'parent': None, 'size': 0, 'level': 0}}
    for cmd in cmds:
        cmd_details = cmd.split()
        if cmd_details[1] == 'cd':
            dir = cmd_details[2]
            if dir == '..':
                cwd = '&'.join(cwd.split('&')[:-1])
            else:
                if dir != '/':
                    cwd = f'{cwd}&{dir}'
                else:
                    cwd = '/'
        elif cmd_details[1] == 'ls':
            pass
        elif cmd_details[0] == 'dir':
            new_dir_name = f'{cwd}&{cmd_details[1]}'
            ftree[new_dir_name] = {'type': 'dir', 'parent': cwd, 'size': 0, 'level': new_dir_name.count('&')}
            dirs.append(new_dir_name)
        else: # it's a file
            file_size = int(cmd_details[0])
            new_file_name = f'{cwd}&{cmd_details[1]}'
            ftree[new_file_name] = {'type': 'file', 'size': file_size, 'parent': cwd}

    if test:
        print(ftree)
        print(dirs)

    # Work from terminal nodes up
    levels = [ftree[d]['level'] for d in dirs]

    dirs.sort(key=lambda d: d.count('&'), reverse=True)

    if test:
        print(levels)
        print(dirs)

    for d in dirs:
        ftree[d]['size'] = dir_size(d, ftree)

# if val['size'] <= 100000
    dir_sizes = [(key, val['size']) for key, val in ftree.items() if val['type'] == 'dir' if val['size'] <= 100000]

    tot_size = sum([d[1] for d in dir_sizes])

    print(dir_sizes)
    print(f'Part 1 (tot_size): {tot_size}')


if __name__ == '__main__':
    test = False
    t1 = time.perf_counter()
    main(test)
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")

