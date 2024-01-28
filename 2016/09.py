import re

with open('09.txt', 'r') as f:
    compressed = f.read()

pattern = re.compile(r'\((\d+)x(\d+)\)')

def unzip(s, part2=False):
    parens = pattern.search(s)
    if not parens:
        return len(s)
    length = int(parens.group(1))
    times = int(parens.group(2))
    start = parens.start() + len(parens.group())
    count = unzip(s[start:start+length], True) if part2 else length

    return (len(s[:parens.start()])
            + times * count
            + unzip(s[start+length:], part2))


print()
print(f"Part 1: {unzip(compressed)}")
print(f"Part 2: {unzip(compressed, part2=True)}")