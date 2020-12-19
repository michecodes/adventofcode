import re

file = open('./input/19.txt')
f_input = file.read()

rules, msgs = re.split(r'\n\n', f_input)
rules = {a[0]: a[1] for a in [r.split(":") for r in rules.split("\n")]}

def get_regex(rule):
    if '"' in rules[rule]:
        return rules[rule].split('"')[1]
        
    if rule == '8':
    	re_42 = get_regex('42')
    	return re_42 + "+"
    if rule == '11':
    	re_42 = get_regex('42')
    	re_31 = get_regex('31')
    	return '(' + '|'.join(re_42 + '{' + str(n) + '}' + 
    		re_31 + '{'+ str(n) +'}' for n in range(1, 40)) + ')'

    opts = rules[rule].strip().split(" | ")
    regex = []
    for opt in opts:
        regex.append(''.join([get_regex(el) for el in opt.strip().split(' ')]))
    return '(' + '|'.join(regex) + ')'

regex = get_regex('0')
print(sum([1 for m in msgs.split('\n') if re.fullmatch(regex, m)]))