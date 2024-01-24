import string
import re

# my puzzle input:
pw = 'vzbxkghb'  

def check_pw(pw):
    ''' comprueba si pw tiene dos letras repetidas que no se superponen y una letra alfabética'''
    if len(re.findall(r'([a-z])\1', pw)) >= 2 and any(pw[i:i+3] in alphabet for i in range(6)):
        return True
    
def increment(pw):
    '''incrementa alfabéticamente pw de derecha a izquierda'''
    pw = list(pw)
    for i in range(7, -1, -1):
        next_index = (altered_alphabet.index(pw[i]) + 1) % 23
        pw[i] = altered_alphabet[next_index]
        if pw[i] != 'a':
            return ''.join(pw)

def get_next(pw):
    '''Incrementa pw hasta que encuentre una válida'''
    while not check_pw(pw):
        pw = increment(pw)
    return pw

alphabet = string.ascii_lowercase
altered_alphabet = re.sub('[iol]', '', alphabet) # eliminando letras prohibidas

part1 = get_next(pw)
part2 = get_next(increment(part1))

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')