
def prt1():
    with open("02.txt") as f:
        t = f.read().replace("\r", "").splitlines()

    t_ = []
    for l in t:
        l = l.split("-")
        a = int(l[0])
        l = l[1].split(" ")
        b = int(l[0])
        c = l[1][0]
        d = l[-1]

        t_.append((a, b, c, d))
    t = t_

    solution = 0
    for i in t:
        a, b, c, d = i
        n = len(list(filter(lambda i: i == c, d)))
        if a <= n <= b:
            solution += 1

    print('Parte 1:',solution)


def prt2():
    with open("02.txt") as f:
        t = f.read().replace("\r", "").splitlines()

    t_ = []
    for l in t:
        l = l.split("-")
        a = int(l[0])
        l = l[1].split(" ")
        b = int(l[0])
        c = l[1][0]
        d = l[-1]
        
        t_.append((a, b, c, d))
    t = t_
    
    solution = 0
    for i in t:
        a, b, c, d = i
        if (d[a - 1] == c) != (d[b - 1] == c):
            solution += 1

    print('Parte 2:',solution)

prt1()
prt2()