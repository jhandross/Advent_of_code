def j(n,b): return max(b) if n==1 else (lambda m: m*10**(n-1)+j(n-1,b[b.index(m)+1:]))(max(b[:-(n-1)]))
p1=p2=0
for b in (list(map(int,l.strip())) for l in open('day03.txt')):
    p1+=j(2,b);p2+=j(12,b)
print(p1)
print(p2)