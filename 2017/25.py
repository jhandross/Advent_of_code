from collections import defaultdict

lines = open('25.txt').read().strip().split('\n')
state = lines[0].split()[-1][:-1]
T = 12683008
rules = defaultdict(dict)

rule_state = chr(ord('A')-1)
for i in range(5, len(lines), 10):
    rule_state = chr(ord(rule_state)+1)
    def symbol(s):
        return int(s.split()[-1][:-1])
    def move(s):
        return -1 if s.split()[-1]=='left.' else 1
    def extract_state(s):
        return s.split()[-1][:-1]
    rules[rule_state][0] = (symbol(lines[i]), move(lines[i+1]), extract_state(lines[i+2]))
    rules[rule_state][1] = (symbol(lines[i+4]), move(lines[i+5]), extract_state(lines[i+6]))
# print (state, T)
# print (rules)

tape = defaultdict(int)
pos = 0

for t in range(T):
    #print state, tape[pos]
    new_symbol, new_move, new_state = rules[state][tape[pos]]
    tape[pos] = new_symbol
    state = new_state
    pos += new_move

ans = 0
for k,v in tape.items():
    if v==1:
        ans += 1
print (ans)