from collections import defaultdict

data = [line.strip() for line in open('05.txt') if line.strip()]
rules = defaultdict(set)

[rules[a].add(b) for line in data if '|' in line for a, b in [map(int, line.split('|'))]]
updates = [list(map(int, line.split(','))) for line in data if ',' in line]
is_correct = lambda u: all(not (set(u[:i]) & rules[u[i]]) for i in range(len(u)))

ans1 = sum(u[len(u) // 2] for u in updates if is_correct(u))
ans2 = sum(next(n for n in update if len(rules[n] & set(update)) == len(update) // 2)
           for update in updates if not is_correct(update))

print(f"{ans1}\n{ans2}")
