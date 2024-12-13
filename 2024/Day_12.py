from collections import defaultdict
with open("12.txt") as f:
    L=[list(x) for x in f.read().split()]
W,H=len(L),len(L[0])
area,perim,corners=defaultdict(int),defaultdict(int),defaultdict(int)
CC=[[0]*W for _ in range(H)]
seen,numcc={},0
def dfs(x,y):
    if (x,y)in seen:return
    seen[(x,y)]=1;CC[y][x]=numcc
    for dx,dy in((0,1),(0,-1),(1,0),(-1,0)):
        nx,ny=x+dx,y+dy
        if 0<=nx<W and 0<=ny<H and L[ny][nx]==L[y][x]:dfs(nx,ny)
def get(x,y):return-1 if not(0<=x<W and 0<=y<H)else CC[y][x]
for y in range(H):
    for x in range(W):
        if(x,y)not in seen:dfs(x,y);numcc+=1
for y in range(H):
    for x in range(W):
        a=get(x,y);area[a]+=1;k=4
        if a==get(x-1,y):k-=2
        if a==get(x,y-1):k-=2
        perim[a]+=k
        for dx,dy in((-1,-1),(-1,1),(1,-1),(1,1)):
            b,c,d=get(x+dx,y),get(x,y+dy),get(x+dx,y+dy)
            if(a!=b and a!=c)or(a==b==c!=d):corners[a]+=1
print(sum(area[x]*perim[x]for x in area))
print(sum(area[x]*corners[x]for x in area))