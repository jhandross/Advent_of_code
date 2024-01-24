import json

with open('input.json', 'r') as j:
    doc=json.load(j)
    
def sum_of_item(item, part2=False):
    if type(item)==list:
        return sum(sum_of_item(i, part2) for i in item)
    if type(item)==dict:
        if part2 and 'red' in item.values():
            return 0
        return sum([sum_of_item(i, part2) for i in item.values()])
    if type(item)==str:
        return 0
    if type(item)==int:
        return item

print(f'Parte 1: {sum_of_item(doc)}')
print(f'Parte 2: {sum_of_item(doc, part2=True)}')