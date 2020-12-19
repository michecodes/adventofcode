file = open('./input/02.txt')
lines = file.read().split("\n")

goodones = 0
for line in lines:
	splitup = line.split(" ")
	minmax = splitup[0].split('-')
	lower = int(minmax[0])
	upper = int(minmax[1])
	letter = splitup[1][0]

	test_string = splitup[2]

	# part 1
	# ct = test_string.count(letter)
	# if ct >= lower and ct <= upper:
	# 	goodones += 1

	if test_string[lower - 1] == letter or test_string[upper - 1] == letter:
		if not (test_string[lower - 1] == letter and test_string[upper - 1] == letter):
			goodones += 1

print(goodones)