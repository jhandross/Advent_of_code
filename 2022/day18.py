cubes = {tuple(map(int,l.split(','))) for l in open('18.txt')}
sides = lambda x,y,z: {(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)}

print('Part 1:',sum((s not in cubes) for c in cubes for s in sides(*c)))

seen = set()
todo = [(-1,-1,-1)]

while todo:
    here = todo.pop()
    todo += [s for s in (sides(*here) - cubes - seen) if all(-1<=c<=25 for c in s)]
    seen |= {here}

print('Part 2:',sum((s in seen) for c in cubes for s in sides(*c)))