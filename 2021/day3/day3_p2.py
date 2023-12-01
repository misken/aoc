test = False
if test:
    data_file = 'data/input_test_p1.txt'
else:
    data_file = 'data/input_p1.txt'

# Method 1 - list of lists

with open(data_file, 'r') as file_input:
    lines = file_input.readlines()
    lines = [line.rstrip() for line in lines]
    lines_co2 = lines.copy()
    num_lines = len(lines)
    codelen = len(lines[0])

    # oxygen rating
    for i in range(codelen):
        num_ones = sum([int(line[i]) for line in lines])
        num_zeroes = len(lines) - num_ones

        if num_ones >= num_zeroes:
            # Keep the ones in this bit position
            lines = [line for line in lines if line[i] == '1']
        else:
            lines = [line for line in lines if line[i] == '0']

        #print(lines)

        # check if done
        if len(lines) == 1:
            break

    oxygen_rating = int(lines[0], 2)

    print(oxygen_rating)

    # co2 rating
    for i in range(codelen):
        num_ones = sum([int(line[i]) for line in lines_co2])
        num_zeroes = len(lines_co2) - num_ones

        if num_ones >= num_zeroes:
            # Keep the z in this bit position
            lines_co2 = [line for line in lines_co2 if line[i] == '0']
        else:
            lines_co2 = [line for line in lines_co2 if line[i] == '1']

        # check if done
        if len(lines_co2) == 1:
            break

    co2_rating = int(lines_co2[0], 2)
    print(co2_rating)

    print(oxygen_rating * co2_rating)


