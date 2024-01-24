# Part 1
with open('18.txt') as f:
    # Set up the board
    lights1 = { (x,y) for y, line in enumerate(f)
              for x, char in enumerate(line.strip())
              if char == '#' }

# This returns the number of neighbours that are turned on.
neighbours = lambda x,y: sum((_x,_y) in lights1 for _x in (x-1,x,x+1)
                            for _y in (y-1,y,y+1) if (_x, _y) != (x, y))

# Do 100 iterations
for c in range(100):
    # Calculate new 'lights1' from previous one
    lights1 = { (x,y) for x in range(100) for y in range(100)
              if (x,y) in lights1 and 2 <= neighbours(x,y) <= 3
              or (x,y) not in lights1 and neighbours(x,y) == 3 }
print (len(lights1))

# Part 2
# These need to stay on.
corners = {(0,0), (0,99), (99,0), (99,99)}
with open('18.txt') as f:
    # Set up the board (use set union to make sure corners are on)
    lights2 = corners | { (x,y) for y, line in enumerate(f)
                        for x, char in enumerate(line.strip())
                        if char == '#' }

# This returns the number of neighbours that are turned on.
neighbours = lambda x,y: sum((_x,_y) in lights2 for _x in (x-1, x, x+1)
                            for _y in (y-1, y, y+1) if (_x, _y) != (x, y))

# Do 100 iterations
for c in range(100):
    # Calculate new 'lights' from previous one, use a set union to make sure coners are turned 'on'
    lights2 = corners | { (x,y) for x in range(100) for y in range(100)
                        if (x,y) in lights2 and 2 <= neighbours(x,y) <= 3
                        or (x,y) not in lights2 and neighbours(x,y) == 3 }
print (len(lights2))