from scipy.optimize import linprog
from collections import deque

T=[({i for i,x in enumerate(t[1:-1])if x=='#'},
    [set(map(int,b[1:-1].split(',')))for b in bs],
    tuple(map(int,c[1:-1].split(','))))
   for t,*bs,c in(map(str.split,open('day10.txt')))]

def s1(g,m):
    q,seen=deque([(frozenset(),0)]),{frozenset()}
    while q:
        cur,s=q.popleft()
        if cur==g:return s
        for x in m:
            n=cur^x;f=frozenset(n)
            if f not in seen:seen.add(f);q.append((n,s+1))

print(sum(s1(g,m)for g,m,_ in T))

def s2(g,m):
    return linprog([1]*len(m),
        A_eq=[[i in x for x in m]for i in range(len(g))],
        b_eq=g,integrality=True).fun

print(sum(s2(c,m)for _,m,c in T))