range_sorted = lambda *p: range(min(p), max(p)+1)
blocked = set()

for ps in [[*map(eval, line.split('->'))] for line in open('14.txt')]:
    for (x1, y1), (x2, y2) in zip(ps, ps[1:]):
        blocked |= {complex(x, y) for x in range_sorted(x1, x2)
                                  for y in range_sorted(y1, y2)}

floor = max(x.imag for x in blocked)

def f(check, path=[500], rock=len(blocked)):
    while True:
        pos = path[-1]
        for dest in pos+1j, pos-1+1j, pos+1+1j:
            if dest not in blocked and dest.imag < floor+2:
                path.append(dest)
                break
        else:
            if check(pos): return len(blocked)-rock
            blocked.add(pos)
            del path[-1]

print('Part 1',f(lambda pos: pos.imag > floor))
print('Part 2:',f(lambda pos: pos == 500) + 1)