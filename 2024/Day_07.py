import re
data = open("07.txt").read()
lines = [[int(n) for n in re.findall(r"(\d+)", line)] for line in data.split("\n")]

def is_valid(line, part):
    target, start, vals = line[1], line[0], line[2:][::-1]
    pool = {start}
    for val in vals:
        new_pool = set()
        for n in pool:
            if part==2 and str(n).endswith(str(val)) and n>val:
                new_pool.add(int(str(n)[:-len(str(val))]))
            if n % val == 0 and n // val >= target:
                new_pool.add(n // val)
            if n - val >= target:
                new_pool.add(n - val)
        if not new_pool: return False
        pool = new_pool
    return target in pool

print("Part 1:", sum(l[0]*is_valid(l,1) for l in lines))
print("Part 2:", sum(l[0]*is_valid(l,2) for l in lines))