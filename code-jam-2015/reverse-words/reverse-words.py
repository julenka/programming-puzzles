__author__ = 'julenka'
# https://code.google.com/codejam/contest/351101/dashboard#s=p1
input = 'B-large-practice.in'
output = input.replace('.in', '.out')
lines = open(input).readlines()[1:]
outf = open(output, 'w')
for i,line in enumerate(lines):
    line = line.strip()
    print >> outf, "Case #%d: %s" % (i + 1, ' '.join(reversed(line.split(' '))))

