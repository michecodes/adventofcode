import math
import re
import sys
import functools
import collections
import operator
from collections import deque


file = open('./input/14.txt')
lines = re.split('\n', file.read())

one_mask = None
zero_mask = None
 
ps = {}
for line in lines: 
	if 'mask' in line:
		mask = line.split(" = ")[1]
		one_mask = int(''.join(['1' if x == '1' else '0' for x in mask]), 2)
		zero_mask = int(''.join(['1' if x == '0' else '0' for x in mask]), 2)
		x_mask = ['1' if x == 'X' else '0' for x in mask]
	else: 
		m = re.match(r'mem\[([\d]*)\] = ([\d]*)', line)
		pos, n = (int(m[1]),  int(m[2]))
		pos = pos | one_mask
		opts = ['']
		i = 0
		for x in x_mask:
			maskr = 2 ** (len(x_mask) - i - 1)
			new_opts = []
			for opt in opts.copy():
				if x == "1":
					new_opts.append(opt + "1")
					new_opts.append(opt + "0")
				else: 
					new_opts.append(opt + ('1' if pos & maskr != 0 else '0'))
			opts = new_opts
			i += 1 
		
		for ops in opts:
			npos = int(ops, 2)
			ps[npos] = n


s = 0
for pos, n in ps.items():
	s += n

print(s)