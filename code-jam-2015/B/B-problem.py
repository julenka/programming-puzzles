__author__ = 'julenka'
import math
# url to the problem goes here

def solve_case_single(line):
    A,B,alpha,beta,Y = [int(x) for x in line.split(' ')]
    # print alpha, beta
    # check: if last same as cur, then just return cur
    Y = int(Y)

    for i in xrange(Y):
        last_B = B
        last_A = A
        a_die = A / 100
        b_die = B  / 100
        K = (min(A,B)  / 50)

        a_new = (K * alpha) / 100
        b_new = (K * beta) / 100
        remainder = int(K - (a_new + b_new))
        # print remainder
        a_new_tot = a_new + remainder / 2
        b_new_tot = b_new + remainder / 2 + remainder % 2
        # print K, a_new, b_new, remainder, a_new_tot, b_new_tot, a_die, b_die
        A = A + a_new_tot - a_die
        B = B + b_new_tot - b_die
        # print A,B
        if last_B == B and last_A == A:
            return "%d %d" % (A, B)

    return "%d %d" % (A, B)

# config
# letter = 'C'
letter = 'B'
# letter = 'A'
size = 'small'
size = 'large'
# size = 'tiny'
input = '%s-%s-practice.in' % (letter,size)
# input = '%s-%s-practice.in' % (letter,size)
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
    result = solve_case_single(line)
    print "Case #%d: %s" % (i + 1, result)
    print >> outf, "Case #%d: %s" % (i + 1, result)

# num_lines1, num_lines2 = [int(x) for x in lines.next().split(' ')]


