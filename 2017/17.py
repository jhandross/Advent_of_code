from collections import deque

puzzle=355

def spin(insertions):
    spinlock=deque([0])
    for i in range(1, insertions+1):
        spinlock.rotate(-puzzle)
        spinlock.append(i)
    return spinlock

res1=spin(2017)
print('Part 1:', res1[0])

res2=spin(50_000_000)
print('Part 2:', res2[res2.index(0)+1])