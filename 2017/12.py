from collections import deque
 
data = open('12.txt').readlines()
 
graph = {}
 
for line in data:
    pipe, neighbours = line.split(' <-> ')
    pipe = int(pipe)
    neighbours = [int(n) for n in neighbours.split(', ')]
    graph[pipe] = neighbours
 
 
def bfs(starting_point):
    connections = set()
    que = deque([starting_point])
    while que:
        current = que.popleft()
        connections.add(current)
        for node in graph[current]:
            if node not in connections:
                que.append(node)
    return connections
 
 
seen = bfs(0)
islands = 1
first_island_size = len(seen)
 
for pipe in graph:
    if pipe not in seen:
        pipe_island = bfs(pipe)
        islands += 1
        seen |= pipe_island
 
print('Part 1:',first_island_size)
print('Part 2:',islands)