from itertools import combinations, pairwise as pw
s=lambda l:[((min(a,c),min(b,d)),(max(a,c),max(b,d)))for(a,b),(c,d)in l]
r=list(map(eval,open('day09.txt')))
g=s(pw(r+[r[0]]))
a=b=0
for(x,y),(u,v)in s(combinations(r,2)):
    z=(u-x+1)*(v-y+1)
    a=max(a,z)
    if z>b and all(not(p<u and q<v and r>x and s>y)for(p,q),(r,s)in g):b=z
print(a,b)