with open("02.txt") as f:
    l = f.read().split("\n")

x, y = 0, 0

for k in l:
    cmd, pwr = k.split()
    pwr = int(pwr)
    if cmd == "forward":
        x += pwr
    elif cmd == "down":
        y += pwr
    elif cmd == "up":
        y -= pwr

print('Part 1:',x * y)

x, y, aim = 0, 0, 0

for k in l:
    cmd, pwr = k.split()
    pwr = int(pwr)
    if cmd == "forward":
        x += pwr
        y += aim * pwr
    elif cmd == "down":
        aim += pwr
    elif cmd == "up":
        aim -= pwr

print('Part 2:',x * y)