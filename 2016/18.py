with open('18.txt', 'r') as infile:
    first_row = infile.read()


def count_safes(row, total_lines):
    safe = 0
    for i in range(total_lines):
        if i == 40:
            first_solution = safe
        safe += row.count('.')
        old = '.' + row + '.'
        row = ''
        for left, right in zip(old, old[2:]):
            row += '^' if left != right else '.'
    return first_solution, safe


first, second = count_safes(first_row, 400000)

print(f"Part 1: {first}")
print(f"Part 2: {second}")