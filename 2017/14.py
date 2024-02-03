from collections import deque
from functools import reduce
from operator import xor
 
def knot_logic(sizes, iterations=64):
    circle = deque(range(256))
    skip = 0
    for _ in range(iterations):
        for group_size in sizes:
            knot = [circle.popleft() for _ in range(group_size)]
            circle += reversed(knot)
            circle.rotate(-skip)
            skip += 1
    unwind = iterations * sum(sizes) + skip * (skip-1) // 2
    circle.rotate(unwind)
    return list(circle)
 
 
def knot_hashing(word):
    ascii_sizes = [ord(c) for c in word] + [17, 31, 73, 47, 23]
    numbers = knot_logic(ascii_sizes)
    SIZE = 256
    BLOCK_SIZE = 16
    block = lambda i: numbers[i*BLOCK_SIZE : (i+1)*BLOCK_SIZE]
    dense = [reduce(xor, block(i)) for i in range(SIZE // BLOCK_SIZE)]
    return ''.join(f'{n:02x}' for n in dense)
 
 
instructions = 'hwlqcszp'
maze = set()
for row in range(128):
    word = f'{instructions}-{row}'
    hex_hash = knot_hashing(word)
    bin_hash = f'{int(hex_hash, 16):0128b}'
    for i, n in enumerate(bin_hash):
        if n == '1':
            maze.add((row, i))
print('Part 1:', len(maze))
 
def dfs(start):
    stack = [start]
    while stack:
        (x, y) = stack.pop()
        for dx, dy in DELTAS:
            candidate = x+dx, y+dy
            if candidate in maze:
                stack.append(candidate)
                maze.remove(candidate)
 
 
DELTAS = ((1, 0), (-1, 0), (0, 1), (0, -1))
regions = 0
while maze:
    dfs(maze.pop())
    regions += 1
print('Part 2:', regions)