__author__ = 'julenka'
# url to the problem goes here
# https://code.google.com/codejam/contest/2994486/dashboard#s=p1
import math

class State:
    ''' Track the maximum that the node can take, its current value, and the number of empty bits, e.g. number
    of bits that need to still be set. We start from most significant bit.
    '''
    def __init__(self, maxval, cur, empty_bits):
        self.maxval = maxval
        self.cur = cur
        self.empty_bits = empty_bits

def bin(s):
    return str(s) if s<=1 else bin(s>>1) + str(s&1)

def solve_case_helper(a, b, k):
    ''' Returns the number of solutions s.t. A < a.cur and B < b.cur s.t. A & B < K

    Recursion progresses by adding one bit to solution space to both a and b, going from MSB to LSB
    '''
    if(a.cur >= a.maxval or b.cur >= b.maxval):
        # current value is too big, exit early. Shouldn't get here.
        return 0
    if(a.empty_bits == 0 and b.empty_bits == 0):
        # we are at a leaf node, no more bits to fill in
        if a.cur & b.cur < k:
            return 1
        return 0

    # If the current value is already too big, then stop exploring solution space, all children will be larger
    if a.cur & b.cur > k:
        return 0

    a_ones = (1 << a.empty_bits) - 1
    b_ones = (1 << b.empty_bits) - 1
    max_a = a.cur + a_ones
    max_b = b.cur + b_ones
    if max_a & max_b < k:
        # If the largest possible value we can achieve is already less than k, we can also stop early.
        # however, we need to be careful about how many valid solutions are below this number
        a_f = a_ones + 1
        b_f = b_ones + 1
        if a.maxval <= max_a:
            a_f = a.maxval & a_ones
        if b.maxval <= max_b:
            b_f = b.maxval & b_ones

        return a_f * b_f

    b0 = State(b.maxval, b.cur, b.empty_bits - 1)
    a0 = State(a.maxval, a.cur, a.empty_bits - 1)
    b1 = State(b.maxval, b.cur + (1 << (b.empty_bits - 1)), b.empty_bits - 1)
    a1 = State(a.maxval, a.cur + (1 << (a.empty_bits - 1)), a.empty_bits - 1)
    return solve_case_helper(a0, b1, k) + solve_case_helper(a0, b0, k) + solve_case_helper(a1, b0, k ) + solve_case_helper(a1, b1, k)


def solve_case_single(line):
    a,b,k = [int(x) for x in line.split(' ')]
    a_hibit, b_hibit = 32, 32
    return solve_case_helper(State(a, 1 << a_hibit, a_hibit), State(b, 0, b_hibit), k) + \
        solve_case_helper(State(a, 1 << a_hibit, a_hibit), State(b, 1 << b_hibit, b_hibit), k) + \
        solve_case_helper(State(a, 0, a_hibit), State(b, 0, b_hibit), k) + \
        solve_case_helper(State(a, 0, a_hibit), State(b, 1 << b_hibit, b_hibit), k)

# config
letter = 'B'
# size = 'small'
# size = 'tiny'
size = 'large'
input = '%s-%s-practice.in' % (letter,size)
output = input.replace('.in', '.out')
lines = (line.strip() for line in open(input).readlines())
outf = open(output, 'w')
num_cases = int(lines.next())


for i in range(num_cases):
    line = lines.next()
    # print line
    print "Case #%d: %s" % (i + 1, solve_case_single(line))
    print >> outf, "Case #%d: %s" % (i + 1, solve_case_single(line))


