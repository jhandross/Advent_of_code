from collections import defaultdict
lines=open('day07.txt').read().splitlines()
beams={lines.pop(0).index('S'):1}; lines=[l for l in lines if '^' in l]; splits=0
for row in lines:
    nb=defaultdict(int)
    for i,n in beams.items():
        if row[i]=='^': splits+=1; nb[i-1]+=n; nb[i+1]+=n
        else: nb[i]+=n
    beams=nb
print('Part1 =',splits); print('Part2 =',sum(beams.values()))