import re

bots = [tuple(map(int, re.findall(r'-?\d+', l))) for l in open('14.txt')]
ffwd = lambda p, q, r, s: ((p + r * t) % 101 - 50, (q + s * t) % 103 - 51)

w, h, t = 101, 103, 100
a = b = c = d = 0

for bot in bots:
    p, q = ffwd(*bot)
    a += p > 0 and q > 0
    b += p > 0 and q < 0
    c += p < 0 and q > 0
    d += p < 0 and q < 0

print(a * b * c * d)

for t in range(10000):
    if len(set(ffwd(*b) for b in bots)) == len(bots): print(t); break
