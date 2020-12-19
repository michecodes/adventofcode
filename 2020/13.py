import math
import re
import sys
import functools
import collections
import operator
from collections import deque


file = open('./input/13.txt')
lines = re.split('\n', file.read())

eal = int(lines[0])
buses = [None if x == "x" else int(x) for x in lines[1].split(',')]

def s_for_n(n, m):
	if m % n != 0: 
		return ((m // n) + 1) * n
	return m

i = 0
mins = {}
for bus in buses:
	if bus:
		mins[i] = bus
	i += 1

for m, bus in mins.items(): 
	# I "cheated" by printing this out and inputting it to wolfram alpha to get the y intercept/answer
	# Right way would've been chinese remainder theorem
	print("t + " + str(m) + " mod " + str(bus) + " = 0,")

