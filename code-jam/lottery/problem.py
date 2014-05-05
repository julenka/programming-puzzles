__author__ = 'julenka'

# url to the problem goes here
# https://code.google.com/codejam/contest/2994486/dashboard#s=p1
import numpy as np

def solve_case_single(line):
    a,b,k = [int(x) for x in line.split(' ')]
    count = (min(a,k) + 1) * (min(b,k) + 1)
    for i in xrange(k, a):
        for j in xrange(k, b):
            if i & j < k:
                count += 1
    return count

# config
# letter = 'C'
letter = 'B'
# letter = 'A'
size = 'small'
# size = 'large'
input = '%s-%s-practice.in' % (letter,size)
output = input.replace('.in', '.out')
lines = (line.strip() for line in open(input).readlines())
outf = open(output, 'w')
num_cases = int(lines.next())

# model 2:
# lines
# case1
# case2
# ...
for i in range(num_cases):
    line = lines.next()
    print "Case #%d: %s" % (i + 1, solve_case_single(line))
    print >> outf, "Case #%d: %s" % (i + 1, solve_case_single(line))


