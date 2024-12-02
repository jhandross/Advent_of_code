import pandas as pd, collections as c

with open("01.txt", encoding="utf-8") as f:
    l, r = zip(*(map(int, line.split()) for line in f))

l, r = sorted(l), sorted(r)
df = pd.DataFrame({'Value': [sum(abs(a - b) for a, b in zip(l, r)), sum(a * c.Counter(r)[a] for a in l)]})
print(df)
