data = open('09.txt').read()
n, mmap, keys, emptys, idx = [], {}, [], [], 0

for i, v in enumerate(data):
    for _ in range(int(v)):
        n.append(' ' if i % 2 else i // 2)
    
    if i % 2 == 0:
        keys.append(i)
        mmap[i] = int(v) * [i // 2]
    else:
        emptys.append(i)
        mmap[i] = int(v) * [' ']
    idx += 1

# First part
idx, ide, p1 = 0, len(n) - 1, 0
while idx < len(n):
    while idx < len(n) and n[idx] != ' ':
        idx += 1
    while n[ide] == ' ':
        ide -= 1
    if idx > ide:
        break
    n[ide], n[idx] = n[idx], n[ide]
    idx += 1

for i, v in enumerate(n):
    if v != ' ':
        p1 += i * v
    if v == ' ':
        break

print(p1)

# Second part
for k in keys[::-1]:
    l = len(mmap[k])
    tr = []
    for i in emptys:
        if i > k: break
        l2 = mmap[i].count(' ')
        if l2 == 0: tr.append(i)
        if l <= l2:
            idx = mmap[i].index(' ')
            mmap[i] = mmap[i][:idx] + mmap[k] + (l2 - l) * [' ']
            mmap[k] = l * [' ']
            break
    for i in tr:
        emptys.remove(i)

l = [v for k in mmap for v in mmap[k]]

p2 = sum(i * v for i, v in enumerate(l) if v != ' ')
print(p2)
