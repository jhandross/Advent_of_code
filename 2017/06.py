from collections import OrderedDict

data=open('06.txt').read().split()
data=list(map(int, data))

size=len(data)
seen=OrderedDict()

while tuple(data) not in seen:
    seen[tuple(data)]=None
    max_value=max(data)
    max_index=data.index(max_value)
    data[max_index]=0
    to_every, to_some=divmod(max_value, size)
    data=[d+to_every for d in data]
    for i in range(to_some):
        data[(max_index+i+1)%size]+=1

print('Part 1:',len(seen))

loop_start=list(seen.keys()).index(tuple(data))
print('Part 2:',len(seen)-loop_start)