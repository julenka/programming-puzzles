__author__ = 'julenka'

# url to the problem goes here

def solve_case_single(line):
    l = len(line)
    l2 = '| %s |' % line
    l1 = '+-%s-+' % ('-' * len(line))
    return "\n" + l1 + "\n" + l2 + '\n' + l1

# config
# letter = 'C'
# letter = 'B'
letter = 'A'
size = 'small'
# size = 'large'
# size = 'tiny'
input = '%s-%s-attempt0.in' % (letter,size)
output = input.replace('.in', '.out')
lines = (line.replace('\n', '') for line in open(input).readlines())
outf = open(output, 'w')
num_cases = int(lines.next())


# model 2:
# lines
# case1
# case2
# ...
for i in range(num_cases):
    line = lines.next()
    result = solve_case_single(line)
    print "Case #%d: %s" % (i + 1, result)
    print >> outf, "Case #%d: %s" % (i + 1, result)

# num_lines1, num_lines2 = [int(x) for x in lines.next().split(' ')]


