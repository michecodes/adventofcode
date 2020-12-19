import re

file = open('inputs/19.txt')
f_input = file.read()

rules, msgs = re.split(r'\n\n', f_input)
rules = {a[0]: a[1] for a in [r.split(":") for r in rules.split("\n")]}

def get_regex(rule):
    if '"' in rules[rule]:
        return rules[rule].split('"')[1]

    opts = rules[rule].strip().split(" | ")
    regex = []
    for opt in opts:
        regex.append(''.join([get_regex(el) for el in opt.strip().split(' ')]))
    return '(' + '|'.join(regex) + ')'

regex = get_regex('0')
print(sum([1 for m in msgs.split('\n') if re.fullmatch(regex, m)]))