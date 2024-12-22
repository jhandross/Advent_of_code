from collections import Counter

lines = open("21.txt").read().split("\n")
kp = {c: (i % 3, i // 3) for i, c in enumerate("789456123 0A")}
dp = {c: (i % 3, i // 3) for i, c in enumerate(" ^A<v>")}

def step(m, seq, inc=1):
    px, py, bx, by = *m["A"], *m[" "]
    res = Counter()
    for c in seq:
        npx, npy = m[c]
        f = (npx == bx and py == by) or (npy == by and px == bx)
        res[(npx - px, npy - py, f)] += inc
        px, py = npx, npy
    return res

def calc(n):
    total = 0
    for line in lines:
        res = step(kp, line)
        for _ in range(n + 1):
            new_res = Counter()
            for x, y, f in res:
                new_res += step(dp, ("<" * -x + "v" * y + "^" * -y + ">" * x)[::-1 if f else 1] + "A", res[(x, y, f)])
            res = new_res
        total += sum(res.values()) * int(line[:3])
    return total

print(calc(2))
print(calc(25))