ls=open("day05.txt").read().splitlines()
r=[list(map(int,l.split("-"))) for l in ls if"-" in l]
i=[int(l) for l in ls if l and"-" not in l]
print(sum(any(a<=x<=b for a,b in r) for x in i))
r.sort(); m=[]
for a,b in r:m.append([a,b]) if not m or m[-1][1]<a-1 else m[-1].__setitem__(1,max(m[-1][1],b))
print(sum(b-a+1 for a,b in m))
print(i)