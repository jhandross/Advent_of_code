with open("day02.txt") as f:
    intervals = [tuple(map(int, x.split("-"))) for x in f.read().split(",")]

p1 = p2 = 0
for lb, ub in intervals:
    for n in range(lb, ub+1):
        s = str(n)
        if len(s)%2==0 and s[:len(s)//2]*2==s: p1+=n
        if any(s[:k]*(len(s)//k)==s for k in range(1,len(s)//2+1) if len(s)%k==0): p2+=n

print(p1,p2)
