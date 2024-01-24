import hashlib

key='bgvyzdsv'

def solucion(parte2=False):
    num=0
    while True:
        res=hashlib.md5((key+str(num)).encode())
        if (not parte2 and res.hexdigest()[:5]=='00000') or (parte2 and res.hexdigest()[:6]=='000000'):
            return num
        num+=1
        
print(f'Parte 1: {solucion()}')
print(f'Parte 2: {solucion(True)}')