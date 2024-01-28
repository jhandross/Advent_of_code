import numpy as np
import matplotlib.pyplot as plt

with open('08.txt', 'r') as infile:
    instructions = infile.read().split('\n')

lcd = np.zeros((6, 50))

for line in instructions:
    if line.startswith('rect'):
        width, height = map(int, line.split()[1].split('x'))
        lcd[:height, :width] = 1
    elif line.startswith('rotate'):
        _, ax, pos, _, shift = line.split()
        pos = int(pos.split('=')[1])
        shift = int(shift)
        if ax == 'row':
            lcd[pos] = np.roll(lcd[pos], shift)
        else:
            lcd[:, pos] = np.roll(lcd[:, pos], shift)

print()
print('Part 1: {:0.0f}'.format(np.sum(lcd)))
print()
print('Part 2:')
print('\n'.join(' '.join('#' if on else ' ' for on in line) for line in lcd))
print()