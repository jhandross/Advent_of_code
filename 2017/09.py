data=open('09.txt', 'r').read().strip()

garb_clear=0
nest_level=0
restult=0
i=0

while i < len(data):
    if data[i] == '<':
        i+=1
        while data[i] != '>':
            if data[i] == '!':
                i+=1
            else:
                garb_clear+=1
            i+=1
    elif data[i] == '{':
        nest_level+=1
    elif data[i] == '}':
        restult+=nest_level
        nest_level-=1
    i+=1

print('Part 1:',restult)
print('Part 2:',garb_clear)