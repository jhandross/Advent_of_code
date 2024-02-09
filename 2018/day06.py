import numpy as np
from scipy.spatial.distance import cdist

def day06(inp, thresh=10000):
    coords = np.array([list(map(int, line.split(','))) for line in inp])
    
    coords -= coords.min(0)
    w,h = coords.max(0) + 1
    
    pxpy = np.mgrid[:w, :h].transpose(1,2,0).reshape(-1,2)
    dists = cdist(pxpy, coords, 'cityblock').astype(int)

    # part 1:
    nearests = dists.argmin(-1)
    points = nearests.reshape(w, h)

    tieds = (dists == dists.min(-1, keepdims=True)).sum(-1) > 1
    points.flat[tieds] = -1

    maxval = 0
    for i in range(points.max() + 1):
        xposes,yposes = (points == i).nonzero()
        if xposes.min() == 0 or xposes.max() == w - 1 or yposes.min() == 0 or yposes.max() == h - 1:
            points[points == i] = -1
            continue

        valnow = (points == i).sum()
        maxval = max(valnow, maxval)

    # part 2:
    totals = dists.sum(-1)
    goodcount = (totals < thresh).sum()

    return maxval,goodcount


if __name__ == "__main__":
    inp = open('06.txt').readlines()
    print('(Prt1:, Prt2:)')
    print(day06(inp))