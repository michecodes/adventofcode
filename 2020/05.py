import math
import re

file = open('input/05.txt')
lines = file.read().split('\n')

seats = []
for line in lines: 
	line = line.replace('L', '0')
	line = line.replace('R', '1')
	line = line.replace('F', '0')
	line = line.replace('B', '1')
	num = int(line, 2)
	seats.append(num) 
# part 1
print(max(seats))

#part 2
for i in range(2 ** len(lines[0])):
    if i not in seats and i+1 in seats and i-1 in seats:
        print(i)