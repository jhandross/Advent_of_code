data = open('01.txt').read().strip()
data = list(map(int, data))
 
def solve(digits, second_part=False):
    jump = 1 if not second_part else len(digits)//2
    return sum(n for i, n in enumerate(digits) if n == digits[i-jump])
 
print('Part 1:',solve(data))
print('Part 2:',solve(data, 'part 2'))