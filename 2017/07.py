from collections import Counter
import re
data = open('07.txt').read().splitlines()
weights = {}
children = {}
for line in data:
    node, weight, *kids = re.findall(r"(\w+)", line)
    weights[node] = int(weight)
    children[node] = kids

 
all_nodes = set(weights)
all_kids = {kid for kids in children.values() for kid in kids}
root = (all_nodes - all_kids).pop()
print('Part 1:',root)
 
def find_offsprings_weights(node):
    kids_weights = [find_offsprings_weights(kid) for kid in children[node]]
    unique_weights = Counter(kids_weights).most_common()
    if len(unique_weights) == 2:
        (correct_total, _), (wrong_total, _) = unique_weights
        difference = correct_total - wrong_total
        wrong_node = children[node][kids_weights.index(wrong_total)]
        wrong_weight = weights[wrong_node]
        print('Part 2:',wrong_weight + difference)
        return weights[node] + sum(kids_weights) + difference
    return weights[node] + sum(kids_weights)
 
find_offsprings_weights(root)