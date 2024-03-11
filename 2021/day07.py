with open("07.txt") as f:
    crabs = [int(x) for x in f.read().split(",")]


mi, ma = min(crabs), max(crabs)

better = float("inf")

for i in range(mi, ma + 1):
    better = min(better, sum(abs(k - i) for k in crabs))

print('Part 1:',better)

better = float("inf")

for i in range(mi, ma + 1):
    better = min(better, sum((abs(k - i) * (abs(k - i) + 1)) / 2 for k in crabs))

print('Part 2:',int(better))