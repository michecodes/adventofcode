import math
import re
import sys
import functools
import collections
import operator
from collections import deque

file = open('./input/20.txt')
f_input = file.read()

tile_dict = {}
tiles = re.split(r'\n\n', f_input)

for tile in tiles:
	tile = tile.split("\n")
	tile_id = re.match(r'Tile (\d*):', tile[0])[1]
	imgs = tile[1:]
	tile_dict[tile_id] = imgs

def get_sides(tile):
	top = tile[0]
	bottom = tile[-1]
	left = ''.join([c[0] for c in tile])	
	right = ''.join([c[-1] for c in tile])
	return (left, top, right, bottom)

def flip_h(tile):
	return [l[::-1] for l in tile]

def rotate_90(tile):
	new_grid = []
	for i in range(len(tile)):
		new_grid.append(''.join(x[-1-i] for x in tile))
	return new_grid


side_map = collections.defaultdict(list)
for tile_id, grid in tile_dict.items():
	sides = get_sides(grid)
	for side in sides: 
		side_map[side].append(tile_id)

mult = 1
corner_tiles = []
for tile_id, grid in tile_dict.items():
	sides = get_sides(grid)
	no_matches = 0
	for side in sides: 
		matches = len(side_map[side])
		matches += len(side_map[side[::-1]])
		if matches == 1:
			no_matches += 1
	if no_matches == 2:
		mult *= int(tile_id)
		corner_tiles.append(tile_id)

print("Part 1", mult)

def get_matches_for_side(side):
	matches = len(side_map[side])
	matches += len(side_map[side[::-1]])
	return matches

final_image = [[]]
tiles_used = {}
# put a single corner tile in a corner
corner_tile_id = corner_tiles[0]
grid = tile_dict[corner_tile_id]
# rotate the tile until its unmatched sides are upper left 
for _ in range(4):
	sides = get_sides(grid)
	if get_matches_for_side(sides[0]) == 1 and get_matches_for_side(sides[1]) == 1:
		final_image[0].append(grid)
		tiles_used[corner_tile_id] = (0, 0)
		break
	grid = flip_h(grid)
	if get_matches_for_side(sides[0]) == 1 and get_matches_for_side(sides[1]) == 1:
		final_image[0].append(grid)
		tiles_used[corner_tile_id] = (0, 0)
		break
	grid = rotate_90(grid)
	grid = flip_h(grid)

def print_i(image):
	for row in image:
		print("NEW_ROW")
		for item in row:
			print('\n'.join(item) + "\n")

row = 0
while len(tile_dict) > len(tiles_used):
	if row >= len(final_image):
		# We're on a new row, match the grid to the top
		grid = final_image[row - 1][0]
		sides = get_sides(grid)
		bottom_side = sides[3]
		next_tile_id = [i for i in (side_map[bottom_side] + side_map[bottom_side[::-1]]) if i not in tiles_used][0]
		next_tile_grid = tile_dict[next_tile_id]
		for _ in range(4):
			if get_sides(next_tile_grid)[1] == bottom_side:
				break
			next_tile_grid = flip_h(next_tile_grid)
			if get_sides(next_tile_grid)[1] == bottom_side:
				break
			next_tile_grid = rotate_90(next_tile_grid)
			next_tile_grid = flip_h(next_tile_grid)
		final_image.append([next_tile_grid])
		tiles_used[next_tile_id] = (row, len(final_image[row]) - 1)
	else:
		# We're appending to an existing row, match the right side
		grid = final_image[row][-1]
		sides = get_sides(grid)
		right_side = sides[2]
		if get_matches_for_side(right_side) == 1:
			# No matches for right side means it's the end of a row
			row += 1
			continue
		else: 
			next_tile_id = [i for i in (side_map[right_side] + side_map[right_side[::-1]]) if i not in tiles_used][0]
			next_tile_grid = tile_dict[next_tile_id]
			for _ in range(4):
				if get_sides(next_tile_grid)[0] == right_side:
					break
				next_tile_grid = flip_h(next_tile_grid)
				if get_sides(next_tile_grid)[0] == right_side:
					break
				next_tile_grid = rotate_90(next_tile_grid)
				next_tile_grid = flip_h(next_tile_grid)
			final_image[row].append(next_tile_grid)
			tiles_used[next_tile_id] = (row, len(final_image[row]) - 1)


def build_image(image):
	final_image = []
	current_i = 0
	for row_n, row in enumerate(image):
		[final_image.append('') for _ in range(8)]
		for grid in row: 
			for r, line in enumerate(grid):
				if r != 0 and r != len(grid) - 1:
					final_image[current_i + r - 1] += line[1:-1]
		current_i += 8
	return final_image

final_image = build_image(final_image)

monster = '                  # \n#    ##    ##    ###\n #  #  #  #  #  #   '
split_monster = monster.split('\n')
monster_octothorpes = monster.count('#')

def search_for_monster(image):
	monsters_found = 0
	for y in range(len(image)):
		for x in range(len(image[0])):
			valid_monster_starts_here = True

			for i in range(len(split_monster)):
				for j in range(len(split_monster[0])):
					if split_monster[i][j] == '#':
						check_y = y + i
						check_x = x + j
						if check_y < len(image) and check_x < len(image[0]):
							if image[check_y][check_x] != "#":
								valid_monster_starts_here = False
						else:
							valid_monster_starts_here = False
			
			if valid_monster_starts_here:
				monsters_found += 1
	return monsters_found

def get_orientation_and_count(image):
	for _ in range(4):
		monsters_found = search_for_monster(image)
		if monsters_found:
			return image, monsters_found
		image = flip_h(image)
		monsters_found = search_for_monster(image)
		if monsters_found:
			return image, monsters_found
		image = rotate_90(image)
		image = flip_h(image)
	return None, None

image, monsters_found = get_orientation_and_count(final_image)
print("Part 2:", '\n'.join(image).count('#') - monster_octothorpes * monsters_found)

