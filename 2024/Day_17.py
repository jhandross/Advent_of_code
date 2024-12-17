from re import findall
x, y, z, *instructions = map(int, findall(r"\d+", open("17.txt").read()))

def execute(program, x):
    pointer, y, z, output = 0, 0, 0, []
    while 0 <= pointer < len(program):
        arg, val = program[pointer + 1], [0, 1, 2, 3, x, y, z, 99999][program[pointer + 1]]
        match program[pointer]:
            case 0: x //= 2**val
            case 1: y ^= arg
            case 2: y = val % 8
            case 3: pointer = pointer if x == 0 else arg - 2
            case 4: y ^= z
            case 5: output.append(val % 8)
            case 6: y = x // 2**val
            case 7: z = x // 2**val
        pointer += 2
    return output

print("Part 1:", ",".join(map(str, execute(instructions, x))))

reverse_target = instructions[::-1]
def find_x(x=0, level=0):
    if level == len(reverse_target):
        return x
    for i in range(8):
        if (result := execute(instructions, x * 8 + i)) and result[0] == reverse_target[level]:
            if answer := find_x(x * 8 + i, level + 1):
                return answer
    return 0

print("Part 2:", find_x())