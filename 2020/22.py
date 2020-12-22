import math
import re
import sys
import functools
import collections
import operator
from collections import deque

file = open('./input/22.txt')
f_input = file.read()

p1, p2 = re.split(r'\n\n', f_input)

p1 = [int(x) for x in p1.split('\n')[1:]]
p2 = [int(x) for x in p2.split('\n')[1:]]

def play_game(p1, p2):
	configurations = set()

	while len(p1) > 0 and len(p2) > 0:
		if (str(p1), str(p2)) in configurations:
			return (p1, [])
		configurations.add((str(p1), str(p2)))

		c1 = p1.pop(0)
		c2 = p2.pop(0)

		if len(p1) >= c1 and len(p2) >= c2:
			p11, p22 = play_game(p1.copy()[:c1], p2.copy()[:c2])
			if len(p11) > len(p22):
				p1.extend([c1, c2])
			else:
				p2.extend([c2, c1])
		elif c1 > c2:
			p1.extend([c1, c2])
		elif c2 > c1:
			p2.extend([c2, c1])
	return p1, p2

p1, p2 = play_game(p1, p2)
list_with_items = p1 if len(p1) > 0 else p2
s = 0
i = 0
while i < len(list_with_items):
	s += list_with_items[i] * (len(list_with_items) - i)
	i += 1

print(s)