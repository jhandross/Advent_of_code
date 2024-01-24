#!/usr/bin/env python3

import re

ingr = {}
igrs = []

with open("15.txt") as f:
	for l in f.readlines():
		line = l.strip()
		ingredient, _, capacity, _, durability, _, flavour, _, texture, _, calories = l.split(" ")
		ingr[ingredient[:-1]] = (int(capacity[:-1]), int(durability[:-1]), int(flavour[:-1]), int(texture[:-1]), int(calories))
		igrs.append((int(capacity[:-1]), int(durability[:-1]), int(flavour[:-1]), int(texture[:-1]), int(calories)))
maxscore = 0
for i in range(100):
	for j in range(100):
		for k in range(100):
			for l in range(100):
				if i + j + k + l != 100:
					continue

				capacity = 0
				capacity += igrs[0][0] * i
				capacity += igrs[1][0] * j
				capacity += igrs[2][0] * k
				capacity += igrs[3][0] * l

				durability = 0
				durability += igrs[0][1] * i
				durability += igrs[1][1] * j
				durability += igrs[2][1] * k
				durability += igrs[3][1] * l

				flavor = 0
				flavor += igrs[0][2] * i
				flavor += igrs[1][2] * j
				flavor += igrs[2][2] * k
				flavor += igrs[3][2] * l

				texture = 0
				texture += igrs[0][3] * i
				texture += igrs[1][3] * j
				texture += igrs[2][3] * k
				texture += igrs[3][3] * l

				calorie = 0
				calorie += igrs[0][4] * i
				calorie += igrs[1][4] * j
				calorie += igrs[2][4] * k
				calorie += igrs[3][4] * l

				if calorie != 500:
					continue

				if capacity < 0:
					capacity = 0

				if durability < 0:
					durability = 0

				if flavor < 0:
					flavor = 0

				if texture < 0:
					texture = 0

				prod = capacity * durability * flavor * texture
				if prod > maxscore:
					maxscore = prod

print(ingr)
print(maxscore)