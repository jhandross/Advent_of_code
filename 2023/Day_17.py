import heapq

grid = {(x, y): int(n) for y, r in enumerate(open("17.txt")) for x, n in enumerate(r.strip())}

def sol(mn, mx):
    q, v, e = [(grid[1, 0], 1, 0, 1, 0, 0), (grid[0, 1], 0, 1, 0, 1, 0)], set(), max(grid)
    while q:
        h, x, y, dx, dy, s = heapq.heappop(q)
        if (x, y) == e and mn <= s: return h
        if (x, y, dx, dy, s) in v: continue
        v.add((x, y, dx, dy, s))
        if s < mx-1 and (p:=(x+dx, y+dy)) in grid: heapq.heappush(q, (h+grid[p], *p, dx, dy, s+1))
        if mn <= s:
            for xx, yy in [(dy, -dx), (-dy, dx)]:
                if (p:=(x+xx, y+yy)) in grid: heapq.heappush(q, (h+grid[p], *p, xx, yy, 0))

print(sol(0, 3))
print(sol(3, 10))