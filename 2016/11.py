# from bovard
items_part_one = [4, 5, 1, 0]
items_part_two = [8, 5, 1, 0]


def get_moves(items):

    moves = 0
    while items[-1] != sum(items):
        # print moves, items
        lowest_floor = 0
        while items[lowest_floor] == 0:
            lowest_floor += 1
        moves += 2 * (items[lowest_floor] - 1) - 1
        items[lowest_floor + 1] += items[lowest_floor]
        items[lowest_floor] = 0
    return moves


print('Part 1:',get_moves(items_part_one))

print('Part 2:',get_moves(items_part_two))