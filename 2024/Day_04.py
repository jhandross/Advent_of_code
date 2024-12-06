def find_word(grid, y, x, word):
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    return sum(
        all(0 <= (ny := y + i * dy) < len(grid) and 0 <= (nx := x + i * dx) < len(grid[ny]) and grid[ny][nx] == word[i]
            for i in range(len(word)))
        for dy, dx in directions
    )

with open("04.txt") as file:
    grid = file.read().splitlines()

found1, found2 = 0, 0
for y, row in enumerate(grid):
    for x, letter in enumerate(row):
        found1 += find_word(grid, y, x, "XMAS")
        if letter == "A" and 0 < y < len(grid) - 1 and 0 < x < len(row) - 1:
            neighbors = [grid[y - 1][x - 1] + grid[y + 1][x + 1], grid[y + 1][x - 1] + grid[y - 1][x + 1]]
            found2 += all(pair in ("MS", "SM") for pair in neighbors)

print(found1)
print(found2)
