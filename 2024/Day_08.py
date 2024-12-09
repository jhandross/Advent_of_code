from itertools import combinations

grid = open('08.txt').read().splitlines()
board  = {complex(r,c) : ch for r,row in enumerate(grid) for c,ch in enumerate(row) }
groups = {v : [k for k in board if board[k] == v] for v in board.values() if v.isalnum() }

antinodes, antinodes_2 = set(), set()

for k in groups:
  for z1,z2 in combinations(groups[k], 2):
    d = z2 - z1
    antinodes.update( [z1 - d, z2 + d] )

    for z3 in board:
      if (z1.conjugate()*z2 + z2.conjugate()*z3 + z3.conjugate()*z1).imag == 0 :
        antinodes_2.add(z3)

print( len(antinodes & set(board)) )
print( len(antinodes_2) )