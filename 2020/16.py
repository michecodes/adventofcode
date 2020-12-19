import math
import re
import sys
import functools
import collections
import operator
from collections import deque

file = open('./input/16.txt')
sects = re.split('\n\n', file.read())

all_names = set()
valid_ranges = []
valid_ranges_map = {}
i = 0
for line in re.split('\n', sects[0]):
	m = re.match(r'(.*): (\d*)-(\d*) or (\d*)-(\d*)', line)
	name = m[1]
	min1 = m[2]
	max1 = m[3]
	min2 = m[4]
	max2 = m[5]

	valid_ranges.append((min1, max1))
	valid_ranges.append((min2, max2))
	all_names.add(name)
	valid_ranges_map[i] = {
		'name': name,
		'ranges': [(min1, max1), (min2, max2)]
	}
	i += 1
	valid_ranges_map[i] = {
		'name': name,
		'ranges': [(min1, max1), (min2, max2)]
	}
	i += 1

valid_tickets = []
s = 0
for line in re.split('\n', sects[2])[1:]:
	ns = line.split(',')
	any_invalid = False
	for n in ns:
		any_valid = False
		for x, y in valid_ranges:
			if int(x) <= int(n) and int(n) <= int(y):
				any_valid = True
		if not any_valid:
			s += int(n)
			any_invalid = True
	if not any_invalid:
		valid_tickets.append(ns)

field_meets_rules = collections.defaultdict(set)
field_not_meets_rules = collections.defaultdict(set)

for ticket in valid_tickets:
	for i in range(len(ticket)):
		for j in range(0, len(valid_ranges), 2):
			x, y = valid_ranges[j]
			z, w = valid_ranges[j + 1]
			n = ticket[i]
			if (int(x) <= int(n) and int(n) <= int(y)) or (int(z) <= int(n) and int(n) <= int(w)):
				name = valid_ranges_map[j].get('name')
				field_meets_rules[i].add(name)
			else:
				name = valid_ranges_map[j].get('name')
				field_not_meets_rules[i].add(name)

possible_mappings = collections.defaultdict(set)

opts = {}
for f in range(len(valid_tickets[0])):
	rules = field_not_meets_rules[f]
	meets = all_names - rules
	opts[f] = meets

unsolved = True
solved = {}
while unsolved:
	any_unsolved = False
	for f in range(len(valid_tickets[0])):
		if len(opts[f]) == 1:
			solved[f] = opts[f]
			for k, i in opts.items():
				if k != f:
					opts[k] = i - opts[f]
		else:
			any_unsolved = True
	if not any_unsolved:
		unsolved = False

# field #s in my input starting with departure 
depts = [2, 3, 7, 10, 11, 13]

for line in re.split('\n', sects[1])[1:]:
	ls = line.split(',')
	s = 1
	for i in depts:
		s = s * int(ls[i])
print(s)


