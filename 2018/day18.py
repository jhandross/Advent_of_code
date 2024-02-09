#!/usr/bin/env python3

from itertools import product

OPEN = '.'
TREES = '|'
LUMBERYARD = '#'

def atleast(g, x, n):
    s = 0
    for i in g:
        if i == x:
            s += 1
            if s == n:
                return True
    return False

def adjacent(grid, i, j, n):
    for dx, dy in product([-1, 0, 1], repeat=2):
        if dx+dy or dx*dy:
            x, y = i+dx, j+dy
            if 0 <= x < n and 0 <= y < n:
                yield grid[y][x]

def make_str(grid):
    return "\n".join("".join(line) for line in grid)

def evolve(n, grid, grid2):
    for j in range(n):
        for i in range(n):
            if grid[j][i] == OPEN:
                if atleast(adjacent(grid, i, j, n), TREES, 3):
                    grid2[j][i] = TREES
                else:
                    grid2[j][i] = OPEN

            elif grid[j][i] == TREES:
                if atleast(adjacent(grid, i, j, n), LUMBERYARD, 3):
                    grid2[j][i] = LUMBERYARD
                else:
                    grid2[j][i] = TREES

            elif grid[j][i] == LUMBERYARD:
                if atleast(adjacent(grid, i, j, n), TREES, 1) and\
                        atleast(adjacent(grid, i, j, n), LUMBERYARD, 1):
                    grid2[j][i] = LUMBERYARD
                else:
                    grid2[j][i] = OPEN

def resource_value(grid):
    trees = sum(c == TREES for line in grid for c in line)
    lumberyards = sum(c == LUMBERYARD for line in grid for c in line)
    return trees, lumberyards

if __name__=="__main__":
    grid = []
    with open("18.txt", 'r') as f:
        for line in f:
            grid.append([c for c in line.strip()])

    n = len(grid)

    grid2 = [[None]*n for _ in range(n)]

    minute = 0
    while minute < 10:
        evolve(n, grid, grid2)
        grid, grid2 = grid2, grid
        minute += 1

    # Part 1
    t, l = resource_value(grid)
    print('Part 1:',t*l)

    seen = dict()
    cycle_len = None
    while minute < int(1e9):
        evolve(n, grid, grid2)
        grid, grid2 = grid2, grid
        minute += 1

        s = make_str(grid)
        if s not in seen:
            seen[s] = minute
        elif cycle_len is None:
            cycle_len = minute - seen[s]
        else:
            if (int(1e9) - minute) % cycle_len == 0:
                # Part 2
                t, l = resource_value(grid)
                print('Part 2:',t*l)
                break