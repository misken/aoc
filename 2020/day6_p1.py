

data_file = 'day6/input'
groups = 0
counts = []

letters = set()
with open(data_file, 'r') as input:
    for line in input:

        line = line.rstrip()
        if len(line) > 0:
           letters = letters | set(line)
        else:
            # Read a blank line, done with this group
            groups += 1
            counts.append(len(letters))
            letters = set()

# Append the last group
groups += 1
counts.append(len(letters))

print(groups)
print(counts)
print(sum(counts))