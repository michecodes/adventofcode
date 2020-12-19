file = open('./input/03.txt')
lines = file.read().split('\n')

rightdown_pairs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

mult = 1

for pair in rightdown_pairs:
	j, i = 0, 0
	trees = 0
	while i < len(lines):
		encountered = lines[i][j % len(lines[0])]
		if encountered == "#":
			trees += 1
		i += pair[1]
		j += pair[0]

	mult = mult * trees

print(mult)