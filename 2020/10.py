import math
import re
import sys
import functools
import collections
import operator


file = open('./input/10.txt')
lines = re.split('\n', file.read())

adapters = [int(x) for x in lines]
adapters.sort()

def attempt_using_next(cur, adapters, aiming=None):
	if len(adapters) == 1:
		if adapters[0] <= cur + 3 and adapters[0] >= cur:
			if aiming and adapters[0] != aiming:
				return None
			return [adapters[0]]
		else:
			return None
	options = [x for x in adapters if x <= cur + 3 and x >= cur]
	for opt in options: 
		options_without = adapters.copy()
		options_without.remove(opt)
		att = attempt_using_next(opt, options_without)
		if att:
			return [opt] + att
	return None

result = attempt_using_next(0, adapters)
aiming = result[-1]

ones, thres, prev = 0, 0, 0
for i in range(len(result)):
	if result[i] - prev == 1:
		ones += 1
	if result[i] - prev == 3:
		thres += 1
	prev = result[i]

print("Part 1: ", ones * (thres + 1))

ways = {}
def get_ways(adapters, cur, aiming):
	i = (len(adapters), cur)
	if i in ways:
		return ways[i]
	ct = 0
	if aiming - cur <= 3:
		ct += 1
	if not adapters:
		return ct
	if adapters[0] - cur <= 3:
		ct += get_ways(adapters[1:], adapters[0], aiming)
	ct += get_ways(adapters[1:], cur, aiming)
	ways[i] = ct
	return ct
print(get_ways(adapters, 0, adapters[-1] + 3))


