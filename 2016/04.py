with open('04.txt', 'r') as infile:
    all_rooms = infile.read().splitlines()

rooms = ((room[:-11].replace('-', ''),
          int(room[-10:-7]),
          room[-6:-1]
         ) for room in all_rooms)


def find_most_common(name):
    ranking = sorted((-name.count(letter), letter) for letter in set(name))
    return ''.join(letter for _, letter in ranking[:5])


def find_rooms():
    total = 0
    for name, sector, ch_sum in rooms:
        if find_most_common(name) == ch_sum:
            total += sector
            decrypted_name = ''.join(chr((ord(letter) - 97 + sector) % 26 + 97)
                                     for letter in name)
            if decrypted_name.startswith('northpole'):
                wanted_room = (sector, decrypted_name)
    return total, wanted_room


total, (sector, name) = find_rooms()

print(f"Part 1: {total}")
print(f"Part 2: {sector}")