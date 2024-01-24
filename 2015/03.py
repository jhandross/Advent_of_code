with open('03.txt') as f:
    moves=f.read()
    
def coord_visitadas(moves: str=moves, x: int=0, y: int=0):
    direcciones={'v': (0,-1), '^': (0,1), '<': (-1,0), '>': (1,0)}
    visitado={(x,y)}
    for move in moves:
        x+=direcciones[move][0]
        y+=direcciones[move][1]
        visitado.add((x,y))
    return visitado

print('Parte 1:', len(coord_visitadas()))
santa, robo = moves[0::2], moves[1::2]
parte2 = len(coord_visitadas(santa).union(coord_visitadas(robo)))
print('Parte 2:', parte2)
