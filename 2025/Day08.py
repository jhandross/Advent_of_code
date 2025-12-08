import math,itertools
P=[tuple(map(int,l.split(',')))for l in open('day08.txt')]
G={frozenset([p])for p in P}
for i,(a,b) in enumerate(sorted(itertools.combinations(P,2),key=lambda x:math.dist(*x))):
    if i==1000:print('p1',math.prod(map(len,sorted(G,key=len)[-3:])))
    A=next(c for c in G if a in c);B=next(c for c in G if b in c)
    G-={A,B}
    if not G:print('p2',a[0]*b[0]);break
    G.add(A|B)