import numpy as np

with open('25.txt') as f:
    cucumber=f.read().strip().split()

field = np.array(list(map(list, cucumber)))

moved = [True]
while any(moved[-2:]):
    for who,axis in ((">",1), ("v",0)):
        allowed_moves = (np.roll(field, -1, axis) == ".") & (field == who)
        moved.append(np.any(allowed_moves))
        field[allowed_moves] = "."
        field[np.roll(allowed_moves, 1, axis)] = who

print('Part 1:',len(moved)//2)