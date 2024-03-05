
lookup = {
    ".": 0,
    "L": 1,
    "#": 2,
}
reverse_lookup = {}
for k, v in lookup.items():
    reverse_lookup[v] = k


def read():
    with open("13.txt") as f:
        t = f.read().replace("\r", "")
    t = t.split("\n")
    N = int(t[0])
    t = t[1].split(",")

    t = ["x" if e == "x" else int(e) for e in t]

    return N, t


N, t = read()


def prt1():
    r = []
    for i in t:
        if i == "x":
            continue
        r.append((i, i - (N % i)))
    r.sort(key=lambda e: e[1])
    print('Part 1:',r[0][0] * r[0][1])


def prt2():
    constraints = []
    for i, n in enumerate(t):
        if n == "x":
            continue
        constraints.append((n, n - i))

    j = 0
    add = 1
    for div, rst in constraints:
        while j % div != rst % div:
            j += add
        add *= div
    print('Part 2:',j)

prt1()
prt2()