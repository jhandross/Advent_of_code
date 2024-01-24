def solve(data, groups):
    def aux(presents, score, used, qe):
        if score == goal:
            possible_solutions.add((used, qe))
        elif score < goal and presents and used < 6:
            aux(presents[1:], score, used, qe)
            aux(presents[1:], score+presents[0], used+1, qe*presents[0])

    possible_solutions = set()
    goal = sum(data) // groups
    aux(data, 0, 0, 1)
    return min(possible_solutions)[1]


data = sorted(map(int, open("24.txt").read().splitlines()), reverse=True)

print('Part 1:',solve(data, 3))
print('Part 2:',solve(data, 4))