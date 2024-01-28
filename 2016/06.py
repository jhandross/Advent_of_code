from collections import Counter

with open('06.txt', 'r') as infile:
    noise = infile.readlines()

columns = (''.join(column) for column in zip(*noise))

first_solution = ''
second_solution = ''

for column in columns:
    (most, _), *others, (least, _) = Counter(column).most_common()
    first_solution += most
    second_solution += least

print("El mensaje suele estar formado por las letras más frecuentes....")
print("Part 1:", first_solution)
print("¿O son las letras menos frecuentes? Quién sabe....")
print("Part 2:", second_solution)