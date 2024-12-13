with open('13.txt') as f:
    lines = [line.rstrip() for line in f]

def solve(part):
    tokens, add = 0, 10**13 if part == 2 else 0
    for line in lines:
        if line.startswith("Button"):
            a, x, y = line.split()[1][0], *map(int, [line.split()[2][2:-1], line.split()[3][2:]])
            if a == 'A': x1, y1 = x, y
            else: x2, y2 = x, y
        elif line.startswith("Prize"):
            c, d = map(lambda v: int(v[2:]) + add, [line.split()[1][:-1], line.split()[2]])
            a, b = (c*y2 - d*x2)/(x1*y2 - y1*x2), (d*x1 - c*y1)/(x1*y2 - y1*x2)
            if a.is_integer() and b.is_integer(): tokens += int(3*a + b)
    print(tokens)

solve(1)
solve(2)