import re

file = open('./input/07.txt')
lines = re.split('\n', file.read())

d = {}
rule_map = {}

for line in lines:
	items = list(map(lambda s: s.replace('.', ''), map(lambda s: s.replace(',', ''), map(lambda s: s.replace('contain', ''), map(lambda s: s.strip(),  re.split('bags|bag', line))))))
	color = items[0]
	contains = [x for x in items[1:]]
	for item in contains: 
		if not "no other" in item and any(char.isdigit() for char in item):
			number = int(item[:2])
			bag = item[item.find(str(number)) + 2:]
			if color.strip() in rule_map: 
				d = rule_map[color.strip()]
				d[bag] = number
			else: 
				rule_map[color.strip()] = {bag: number}
		if "no other" in item: 
			rule_map[color] = {}


def get_contains(color):
	if len(rule_map[color]) == 0:
		return 0
	else:
		return sum([n * (get_contains(c) + 1) for c, n in rule_map[color].items()])

print(get_contains('shiny gold'))

