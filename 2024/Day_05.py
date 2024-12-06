from functools import cmp_to_key

with open('05.txt') as file:
    rules_raw, manuals_raw = file.read().split('\n\n')
    rules = set(rules_raw.splitlines())
    manuals = [[int(x) for x in line.split(',')] for line in manuals_raw.splitlines()]

compare = cmp_to_key(lambda a, b: -1 if f"{a}|{b}" in rules else 0)
sorted_pages = lambda manual: sorted(manual, key=compare)
get_mid = lambda items: items[len(items) // 2]

part1 = sum(get_mid(m) for m in manuals if sorted_pages(m) == m)
part2 = sum(get_mid(sorted_pages(m)) for m in manuals) - part1

print(part1)
print(part2)