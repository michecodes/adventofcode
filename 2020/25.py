import re

file = open('./input/25.txt')
f_input = file.read()
card, door = re.split(r'\n', f_input)
card = int(card)
door = int(door)

def op(v, s):
	v = v * s
	v = v % 20201227
	return v

def get_loop(subject_number, target):
	v = subject_number
	i = 0
	sub = 1
	while True: 
		i += 1
		sub = op(v, sub)
		if sub == target:
			break
	return (i, sub)

card_loop, card_public_key = get_loop(7, card)
door_loop, door_public_key = get_loop(7, door)

sub = 1
for _ in range(door_loop):
	sub = op(card_public_key, sub)

print(sub)
