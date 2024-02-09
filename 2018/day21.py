import pathlib


def read():
    with open('21.txt') as f:
        t = f.read().splitlines()
    return [[i[:4], *map(int, i[5:].split(" "))] for i in t[1:]]


def test():
    s = set()
    b = c = d = i = 0
    while True:
        b = c | A
        c = C
        while True:
            c += b & 255
            c &= D
            c *= B
            c &= D
            if b < 256:
                if i == 0:
                    print('Part 1:',c)
                if c in s:
                    print('Part 2:',d)
                    return
                d = c
                i = 1
                s.add(c)
                break
            else:
                b //= 256


def easy():
    return


def hard():
    test()



t = read()
A, B, C, D = t[6][2], t[11][2], t[7][1], t[10][2]


if __name__ == "__main__":
    easy()
    hard()