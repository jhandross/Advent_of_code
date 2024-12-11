with open('10.txt') as f:
    grid = {x + y * 1j: int(c) for y, line in enumerate(f) for x, c in enumerate(line.strip())}

def get_score(p, distinct=False):
    q, seen, score = [p], set(), 0
    while q:
        pos = q.pop(0)
        if pos in seen: continue
        if not distinct: seen.add(pos)
        if (e := grid[pos]) == 9: score += 1; continue
        q += [pos + d for d in [1, -1, 1j, -1j] if grid.get(pos + d) == e + 1]
    return score

trailheads = [p for p, v in grid.items() if v == 0]
print(sum(get_score(p) for p in trailheads))
print(sum(get_score(p, True) for p in trailheads))