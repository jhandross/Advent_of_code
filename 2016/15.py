import re

with open('15.txt', 'r') as infile:
    instructions = infile.read().split('\n')

discs = []
for i, line in enumerate(instructions, 1):
    settings = re.search(r'(\d+) positions; .+ (\d+)', line)
    slots = int(settings.group(1))
    position = int(settings.group(2)) + i
    discs.append((slots, position))


def wait_a_sec(discs):
    time = 0
    while True:
        if not sum((position+time)%slot for (slot, position) in discs):
            return time
        time += 1


first = wait_a_sec(discs)

# a new disc with 11 positions and starting at position 0 has appeared
# exactly one second below the previously-bottom disc
discs.append((11, 0+7))
second = wait_a_sec(discs)


print(f"Part 1: {first}")
print(f"Part 2: {second}")
