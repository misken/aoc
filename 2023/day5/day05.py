# Day 5 - If You Give A Seed A Fertilizer - Problems 1 and 2

"""
My code is truly horrible. See https://advent-of-code.xavd.id/writeups/2023/day/5/ for a great explanation
of a much better approach.
"""

import re
from collections import namedtuple
import numpy as np
import math

"""
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


def parse_maps(map_lines, test=False):
    Seedmap = namedtuple("Seedmap", "dest source range")
    maps = {}
    map_name_re = re.compile(r'([\w-]+)\smap:')
    for line in map_lines:
        if 'seeds:' in line:
            # seed line
            seeds = [int(seed) for seed in line.split(':')[-1].split()]
        elif ':' in line:
            # It's a new map
            map_name = re.search(map_name_re, line).group(1)
            maps[map_name] = []
        elif len(line) > 0:
            # It's mapping values
            dest, source, range = [int(val) for val in line.split()]
            maps[map_name].append(Seedmap(dest, source, range))

    return seeds, maps


def get_next_source(current_source, maps, map_section):
    map_segment_stop = None
    next_dest = current_source
    for range_def in maps[map_section]:
        map_range = range(range_def.source, range_def.source + range_def.range)
        if current_source in map_range:
            offset = current_source - range_def.source
            next_dest = range_def.dest + offset
            map_segment_stop = range_def.source + range_def.range

    return next_dest, map_segment_stop  # Will be current source if not mapped

def get_final_location(seed, maps, map_sections):
    current_source = seed
    next_source = current_source
    for map_section in map_sections:
        next_source, map_segment_stop = get_next_source(current_source, maps, map_section)
        current_source = next_source
    final_location = next_source
    return final_location


def process_maps(seeds, maps, test=False):

    map_sections = maps.keys()
    final_locations = {}
    for seed in seeds:
        final_location = seed # If not determined during mapping
        current_source = seed
        for map_section in map_sections:
            next_source, map_segment_stop = get_next_source(current_source, maps, map_section)
            current_source = next_source

        # If we get here, we made it to the final location
        final_location = next_source
        final_locations[seed] = final_location

    return final_locations

def process_maps_p2(seed_ranges, maps, test=False):

    map_sections = maps.keys()
    smallest_final_locations = np.infty
    starting_step_size = 10000
    for seed_range in seed_ranges:
        step_size = starting_step_size
        seed_start = seed_range.start
        seed_stop = seed_range.stop
        seed = seed_start
        range_checked = False

        location_changed = False
        while seed < seed_stop:
            final_location = get_final_location(seed, maps, map_sections)
            if final_location < smallest_final_locations:
                smallest_final_locations = final_location

            # Get and test next final location
            next_final_location = get_final_location(seed + step_size, maps, map_sections)
            if (next_final_location - final_location) == step_size:
                # We can step ahead
                seed = seed + step_size
            else:
                # We had a change
                # Did the final location change?d

                # Somewhere between seed and seed + step_size we had at least one change
                # Check the whole range
                current_seed = seed
                while seed < current_seed + step_size:
                    final_location = get_final_location(seed, maps, map_sections)
                    if final_location < smallest_final_locations:
                        smallest_final_locations = final_location

                    seed += 1

        print(seed_range, smallest_final_locations)


    return smallest_final_locations

def seeds_p2(seeds):
    # Now seed values come in pairs (start, num_values)

    num_pairs = int(len(seeds) / 2)
    seed_tuples = [(seeds[2 * i], seeds[2 * i + 1]) for i in range(0, num_pairs)]

    seed_ranges = []
    seed_range_tuples = []
    for seed_tuple in seed_tuples:
        seed_range = range(seed_tuple[0], seed_tuple[0] + seed_tuple[1])
        seed_range_tuple = (seed_tuple[0], seed_tuple[0] + seed_tuple[1])
        seed_ranges.append(seed_range)
        seed_range_tuples.append(seed_range_tuple)

    # check for overlap
    new_seed_ranges=[]

    a = [(7, 10), (11, 13), (11, 15), (14, 20), (23, 39)]
    b = []
    for begin, end in sorted(seed_range_tuples):
        if b and b[-1][1] >= begin - 1:
            b[-1][1] = max(b[-1][1], end)
        else:
            b.append([begin, end])

    return [range(seed_tuple[0], seed_tuple[0] + seed_tuple[1]) for seed_tuple in b]






def day5_p1(data, test=False):
    with open(data, 'r') as f_in:
        map_lines = f_in.read().splitlines()

    seeds, maps = parse_maps(map_lines, test)
    if test:
        print(seeds)
        print(maps.keys())

    final_locations = process_maps(seeds, maps, test)

    print(f'Part 1: Smallest location value = {min(final_locations.values())}')


def day5_p2(data, test=False):
    with open(data, 'r') as f_in:
        map_lines = f_in.read().splitlines()

    seeds, maps = parse_maps(map_lines, test)
    seed_ranges = seeds_p2(seeds)

    smallest_final_locations = process_maps_p2(seed_ranges, maps, test)

    print(f'Part 2: Smallest location value = {smallest_final_locations}')



def main():
    TEST = False
    if TEST:
        data_file = 'data/input_test.txt'
    else:
        data_file = 'data/input.txt'

    day5_p1(data_file, TEST)
    day5_p2(data_file, TEST)


if __name__ == '__main__':
    main()
