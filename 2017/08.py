from collections import defaultdict
from operator import lt, gt, eq, ne, le, ge

data=open('08.txt', 'r').read().splitlines()

regists=defaultdict(int)
opers={
    '<':lt,
    '>':gt,
    '==':eq,
    '!=':ne,
    '<=':le,
    '>=':ge
}
maxi=0

for line in data:
    regist, instruct, cant, _, cond_reg, operator, valor = line.split()
    direccion=1 if instruct =='inc' else -1
    if opers[operator](regists[cond_reg], int(valor)):
        regists[regist] += direccion*int(cant)
        maxi=max(regists[regist], maxi)

print('Part 1:',max(regists.values()))
print('Part 2:',maxi)