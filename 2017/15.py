data = open('15.txt').read().splitlines()
data = [line.split(' ') for line in data]
a = int(data[0][4])
b = int(data[1][4])
 
factors = {'a': 16807, 'b': 48271}
divisor = 2147483647
 
def generator(value, factor, multi=1):
    while True:
        value = value * factor % divisor
        if value % multi == 0:
            yield value & 0xFFFF
 
 
gen_a = generator(a, factors['a'])
gen_b = generator(b, factors['b'])
ans = sum(next(gen_a) == next(gen_b) for _ in range(40_000_000))
print('Part 1:', ans)
 
gen_a = generator(a, factors['a'], 4)
gen_b = generator(b, factors['b'], 8)
ans = sum(next(gen_a) == next(gen_b) for _ in range(5_000_000))
print('Part 2:', ans)