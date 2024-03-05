from functools import reduce
from string import ascii_lowercase


def read():
    with open("06.txt") as f:
        t = f.read().replace("\r", "").split("\n\n")
    if t[-1] == "":
        t.pop()
    t = [l.split("\n") for l in t]
    if t[-1][-1] == "":
        t[-1].pop()

    return t


def prt1():
    t = read()

    t = [len(reduce(lambda a, b: a | set(list(b)), e, set())) for e in t]
    print('Part 1:',sum(t))


def prt2():
    t = read()

    t = [
        len(reduce(lambda a, b: a & set(list(b)), e, set(list(ascii_lowercase))))
        for e in t
    ]
    print('Part 2:',sum(t))

prt1()
prt2()