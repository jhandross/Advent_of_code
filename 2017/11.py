i = []
with open("11.txt") as f:
  i = f.read().split(",")

dmap = {
  "n": (0,1),
  "s": (0,-1),
  "ne": (.5,.5),
  "se": (.5,-.5),
  "nw": (-.5,.5),
  "sw": (-.5,-.5)
}

x,y = 0,0
m = []
for d in i:
  x += dmap[d][0]
  y += dmap[d][1]
  m.append(abs(x)+abs(y))

print('Part 1:',int(abs(x)+abs(y)))
print('Part 2:',int(max(m)))