__author__ = 'julenka'

# url to the problem goes here
# https://code.google.com/codejam/contest/619102/dashboard#s=p0

def solve_case_multi(lines):
    ropes = []
    for l in lines:
        ls = l.strip().split(' ')
        ropes.append([int(ls[0]), int(ls[1])])

    c = 0
    for i in range(len(ropes)):
        for j in range(i+1,len(ropes)):
            r1 = ropes[i]
            r2 = ropes[j]
            if(r1[0] < r2[0] and r1[1] > r2[1]):
                c += 1
            elif(r1[0] > r2[0] and r1[1] < r2[1]):
                c += 1

    return c


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


# model 1:
# lines
# n_lines_for_case
# line1
# line2
# ...
for i in range(num_cases):
    num_lines = int(lines.next())
    case_lines = []
    for j in range(num_lines):
        case_lines.append(lines.next())
    print "Case #%d: %s" % (i + 1, solve_case_multi(case_lines))
    print >> outf, "Case #%d: %s" % (i + 1, solve_case_multi(case_lines))
