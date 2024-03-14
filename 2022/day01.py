with open('01.txt') as f:
    elves=sorted(sum(map(int, elf.splitlines())) for elf in f.read().split('\n\n'))
    print('Part 1:', elves[-1])
    print('Part 2:', sum(elves[-3:]))