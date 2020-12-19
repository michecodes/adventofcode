import re 

file = open('./input/04.txt')
lines = file.read().split('\n\n')

fields = {
	'byr': {
		'digits': 4,
		'min': 1920,
		'max': 2002
	}, 
	'iyr': {
		'digits': 4,
		'min': 2010,
		'max': 2020
	}, 
	'eyr' : {
		'digits': 4,
		'min': 2020,
		'max': 2030
	}, 
	'hgt' : {
		'followed_by': ['cm', 'in'],
	}, 
	'hcl' : {
		'preceded_by': '#'
	}, 
	'ecl' : {
		'one_of': ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	}, 
	'pid' : {
		'digits': 9 
	}
}

result = 0
results = []
rd = {}

for line in lines: 
	all_good = True
	for field, rules in fields.items():
		items = re.split(' |\n', line)


		if not field + ":" in line: 
			all_good = False

		# part 2
		relevant = [x for x in items if x.startswith(field)]
		if len(relevant) > 0:
			relevant = relevant[0]
			value = relevant.split(':')[1]
			if 'digits' in rules: 
				if not len(value) == rules['digits']:
					all_good = False

			if 'min' in rules: 
				if not int(value) >= rules['min']:
					all_good = False

			if 'max' in rules: 
				if not int(value) <= rules['max']:
					all_good = False

			if field == 'hgt':
				if value.endswith('cm'):
					if int(value.split('cm')[0]) < 150 or int(value.split('cm')[0]) > 193:
						all_good = False
				elif value.endswith('in'):
					if int(value.split('in')[0]) < 59 or int(value.split('in')[0]) > 76: 
						all_good = False
				else: 
					all_good = False

			if 'one_of' in rules: 
				if value not in rules['one_of']:
					all_good = False

			if 'preceded_by' in rules:
				if not value.startswith('#'):
					all_good = False
			
	if all_good:
		result += 1

print(result)
