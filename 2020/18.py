import math
import re
import sys
import functools
import collections
import operator
from collections import deque

file = open('./input/18.txt')
lines = re.split('\n', file.read())


def eval_till_end(expr, input_pos):
	pos = input_pos
	ev = None
	last_val = 0
	last_op = None
	while pos < len(expr):
		nxt = expr[pos]
		if nxt == "(":
			amt, end = eval_till_end(expr, pos + 1)
			if last_op is None:
				ev = amt
			if last_op == "+":
				ev += amt
			elif last_op == "*":
				ev = ev * amt
			pos = end
		elif nxt == " ":
			pos += 1
			continue
		elif nxt == "+":
			last_op = "+"
		elif nxt == "*":
			last_op = "*"
		elif nxt == ")":
			return (ev, pos)
		else: 
			nxt == int(expr[pos])
			if last_op is None:
				ev = int(nxt)
			if last_op == "+":
				ev += int(nxt)
			elif last_op == "*":
				ev = ev * int(nxt)
		pos += 1
	
	return (ev, pos)

def is_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def add_parens_for_plus(plus_pos, expr):
	right = plus_pos
	left = plus_pos
	while right < len(expr) - 1:
		if expr[right].isdigit():
			expr = expr[:right + 1] + ")" + expr[right + 1:]
			break
		if expr[right] == " ":
			right += 1
			continue
		if expr[right] == "(":
			num_open = 1
			num_closed = 0
			while num_closed != num_open and right < len(expr):
				right += 1
				if expr[right] == "(":
					num_open += 1
				elif expr[right] == ")":
					num_closed += 1
			expr = expr[:right + 1] + ")" + expr[right + 1:]
			break
		right += 1
	while left >= 0:
		if expr[left].isdigit():
			expr = expr[:left] + "(" + expr[left:]
			break
		if expr[left] == " ":
			left -= 1
			continue
		if expr[left] == ")":
			num_open = 1
			num_closed = 0
			while num_closed != num_open and left > 0:
				left -= 1
				if expr[left] == ")":
					num_open += 1
				elif expr[left] == "(":
					num_closed += 1
			expr = expr[:left] + "(" + expr[left:]
			break
		left -= 1
	return expr


total = 0
total_p1 = 0
for line in lines:
	res, p = eval_till_end(line, 0)
	total_p1 += res
	i = 0
	while i < len(line):
		if line[i] == "+":
			line = add_parens_for_plus(i, line)
			i += 2
		else:
			i += 1
	res, p = eval_till_end(line, 0)
	total += res
print("Part 1: ", total_p1)
print(total)
