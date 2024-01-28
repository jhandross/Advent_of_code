import re

# **Part 1

data = open('22.txt').read().splitlines()
data = data[2:]
 
nodes = []
pattern = "^\/dev\/grid\/node-x(?P<x>[0-9]+)-y(?P<y>[0-9]+)\s+(?P<size>[0-9]+)T\s+(?P<used>[0-9]+)T\s+(?P<available>[0-9]+)T\s+(?P<use>[0-9]+)%"
 
for line in data:
    match = re.match(pattern, line)
    nodes.append (match.groupdict())
#print (nodes)
 
minX = min(nodes, key=lambda d: int(d["x"]))["x"]
maxX = max(nodes, key=lambda d: int(d["x"]))["x"]
minY = min(nodes, key=lambda d: int(d["y"]))["y"]
maxY = max(nodes, key=lambda d: int(d["y"]))["y"]
 
total_pairs = 0
for node in nodes:
  for node2 in nodes:
    if node["x"] != node2["x"] or node["y"] != node2["y"]:
      if int(node["used"]) != 0:
        if int(node["used"]) <= int(node2["available"]):
          total_pairs+=1
 
print('Part 1:',total_pairs)


# **Part 2
 
from collections import deque
from dataclasses import dataclass
 
START: complex = 0j
LINE_PATTERN: re.Pattern = re.compile(r".*x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T.*")
 
State = tuple[complex, complex]
 
@dataclass
class Node:
    coord: complex
    size: int
    used: int
 
    @property
    def avail(self) -> int:
        return self.size - self.used
 
    @classmethod
    def from_line(cls, line: str) -> "Node":
        match = LINE_PATTERN.match(line)
        if not match:
            raise Exception(f"wat: {line}")
 
        x, y, size, used, avail = [int(x) for x in match.groups()]
        if size != used + avail:
            raise Exception(f"wat2: {line}")
 
        return cls(x + 1j * y, size, used)
 
 
def get_neighbours(empty_space: complex, max_coord: complex, immovables: set[complex]) -> list[complex]:
    maybe_neighbours = set(
        empty_space + dx + 1j * dy
        for dx in (-1, 0, 1)
        for dy in (-1, 0, 1)
        if 0 <= empty_space.real + dx <= max_coord.real
        and 0 <= empty_space.imag + dy <= max_coord.imag
        and (dx == 0) != (dy == 0)
    )
    return maybe_neighbours.difference(immovables)
 
 
def solve(nodes: list[Node]) -> int:
    movable_capacity: int = 0
    empty_space: complex = 0j
 
    for node in nodes:
        if node.used == 0:
            movable_capacity = node.size
            empty_space = node.coord
            break
 
    immovables: set[complex] = set()
    max_coord: complex = 0j
    for node in nodes:
        if node.used > movable_capacity:
            immovables.add(node.coord)
        max_coord = max(max_coord.real, node.coord.real) + 1j * max(
            max_coord.imag, node.coord.imag
        )
 
    goal = max_coord.real + 0j
 
    state = (goal, empty_space)
    to_visit: deque = deque([state])
    visited: dict[State, int] = {state: 0}
 
    while to_visit:
        state = to_visit.popleft()
        goal, empty_space = state
        steps = visited[state]
        new_steps = steps + 1
        empty_neighbours = get_neighbours(empty_space, max_coord, immovables)
        for empty_neighbour in empty_neighbours:
            if empty_neighbour == goal:
                if empty_space == 0j:
                    # print("Finished!")
                    return new_steps
                new_state = (empty_space, goal)
            else:
                new_state = (goal, empty_neighbour)
 
            if new_state not in visited:
                visited[new_state] = new_steps
                to_visit.append(new_state)
 
    print("Finished search without finding solution")
 
 
data = open('22.txt').read().splitlines()
data = data[2:]
nodes: list[Node] = ([Node.from_line(d) for d in data])
# print(nodes)
 
print("Part 2:", solve(nodes))