import math
import re
import sys
import functools
import collections
import operator
from collections import deque

file = open('./input/11.txt')
lines = re.split('\n', file.read())

w = len(lines[0])
h = len(lines)

#used for part 1
def get_adjs(x, y, arr):
	adjs = 0
	for i in range (-1, 2):
		for j in range(-1, 2):
			if i + y >= 0 and i + y < w and j + x >= 0 and j + x < h:
				if not (i == 0 and j == 0):
					if arr[x + j][y + i] == '#':
						adjs += 1
	return adjs

def get_visible(x, y, arr):
	adjs = 0
	for i in range (-1, 2):
		for j in range(-1, 2):
			if i + y >= 0 and i + y < w and j + x >= 0 and j + x < h:
				if not (i == 0 and j == 0):
					ii = i
					jj = j
					iii = i
					jjj = j
					found_any_in_dir = False
					while iii + y >= 0 and iii + y < w and jjj + x >= 0 and jjj + x < h:
						if arr[x + jjj][y + iii] == '#':
							found_any_in_dir = True
							break
						if arr[x + jjj][y + iii] == 'L':
							found_any_in_dir = False
							break

						iii += i
						jjj += j
					if found_any_in_dir:
						adjs += 1
	return adjs

def fill(lines):
	next_round = [[['.'] for _ in range(w)] for _ in range(h)]
	for i in range(h):
		for j in range(w):
			if lines[i][j] == ".":
				next_round[i][j] = "."
				continue
			elif lines[i][j] == "L":				
				adjs = get_visible(i, j, lines)
				if adjs == 0:
					next_round[i][j] = "#"
				else: 
					next_round[i][j] = "L"
			elif lines[i][j] == "#":
				adjs = get_visible(i, j, lines)
				if adjs >= 5:
					next_round[i][j] = "L"
				else:
					next_round[i][j] = "#"
	return next_round

def pb(arr):
	for line in arr:
		print(''.join(line))
	print("\n")

cur_lines = lines
while True: 
	next_time = fill(cur_lines)
	if next_time == cur_lines:
		break
	cur_lines = next_time

occ = 0
for i in range(h):
	for j in range(w):	
		if cur_lines[i][j] == "#":
			occ += 1	

print(occ) 