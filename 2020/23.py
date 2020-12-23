import math
import re
import sys
import functools
import collections
import operator
import itertools
from collections import deque

class LinkedNode: 
	def __init__(self, label, right=None, left=None,):
		self.label = label
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.label)


file = open('./input/23.txt')
f_input = file.read()
lines = re.split(r'\n', f_input)

labels = [int(c) for c in lines[0]]
max_label = max(all_labels)
labels += [k for k in range(max_label + 1, 1000001)]
max_label = 1000000


node_map = {}
head_node = None
prev_node = None

# build the linked list of cups
for label in labels:
	if head_node is None:
		head_node = LinkedNode(label)
		prev_node = head_node
		node_map[label] = head_node
	else: 
		next_node = LinkedNode(label, left=prev_node)
		prev_node.right = next_node
		node_map[label] = next_node
		prev_node = next_node
head_node.left = prev_node
prev_node.right = head_node


cur = head_node
i = 0
while i < 10000001:
	cur_label = cur.label
	next_3 = [cur.right, cur.right.right, cur.right.right.right]

	# Remove the next 3 from the loop
	cur.right = next_3[2].right
	cur.right.left = cur

	dest = cur_label - 1 if cur_label - 1 != 0 else max_label
	while dest in [v.label for v in next_3]:
		dest = dest - 1 if dest - 1 != 0 else max_label

	# Re-add the next 3 to the loop
	dest_node = node_map[dest]
	next_3[2].right = dest_node.right
	next_3[2].right.left = next_3[2]
	dest_node.right = next_3[0]
	next_3[0].left = dest_node

	cur = cur.right
	i += 1


# get to 1 node
node_one = node_map.get(1)
print(node_one.right.label * node_one.right.right.label)
