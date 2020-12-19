import math
import re
import sys
import functools
import collections
import operator

preamble_len = 25
file = open('./input/09.txt')
lines = re.split('\n', file.read())

i = 0
past_25 = []
for line in lines:
	past_25.append(int(line))
	if i > preamble_len: 
		valid_line = False
		past_25.pop(0)
		for x in range(len(past_25)):
			for y in range(len(past_25)):
				if x != y and int(past_25[x]) + int(past_25[y]) == int(line):
					valid_line = True
		if not valid_line:
			print("Part 1: ", line)
			looking_for = int(line)

	i += 1

for i in range(len(lines)): 
	sum_from_i = 0
	pos = i
	while sum_from_i < looking_for and pos < len(lines):
		sum_from_i += int(lines[pos])
		pos += 1
	if sum_from_i == looking_for:
		l = min(lines[i:pos])
		m = max(lines[i:pos])
		print(int(l) + int(m))
		break

