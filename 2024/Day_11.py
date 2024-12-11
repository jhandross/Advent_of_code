with open('11.txt') as f:
    data = [int(x) for x in f.read().split()]

def update_stone(s):
  ss = str(s)
  return (1,) if s == 0 else (int(ss[:len(ss)//2]), int(ss[len(ss)//2:])) if len(ss) % 2 == 0 else (s * 2024,)

def dfs(mem, val, blinks):
  if blinks == 0: return 1
  if (val, blinks) in mem: return mem[(val, blinks)]
  mem[(val, blinks)] = sum(dfs(mem, el, blinks-1) for el in update_stone(val))
  return mem[(val, blinks)]

def run(n):
  return sum(dfs({}, stone, n) for stone in data)

part1 = lambda: run(25)
part2 = lambda: run(75)

print(part1())
print(part2())