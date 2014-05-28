__author__ = 'julenka'
import math
# url to the problem goes here

def choose(n, k):
    if(n == 0 or k == 0): return 1
    f = math.factorial
    return f(n) / (f(k) * f(n - k))

def helper(n, k):
    # n is guaranteed to divide k here
    if(n == 0 or k == 0): return 1

    n_per_table = n / k
    # pick first person, doesn't matter who it is. let's just say it's the smallest member
    # pick his neighbors.
    num_ways_to_pick_neighbors = choose(n - 1, n_per_table - 1)
    num_ways_to_arrange_single_table = math.ceil(math.factorial(n_per_table - 1) / 2.0)
    return int(num_ways_to_pick_neighbors * num_ways_to_arrange_single_table * helper(n - n_per_table, k - 1))

def solve_case_single(line):
    # n people, k tables
    n,k = [int(x) for x in line.split(' ')]

    small_per_table = math.floor(float(n)/k)
    small_num_tables = k - (n % k)
    small_num_people = small_per_table * small_num_tables

    big_per_table = math.ceil(float(n)/k)
    big_num_tables = n % k
    big_num_people = big_per_table * big_num_tables

    return choose(n, big_num_people) * helper(small_num_people, small_num_tables) * helper(big_num_people, big_num_tables)

# config
letter = 'C'
# letter = 'B'
# letter = 'A'
# size = 'small'
size = 'large'
# size = 'tiny'
input = '%s-%s-practice.in' % (letter,size)
output = input.replace('.in', '.out')
lines = (line.strip() for line in open(input).readlines())
outf = open(output, 'w')
num_cases = int(lines.next())


for i in range(num_cases):
    line = lines.next()
    result = solve_case_single(line)
    print "Case #%d: %s" % (i + 1, result)
    print >> outf, "Case #%d: %s" % (i + 1, result)



