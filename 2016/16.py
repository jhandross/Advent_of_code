START = list(map(int, '11011110011011101'))
DISK_1 = 272
DISK_2 = 35651584


def fill_disk(data, disk_size):
    while len(data) < disk_size:
        new = [1-i for i in reversed(data)]
        data.append(0)
        data.extend(new)
    return data[:disk_size]


def create_checksum(data):
    while len(data) % 2 == 0:
        data = [a == b for a, b in zip(data[::2], data[1::2])]
    return ''.join(map(str, map(int, data)))


first = create_checksum(fill_disk(START, DISK_1))
second = create_checksum(fill_disk(START, DISK_2))

print("Part 1:", first)
print("Part 2:", second)