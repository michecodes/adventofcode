import collections

file = open('./input/24.txt')
f_input = file.read()

offsets = {
	'e': (2,0),
	'w': (-2, 0),
	'ne': (1, -1), 
	'nw': (-1, -1),
	'se': (1, 1),
	'sw': (-1, 1)
}

lines = f_input.split('\n')
tiles = collections.defaultdict(bool)

for dirs in lines:
	x, y = 0, 0
	while len(dirs) > 0:
		if dirs.startswith('n') or dirs.startswith('s'):
			dx, dy = offsets[dirs[:2]]
			dirs = dirs[2:]
		else:
			dx, dy = offsets[dirs[:1]]
			dirs = dirs[1:]
		x, y = x + dx, y + dy
	tiles[(x,y)] = not tiles[(x,y)]


def get_adj(x, y, tiles):
	adj = 0
	for dx, dy in offsets.values():
		if (x + dx, y + dy) in tiles:
			if tiles[(x+dx, y+dy)]:
				adj += 1
	return adj


def flip(tiles):
	min_x = min([k[0] for k, is_black in tiles.items() if is_black])
	min_y = min([k[1] for k, is_black in tiles.items() if is_black])
	max_x = max([k[0] for k, is_black in tiles.items() if is_black])
	max_y = max([k[1] for k, is_black in tiles.items() if is_black])

	tiles_copy = collections.defaultdict(bool)
	for x in range(min_x - 1, max_x + 2):
		for y in range(min_y - 2, max_y + 2):
			is_black = tiles[(x, y)]
			adj = get_adj(x, y, tiles)
			if is_black and (adj == 0 or adj > 2):
				tiles_copy[(x, y)] = False
			elif is_black:
				tiles_copy[(x, y)] = True
			elif not is_black and adj == 2:
				tiles_copy[(x, y)] = True
			else:
				tiles_copy[(x, y)] = False
	return tiles_copy


for i in range(100):
	tiles = flip(tiles)
	print(i + 1, sum(tiles.values()))



