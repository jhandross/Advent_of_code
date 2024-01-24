import ast

with open('08.txt') as input:
    lines=input.read().split()
    
print(lines)

parte1=sum(len(line) - len(ast.literal_eval(line)) for line in lines)
parte2=sum(2+line.count('\\') + line.count('"') for line in lines)

print(parte1)
print(parte2)