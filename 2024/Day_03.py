import re

with open('03.txt') as f:
    mega_line = f.read().replace('\n', '')

def find_multiply_pairs(text):
    return sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", text))

# Part 1
print(f"Part 1: {find_multiply_pairs(mega_line)}")

# Part 2
mul_result = find_multiply_pairs(mega_line.split("don't()")[0])

for block in mega_line.split("don't()")[1:]:
    if 'do()' in block:
        mul_result += find_multiply_pairs(block.split('do()', 1)[1])

print(f"Part 2: {mul_result}")
