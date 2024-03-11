from collections import defaultdict


fish = [3, 4, 3, 1, 2]
fish = [int(f) for f in open('06.txt').readline().split(',')]


def simulate_fish_population(fish, days):
    for _ in range(days):
        new_fish = []
        for fish in fish:
            if fish == 0:
                new_fish.append(6)
                new_fish.append(8)
            else:
                new_fish.append(fish - 1)
        fish = new_fish
    return fish


def calculate_fish_population(fish, days):
    born_at = defaultdict(lambda: 0)

    for fish_individual in fish:
        born_at[fish_individual] += 1
    for day in range(days):
        born_at[day] = born_at[day] + born_at[day - 7] + born_at[day - 9]
    return sum(born_at.values()) + len(fish)


print("Part 1:", len(simulate_fish_population(fish, 80)))
print("Part 2:", calculate_fish_population(fish, 256))
