

data_file = 'day6/input'
groups = 0
counts = []

letters = set()
new_group = True
with open(data_file, 'r') as input:
    for line in input:

        line = line.rstrip()
        if len(line) > 0:
            if new_group:
                letters = set(line)
                new_group = False
            else:
                letters = letters & set(line)
        else:
            # Read a blank line, done with this group
            groups += 1
            counts.append(len(letters))
            letters = set()
            new_group = True

# Append the last group
groups += 1
counts.append(len(letters))

print(groups)
print(counts)
print(sum(counts))