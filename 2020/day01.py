
def prt1():
    with open("01.txt") as f:
        t = f.read().replace("\r", "").splitlines()

    t = [int(i) for i in t]
    t.sort()

    for i in range(len(t)):
        for j in range(len(t)):
            j = len(t) - j - 1
            a = t[i]
            b = t[j]
            if a + b == 2020:
                print('Parte 1:',a * b)
                return
            if a + b < 2020:
                break


def prt2():
    with open("01.txt") as f:
        t = f.read().replace("\r", "").splitlines()

    t = [int(i) for i in t]
    t.sort()

    n = len(t)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                j = n - j - 1
                k = n - k - 1
                a = t[i]
                b = t[j]
                c = t[k]
                if a + b + c == 2020:
                    print('Parte 2:',a * b * c)
                    return
                if a + b + c < 2020:
                    break



prt1()
prt2()