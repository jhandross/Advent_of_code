import re
from sympy import solve


def read():
    with open("21.txt") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda r: r.replace(": ", " = "), s)


mv = [
    (-1, 0),  # U
    (1, 0),  # D
    (0, -1),  # L
    (0, 1),  # R
]


def subs(vars, s, var_a, var_b):
    s = s.replace(var_a, str(vars[var_a]))
    s = s.replace(var_b, str(vars[var_b]))
    return s


def prt1():
    solved = set([])
    root = None
    vars = {}
    while "root" not in solved:
        for row in t:
            start = row.split(" = ")[0]
            end = row.split(" = ")[1]
            if start in solved:
                continue
            if re.sub(r"[0-9\s]+", "", end) == "":
                vars[start] = eval(end)
                solved.add(start)
                continue
            parts = end.split(" ")
            var_a = parts[0]
            var_b = parts[-1]
            if var_a not in solved or var_b not in solved:
                continue
            vars[start] = eval(subs(vars, end, var_a, var_b))
            solved.add(start)

    print('Part 1:',int(vars["root"]))


def prt2():
    from sympy.core.sympify import sympify
    from sympy.parsing.sympy_parser import parse_expr
    from sympy import simplify

    statements = {}
    for row in t:
        start = row.split(" = ")[0]
        end = f"({row.split(' = ')[1]})"
        statements[start] = end
    statements["humn"] = " x "

    lhs, rhs = statements["root"].replace("(", "").replace(")", "").split("+")

    didrepl = True
    while didrepl:
        didrepl = False
        for key, value in statements.items():
            if key in lhs:
                didrepl = True
                lhs = lhs.replace(key, value)
    didrepl = True
    while didrepl:
        didrepl = False
        for key, value in statements.items():
            if key in rhs:
                didrepl = True
                rhs = rhs.replace(key, value)

    lhs = simplify(sympify(lhs))
    rhs = simplify(sympify(rhs))

    sol = solve(lhs - rhs)

    print('Part 2:',str(sol)[1:-1])


teststr = """"""

lmap = lambda *a: list(map(*a))
inf = float("inf")
t = read()

prt1()
prt2()
