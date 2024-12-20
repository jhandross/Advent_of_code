from bisect import bisect_left

data = [tuple(map(int, line.split(","))) for line in open("18.txt").read().split()]
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(delay=1024, W=70):
    blocks, seen, step, boundary = set(data[:delay]), set(), 0, {(0, 0)}
    while boundary:
        newb = {(y+dy, x+dx) for y, x in boundary if (y, x) not in seen 
                for dy, dx in DIRS if 0 <= y+dy <= W >= x+dx >= 0 and (y+dy, x+dx) not in blocks}
        if (W, W) in boundary: return step
        seen |= boundary
        boundary, step = newb, step + 1
    return 0

print(bfs())
print(*data[bisect_left(range(len(data)), True, key=lambda i: not bfs(i))-1], sep=",")