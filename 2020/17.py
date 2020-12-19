import math
import re
import sys
import functools
import collections
import operator
from collections import deque



file = open('./input/17.txt')
lines = re.split('\n', file.read())

cubes = {}
x,y = 0,0
for line in lines:
	x = 0
	for c in line: 
		cubes[(x, y, 0, 0)] = c == "#"
		x += 1
	y += 1

def active_at(x, y, z, w):
	if (x, y, z, w) in cubes:
		return cubes[(x, y, z, w)]
	return False

def get_range_for_dir(dir):
	dirs = ['x', 'y', 'z', 'w']
	pos = dirs.index(dir)
	return (min(c[pos] for c in cubes.keys()) - 1, max(c[pos] for c in cubes.keys()) + 2)

def cycle(cubes):
	new_cubes = {}
	for x in range(*get_range_for_dir('x')):
		for y in range(*get_range_for_dir('y')):
			for z in range(*get_range_for_dir('z')):
				for w in range(*get_range_for_dir('w')):
					active = active_at(x, y, z, w)
					
					neighbors = 0
					for dx in range(-1, 2):
						for dy in range(-1, 2):
							for dz in range(-1, 2):
								for dw in range(-1, 2):
									if not dx == dz == dy == dw == 0:
										if active_at(x + dx, y + dy, z + dz, w + dw):
											neighbors += 1

					if active and neighbors in [2, 3]:
						new_cubes[(x, y, z, w)] = True
					elif not active and neighbors == 3:
						new_cubes[(x, y, z, w)] = True
					else:
						new_cubes[(x, y, z, w)] = False
	return new_cubes

for i in range(6):
	cubes = cycle(cubes)
	print(sum([1 for c in cubes.values() if c]))
