__author__ = 'julenka'
import itertools

# url to the problem goes here
def helper(n,k):
    if n == 1 and k == 1:
        return 1
    if n == 2 and k == 1:
        return 1

    if k == 1:
        all = list(itertools.permutations(range(n)))
        pairs = []
        count = 0
        for a in all:
            a = list(a)
            my_set = set()
            my_set.add((a[0],a[-1]))
            for i in range(len(a)-1):
                my_set.add((a[i],a[i+1]))
            if my_set not in pairs:
                pairs.append(my_set)
                count += 1
        return count

    table_n = [0 for x in range(k)]
    i = 0
    for x in range(n):
        table_n[i] += 1
        i += 1
        i %= k

    result = 0
    for i in range(len(table_n) - 1, 0, -1):
        others = sum([table_n[i2] for i2 in range(i)])
        result *= helper(table_n[i], 1)
        result = helper(others, i)
    return result

def solve_case_single(line):
    n,k = [int(x) for x in line.split(' ')]
    return "%d" % helper(n,k)

# config
letter = 'C'
# letter = 'B'
# letter = 'A'
# size = 'small'
size = 'large'
size = 'tiny'
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
    result = solve_case_single(line)
    print "Case #%d: %s" % (i + 1, result)
    print >> outf, "Case #%d: %s" % (i + 1, result)

# num_lines1, num_lines2 = [int(x) for x in lines.next().split(' ')]


