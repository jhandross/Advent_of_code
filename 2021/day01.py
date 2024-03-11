depths = [int(line.strip()) for line in open('01.txt')]


num_increases = sum(1 for i in range(1, len(depths)) if depths[i] > depths[i - 1])
print('Part 1:',num_increases)


depth_sums = [depths[i] + depths[i + 1] + depths[i + 2] for i in range(len(depths) - 2)]
num_increases = sum(1 for i in range(1, len(depth_sums)) if depth_sums[i] > depth_sums[i - 1])


print('Part 2:',num_increases)