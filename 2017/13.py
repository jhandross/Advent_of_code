import itertools
 
data = open('13.txt').read().splitlines()
lines = [line.split(': ') for line in data]
heights = {int(pos): int(height) for pos, height in lines}
 
def scanner(height, time):
    offset = time % ((height - 1) * 2)
 
    return 2 * (height - 1) - offset if offset > height - 1 else offset

pt1=sum(pos * heights[pos] for pos in heights if scanner(heights[pos], pos) == 0)
pt2=next(wait for wait in itertools.count() if not any(scanner(heights[pos], wait + pos) == 0 for pos in heights))

print('Part 1:', pt1)
print('Part 2:', pt2)