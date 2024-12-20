from functools import cache

blocks = [block.splitlines() for block in open("19.txt").read().split("\n\n")]
patterns = blocks[0][0].split(", ")

@cache
def count_ways(d):
    return 1 if not d else sum(count_ways(d[len(p):]) for p in patterns if d.startswith(p))

ans1, ans2 = 0, 0
for d in blocks[1]:
    ans1 += count_ways(d) > 0
    ans2 += count_ways(d)

print(f"part 1: {ans1}\npart 2: {ans2}")