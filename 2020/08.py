import math
import re
import functools
import collections
import operator


file = open('./input/08.txt')
lines = re.split('\n', file.read())

insts = []

for line in lines: 
	command, amt = line[:3], int(line[3:])
	insts.append((command, amt))

for j in range(len(insts)):
	copied = insts.copy()
	if copied[j][0] == "nop":
		copied[j] = ("jmp", copied[j][1])
	if copied[j][0] == "jmp":
		copied[j] = ("nop", copied[j][1])

	run_already = set()
	time_to_stop = False
	i = 0
	acc = 0

	while not time_to_stop:
		if i >= len(copied):
			print(acc)
			break
		elif i in run_already:
			time_to_stop = True
		run_already.add(i)
		if copied[i][0] == 'acc':
			acc += copied[i][1]
			i += 1
		elif copied[i][0] == 'jmp':
			i += insts[i][1]
		elif copied[i][0] == 'nop':
			i += 1


