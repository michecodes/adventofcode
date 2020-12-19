import math
import re
import sys
import functools
import collections
import operator
from collections import deque

file = open('./input/12.txt')
lines = re.split('\n', file.read())
dirs = ['N', "E", "S", "W"]
pos = (10, 1)
ship = (0, 0)
cur_dir = 1

def go_dir(pos, n, d):
	if d == "N":
		pos = (pos[0], pos[1] + n)
	if d == "S":
		pos = (pos[0], pos[1] - n)
	if d == "E":
		pos = (pos[0] + n, pos[1])
	if d == "W":
		pos = (pos[0] - n, pos[1])
	return pos

def translate_clock(pos, times):
	for _ in range(times):
		pos = (pos[1], -1 * pos[0])
	return pos

def translate_ctr(pos, times):
	for _ in range(times):
		pos = (pos[1] * -1, pos[0])
	return pos

for line in lines: 
	d, n = line[0], int(line[1:])
	if d in dirs: 
		pos = go_dir(pos, n, d)
	if d == "L":
		pos = translate_ctr(pos, n // 90)
	if d == "R":
		pos = translate_clock(pos, n // 90)
	if d == "F":
		ship = (ship[0] + pos[0] * n, ship[1] + pos[1] * n)


print(abs(ship[0]) + abs(ship[1]))




