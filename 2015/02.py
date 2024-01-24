import numpy as np

with open('02.txt') as f:
    lines = [list(map(int, line.split('x'))) for line in f.read().split('\n')]

def part1(total=0):
    for line in lines:
        sides=[line[0]*line[1], line[1]*line[2], line[0]*line[2]]
        total += sum(sides)*2 + min(sides)
    return total

def part2(total=0):
    for line in lines:
        esquinas=[line[0], line[1], line[2]]
        total+=np.prod(esquinas)
        esquinas.remove(max(esquinas))
        total+=sum(esquinas*2)
    return total

print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')