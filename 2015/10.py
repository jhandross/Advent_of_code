# solution using itertools
import itertools

# my puzzle input:
input_num = '1321131112'

def look_and_say(num, iterations):
    for _ in range(iterations):
        num = ''.join(str(len(list(g))) + str(n) for n, g in itertools.groupby(num))
    return num

first_num = look_and_say(input_num, 40)
second_num = look_and_say(first_num, 10)


print(f'Part 1: {len(first_num)}')
print(f'Part 2: {len(second_num)}')