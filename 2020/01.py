file = open('./input/01.txt')
lines = file.read().split("\n")

def eval_part_1(input):
	for entry in input: 
		i = 0
		while i < len(input):
			if int(input[i]) + int(entry) == 2020:
				return int(input[i]) * int(entry)
			i += 1 

def eval_part_2(input):
	for entry in input: 
		i = 0
		while i < len(input):
			j = 0
			while j < len(input): 
				if int(input[i]) + int(input[j]) + int(entry) == 2020:
					return int(input[i]) * int(entry) * int(input[j])
				j+=1
			i += 1

print(eval_part_1(lines))
print(eval_part_2(lines))