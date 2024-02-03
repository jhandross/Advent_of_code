
PUZZLE = 361527

def part1(number: int) -> int:
    position = 0
    direction = -1j
    for i in range(1, number):
        x, y = position.real, position.imag
        # turn at the corners
        if x == y or (x == -y and x < 0) or (x == 1 - y and x > 0):
            direction *= 1j

        # move forward
        position += direction

    return abs(int(position.real)) + abs(int(position.imag))

first = part1(PUZZLE)



grid = {(0, 0): 1}

neighbours = lambda x, y: [(x+1, y), (x, y+1), (x+1, y+1), (x-1, y-1), (x-1, y), (x, y-1), (x+1, y-1), (x-1, y+1)]

def set_value(point):
    grid[point] = sum(grid.get(neighbour, 0) for neighbour in neighbours(*point))
    return grid[point]

def iterate_through_spiral(ring=0):
    while True:
        ring += 1
        for y in range(-ring + 1, ring): yield set_value((ring,  y))
        for x in range(ring, -ring, -1): yield set_value((x,  ring))
        for y in range(ring, -ring, -1): yield set_value((-ring, y))
        for x in range(-ring, ring + 1): yield set_value((x, -ring))

for value in iterate_through_spiral():
    if value > PUZZLE:
        second = value
        break


print('Part 1:', first)
print('Part 2:', second)