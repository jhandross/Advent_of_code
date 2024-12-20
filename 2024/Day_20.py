import numpy as np, time
t = time.time()
arr = np.array([list(l.strip()) for l in open('20.txt')])
dMap = np.zeros_like(arr, int)
ds, (i, j) = [(1, 0), (-1, 0), (0, 1), (0, -1)], [v[0] for v in np.where(arr == 'S')]
arr = np.isin(arr, ['E', '.'])
dMap[i, j] = c = 1
while any(arr[i+di, j+dj] and not dMap[i+di, j+dj] for di, dj in ds):
    for di, dj in ds:
        if arr[i+di, j+dj] and not dMap[i+di, j+dj]:
            c, dMap[i+di, j+dj], i, j = c + 1, c + 1, i + di, j + dj
            break
iG, jG = np.ogrid[:arr.shape[0], :arr.shape[1]]
i, j = np.where(dMap)
mDist = np.abs(i - iG[:, :, None]) + np.abs(j - jG[:, :, None])
res = dMap[:, :, None] - dMap[i, j] - mDist
print(np.sum(res[mDist <= 2] >= 100))
print(np.sum(res[mDist <= 20] >= 100))
print(time.time() - t)