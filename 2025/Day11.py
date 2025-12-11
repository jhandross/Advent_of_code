from functools import cache
g={s:t.split() for s,t in (l.strip().split(': ') for l in open('day11.txt'))}

@cache
def count(s): return 1 if s=='out' else sum(count(n) for n in g[s])

@cache
def count2(s,f):
    if s=='out': return f==('dac','fft')
    if s in('dac','fft'): f=tuple(sorted(set(f)|{s}))
    return sum(count2(n,f) for n in g[s])

print(count('you')); print(count2('svr',()))