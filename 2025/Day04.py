import numpy as np
from scipy.signal import convolve2d

grid = np.array([[*x.strip()] for x in open('day04.txt')]) == '@'
orig = grid.copy()

for i in range(101):
    grid &= convolve2d(grid, np.ones((3,3)), mode='same') > 4
    if i in [0, 100]: print(orig.sum() - grid.sum())