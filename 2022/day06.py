def solve(inp, count):
    for i in range(count, len(inp)):
        if len(set(inp[i - count : i])) == count:
            return i


with open("06.txt") as f:
    inp = f.read()
    print("Part 1:", solve(inp, 4))
    print("Part 2:", solve(inp, 14))