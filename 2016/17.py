from collections import deque
from hashlib import md5


INPUT = 'pvhmgsws'
VAULT = 3+3j


def find_vault():
    solutions = []
    que = deque([(0+0j, '')])

    while que:
        pos, path = que.popleft()

        if pos == VAULT:
            solutions.append(path)
            continue

        u, d, l, r = md5((INPUT+path).encode()).hexdigest()[:4]

        if u > 'a' and pos.imag > 0:
            que.append((pos-1j, path+'U'))
        if d > 'a' and pos.imag < 3:
            que.append((pos+1j, path+'D'))
        if l > 'a' and pos.real > 0:
            que.append((pos-1, path+'L'))
        if r > 'a' and pos.real < 3:
            que.append((pos+1, path+'R'))

    return solutions[0], len(solutions[-1])


first, second = find_vault()

print(f"Part 1: {first}")
print(f"Part 2: {second}")