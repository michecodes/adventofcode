import math
import re
import string

file = open('./input/06.txt') 
groups = re.split('\n\n', file.read())

# I have since learned that string.ascii_uppercase is a thing...
letters = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'
letters = re.split(',| ', letters)

alls = 0
for group in groups: 
	lines = group.split('\n')
	all_yes = [x for x in lines[0]]
	for line in lines: 
		for letter in all_yes.copy():
			if letter not in line: 
				all_yes.remove(letter)

	for letter in all_yes:
		amt = group.count(letter)
	alls += len(all_yes)

print(alls)