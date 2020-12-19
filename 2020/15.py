import math
import re
import sys
import functools
import collections
import operator
from collections import deque


file = open('./input/15.txt')
numbers = re.split(',', file.read())

spoken = collections.defaultdict(list)
last_spoke = None

for i in range(30000000):
	if i < len(numbers):
		last_spoke = int(numbers[i])
		spoken[last_spoke].append(i)
	else:
		if len(spoken[last_spoke]) == 1:
			last_spoke = 0
			spoken[0].append(i)
			spoken[0] = spoken[0][-2:]
		else:
			n = i - (spoken[last_spoke][0] + 1)
			last_spoke = n
			spoken[n].append(i)
			spoken[n] = spoken[n][-2:]

print(last_spoke)
