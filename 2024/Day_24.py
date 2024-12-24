wires, ops, wrong = {}, [], set()

def process(op, a, b): return a & b if op == "AND" else a | b if op == "OR" else a ^ b

data, highest_z = open("24.txt").read().split("\n"), "z00"
for line in data:
    if ":" in line: wire, val = line.split(": "); wires[wire] = int(val)
    elif "->" in line:
        o1, op, o2, _, res = line.split(" "); ops.append((o1, op, o2, res))
        if res[0] == "z" and int(res[1:]) > int(highest_z[1:]): highest_z = res

for o1, op, o2, res in ops:
    if res[0] == "z" and op != "XOR" and res != highest_z: wrong.add(res)
    if op == "XOR" and not {o1[0], o2[0], res[0]} & {"x", "y", "z"}: wrong.add(res)
    if op == "AND" and "x00" not in [o1, o2]:
        wrong |= {res for s1, sop, s2, sres in ops if (res in [s1, s2]) and sop != "OR"}
    if op == "XOR":
        wrong |= {res for s1, sop, s2, sres in ops if (res in [s1, s2]) and sop == "OR"}

while ops:
    o1, op, o2, res = ops.pop(0)
    if o1 in wires and o2 in wires: wires[res] = process(op, wires[o1], wires[o2])
    else: ops.append((o1, op, o2, res))

print(int("".join(str(wires[w]) for w in sorted(wires, reverse=True) if w[0] == "z"), 2))
print(",".join(sorted(wrong)))