turns=[l.strip() for l in open('day01.txt')]
moves=[(t[0],int(t[1:])) for t in turns]

# PART 1
p=z=50,0; p,z=50,0
for d,n in moves:
    p=(p+(-n if d=='L' else n))%100
    z+=p==0
print("Result 1:",z)

# PART 2  (correct version)
p=z=50,0; p,z=50,0
for d,n in moves:
    if d=='L':
        if p-n<0:
            z+=abs((100+p-n)//100)
            if p!=0: z+=1
        p=(p-n)%100
        z+=p==0
    else:  # R
        z+=(p+n)//100
        p=(p+n)%100
print("Result 2:",z)
