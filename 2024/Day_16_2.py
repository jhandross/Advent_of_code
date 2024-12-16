import heapq
from collections import defaultdict
import math

with open('16.txt') as f:
    grid = f.read().splitlines()

directions = {(-1, 0), (0, -1), (0, 1), (1, 0)}
walls = {(i, j) for i, line in enumerate(grid) for j, c in enumerate(line) if c == '#'}
start = next((i, j) for i, line in enumerate(grid) for j, c in enumerate(line) if c == 'S') + (0, 1)
end = next((i, j) for i, line in enumerate(grid) for j, c in enumerate(line) if c == 'E')
ends = [(end[0], end[1], dx, dy) for dx, dy in directions]

def dijkstra(start, ends, dist_func):
    visited, queue, dist = {}, [(0, start)], defaultdict(lambda: math.inf, {start: 0})
    while queue:
        time, loc = heapq.heappop(queue)
        if loc in visited: continue
        visited[loc] = 1
        if loc in ends: return time
        for (coord, d) in dist_func(loc):
            new_time = time + d
            if coord not in visited and new_time < dist[coord]:
                dist[coord] = new_time
                heapq.heappush(queue, (new_time, coord))

def dijkstra_multi(starts, dist_func):
    visited, queue, dist, output = {}, [(0, s) for s in starts], defaultdict(lambda: math.inf, {s: 0 for s in starts}), {}
    while queue:
        time, loc = heapq.heappop(queue)
        if loc in visited: continue
        visited[loc] = 1
        output[loc] = time
        for (coord, d) in dist_func(loc):
            new_time = time + d
            if coord not in visited and new_time < dist[coord]:
                dist[coord] = new_time
                heapq.heappush(queue, (new_time, coord))
    return output

def dist_func(loc):
    x, y, dx, dy = loc
    output = []
    if (x + dx, y + dy) not in walls: output.append(((x + dx, y + dy, dx, dy), 1))
    output.extend([((x, y, new_dx, new_dy), 1000) for new_dx, new_dy in directions if (new_dx, new_dy) != (dx, dy)])
    return output

answer = dijkstra(start, ends, dist_func)
print(answer)

dist_from_start = dijkstra_multi([start], dist_func)
dist_from_end = dijkstra_multi(ends, dist_func)

coords = {(x, y) for (x, y, dx, dy) in dist_from_start if dist_from_start[(x, y, dx, dy)] + dist_from_end[(x, y, -dx, -dy)] == answer}
print(len(coords))