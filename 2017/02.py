data = open('02.txt').read().splitlines()
delta1 = 0
delta2 = 0
nums = []
for line in data:
    nums = line.split('\t')
    nums = list(map(int, nums))
    delta1 += max(nums) - min(nums)
    for a in nums:
        for b in nums:
            if a % b == 0 and a != b:
                delta2 += a // b
print('Part 1:',delta1)
print('Part 2:',delta2)