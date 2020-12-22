import math
import re
import sys
import functools
import collections
import operator
from collections import deque

file = open('./input/21.txt')
f_input = file.read()

lines = re.split(r'\n', f_input)

allerg_sets = {}
all_ingredients = set()
i_ct = collections.defaultdict(int)

for line in lines: 
	m = re.match(r'(.*) \(contains (.*)\)', line)
	ingredients = m[1].split(' ')
	all_ingredients.update(ingredients)
	for i in ingredients:
		i_ct[i] += 1
	allerg = m[2].split(', ')
	for a in allerg:
		allerg_sets[a] = set(ingredients) if a not in allerg_sets else allerg_sets[a].intersection(set(ingredients))
	
might_be_bad = set()
for a, i in allerg_sets.items():
	might_be_bad.update(i)
ct = 0

any_updated = True
while any_updated:
	any_updated = False
	for a, i in allerg_sets.copy().items():
		if len(i) == 1:
			ing = next(iter(i))
			for b, j in allerg_sets.copy().items():
				if ing in j and b != a:
					any_updated = True
					j.remove(ing)

allergens = [k for k in allerg_sets.keys()]
allergens.sort()
ings = []
for a in allergens:
	i = allerg_sets[a]
	ing = next(iter(i))
	ings.append(ing)
print(','.join(ings))
