def s(lst): return sorted(lst) in [lst, lst[::-1]] and all(1 <= abs(a - b) <= 3 for a, b in zip(lst, lst[1:]))
p1, o = 0, 0
for l in open('02.txt'):
    L = list(map(int, l.split()))
    p1 += s(L)
    o += not s(L) and any(s(L[:i] + L[i + 1:]) for i in range(len(L)))
print(p1, p1 + o, sep='\n')
