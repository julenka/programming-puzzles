__author__ = 'julenka'

# url to the problem goes here

def solve_case_multi(lines):
    return None

def solve_case_single(line):
    return None

# config
# letter = 'C'
# letter = 'B'
letter = 'A'
# size = 'small'
size = 'large'
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

# model 2:
# lines
# case1
# case2
# ...
for i in range(num_cases):
    line = lines.next()
    print "Case #%d: %s" % (i + 1, solve_case_single(line))
    print >> outf, "Case #%d: %s" % (i + 1, solve_case_single(line))


