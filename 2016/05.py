#first solution
door_id = 'cxdnnyjw'
import hashlib

first_password = ''
second_password = [''] * 8
available_positions = set('01234567')

i = 0
while available_positions:
    char_input = (door_id + str(i)).encode()
    md5_hex = hashlib.md5(char_input).hexdigest()

    if md5_hex.startswith(5*'0'):
        if len(first_password) < 8:
            first_password += md5_hex[5]
        if md5_hex[5] in available_positions:
            second_password[int(md5_hex[5])] = md5_hex[6]
            available_positions.remove(md5_hex[5])
    i += 1

print("Part 1:", first_password)
print("Part 2:", ''.join(second_password))

#second solution
import hashlib
import time
t=time.time()
ip='cxdnnyjw'
ans=''
ans2='????????'
for i in range(10**8):
    h=hashlib.md5((ip+str(i)).encode()).hexdigest()
    if h.startswith('00000'):
        pos=h[5]
        ans=ans+pos
        if pos in '01234567' and ans2[int(pos)]=='?':
            ans2=ans2[:int(pos)]+h[6]+ans2[int(pos)+1:]
            if ans2.find('?')==-1:
                break
print('ans1:',ans[:8])
print('ans2:',ans2)
print('Time:',time.time()-t)
print('no of loop',i)
