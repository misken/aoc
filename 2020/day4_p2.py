import numpy as np
import pandas as pd
import re


def validate(entries):

    # Match whole line - was missing pid len > 9
    hgt_rgx = re.compile('^([0-9]+)(in|cm)$')
    hcl_rgx = re.compile('^#[0-9a-f]{6,6}$')
    pid_rgx = re.compile('^[0-9]{9,9}$')

    for e in entries:
        key, val = e.split(':')
        val = val.strip()

        if key == 'byr':
            assert 1920 <= float(val) <= 2002
        elif key == 'iyr':
            assert 2010 <= float(val) <= 2020
        elif key == 'eyr':
            assert 2020 <= float(val) <= 2030
        elif key == 'hgt':
            hgt_match = re.match(hgt_rgx, val)
            if hgt_match:
                height = hgt_match.group(1)
                units = hgt_match.group(2)
                if units == 'cm':
                    assert 150 <= float(height) <= 193
                elif units == 'in':
                    assert 59 <= float(height) <= 76
                else:
                    assert False
                #print(height, units)
            else:
                assert False
        elif key == 'hcl':
            if not re.match(hcl_rgx, val):
                assert False
            #print(val)
        elif key == 'ecl':
            assert val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            #print(val)

        elif key == 'pid':
            if not re.match(pid_rgx, val):
                assert False
            #print(val)

        elif key == 'cid': # Ignore cid if present
            assert True

        else: # Invalid key
            assert False

    return True


data_file = 'day4/input'
allkeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
good_passport = 0
num_with_missing_keys = 0
num_with_invalid_keys = 0
entries = []
new_dict = {}
valid_passports = []
linenum = 0
num_blank_lines = 0
do_validation = True
with open(data_file, 'r') as input:
    for line in input:

        line = line.rstrip()
        if len(line) > 0:
            new_entries = line.split()
            entries.extend(new_entries)
        else:
            # Read a blank line, done with this chunk
            linenum += 1
            for e in entries:
                # Split each entry on the ':' and create the dictionary to test
                pair = e.split(':')
                key = pair[0]
                val = pair[1]
                new_dict[key] = val

            # Look for missing keys other than 'cid'
            missing_keys = {key for key in allkeys if key not in new_dict.keys() if key != 'cid'}
            # print(missing_keys)
            if len(missing_keys) > 0:
                num_with_missing_keys += 1
                # print(missing_keys)
            else:
                try:
                    if do_validation:
                        valid = validate(entries)
                    else:
                        valid = True
                    if valid:
                        #print(linenum, entries, len(entries))
                        valid_passports.append(entries)
                        good_passport += 1
                except AssertionError:
                    num_with_invalid_keys += 1

            entries = []
            new_dict = {}

# Deal with the last chunk of data (since no blank line at end)
linenum += 1
for e in entries:
    pair = e.split(':')
    key = pair[0]
    val = pair[1]
    new_dict[key] = val

missing_keys = {key for key in allkeys if key not in new_dict.keys() if key != 'cid'}
# print(missing_keys)
if len(missing_keys) > 0:
    num_with_missing_keys += 1
    # print(missing_keys)
else:
    try:
        if do_validation:
            valid = validate(entries)
        else:
            valid = True
        if valid:
            valid_passports.append(entries)
            print(linenum, entries)
            good_passport += 1
    except AssertionError:
        num_with_invalid_keys += 1


print(linenum)
print(good_passport, num_with_missing_keys, num_with_invalid_keys)
assert linenum == good_passport + num_with_missing_keys + num_with_invalid_keys
print(len(valid_passports))