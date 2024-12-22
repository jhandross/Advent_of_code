from time import time

time_start = time()
numbers = [int(line.rstrip("\n")) for line in open('22.txt')]

MOD, N = 16777216, 2_000

def update(x):
    x = (x ^ (x << 6)) % MOD
    x = (x ^ (x >> 5)) % MOD
    return (x ^ (x << 11)) % MOD

x, b, d, seen, res = [0] * (N + 1), [0] * (N + 1), [0] * (N + 1), [0] * (1 << 20), [0] * (1 << 20)
ans1 = 0

for buyer_id, secret_number in enumerate(numbers, 1):
    x[0], b[0] = secret_number, secret_number % 10
    for i in range(1, N + 1):
        x[i] = update(x[i - 1])
        b[i] = x[i] % 10
        d[i] = b[i] - b[i - 1]

    ans1 += x[N]

    for i in range(4, N + 1):
        h = ((d[i - 3] + 9) << 15) | ((d[i - 2] + 9) << 10) | ((d[i - 1] + 9) << 5) | (d[i] + 9)
        if seen[h] != buyer_id:
            seen[h], res[h] = buyer_id, res[h] + b[i]

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")
print(f"part 2: {max(res)}  ({time() - time_start:.3f}s)")
