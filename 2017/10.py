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
 
 
data = open('10.txt').read().strip()
int_sizes = [int(n) for n in data.split(',')]
 
first_hash = knot_logic(int_sizes, iterations=1)

print('Part 1:',first_hash[0]*first_hash[1])
print('Part 2:',knot_hashing(data))