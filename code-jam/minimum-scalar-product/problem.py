__author__ = 'julenka'

# url to the problem goes here
import numpy as np

def solve_case_multi(lines):
    A = list(reversed(sorted([int(x) for x in lines[0].split(' ')])))
    B = list(sorted([int(x) for x in lines[1].split(' ')]))
    result = 0
    for i in range(len(A)):
        result += A[i] * B[i]
    return result


# config
# letter = 'C'
# letter = 'B'
letter = 'A'
# size = 'small'
size = 'large'
# size = 'tiny'
input = '%s-%s-practice.in' % (letter,size)
output = input.replace('.in', '.out')
lines = (line.strip() for line in open(input).readlines())
outf = open(output, 'w')
num_cases = int(lines.next())


for i in range(num_cases):
    num_lines = 2
    lines.next()
    case_lines = []
    for j in range(num_lines):
        case_lines.append(lines.next())
    print "Case #%d: %s" % (i + 1, solve_case_multi(case_lines))
    print >> outf, "Case #%d: %s" % (i + 1, solve_case_multi(case_lines))



