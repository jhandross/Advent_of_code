

input = list(
    map(int, open('01.txt').read().splitlines())
)

currents = dict()
current = 0
done = False
print('Part 1:',sum(input))
while not done:
    for i in input:
        current += i
        if currents.get(current, False):
            print('Part 2:',current)
            done = True
            break
        currents[current] = True