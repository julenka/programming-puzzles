__author__ = 'julenka'

import re

input = 'A-large-practice.in'
output = input.replace('.in', '.out')
lines = open(input).readlines()[0:]
outf = open(output, 'w')
num_cases = int(lines[0])

def solve_case(lines):
    credit = int(lines[0])
    values = [int(x) for x in re.split('\s+', lines[2].strip())]
    v_map = { v:i for i,v in enumerate(values)}
    for i,v in enumerate(values):
        if credit - v in values[i+1:]:
            return (i + 1, v_map[(credit - v)] + 1)
    return (-1, -1)

for i in range(num_cases):
    a,b = solve_case(lines[i * 3 + 1: (i+1) * 3 + 1])
    print >> outf, "Case #%d: %d %d" % (i + 1, a, b)
