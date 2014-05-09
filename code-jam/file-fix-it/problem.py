__author__ = 'julenka'
import os
# url to the problem goes here

def solve_case_multi(existing_dirs, new_dirs):
    e_set = set(['/'])
    print existing_dirs, new_dirs
    for d in existing_dirs:
        e_set.add(d)
        h,t = os.path.split(d)
        e_set.add(h)
        while h != '/':
            e_set.add(h)
            h,t = os.path.split(h)

    print e_set
    count = 0
    for d in new_dirs:
        if d not in e_set:
            count += 1
            e_set.add(d)
        h,t = os.path.split(d)
        if h not in e_set:
            count += 1
            e_set.add(h)
        while h != '/':
            h,t = os.path.split(h)
            if h not in e_set:
                e_set.add(h)
                count += 1
    print "after:", e_set
    return count

# config
# letter = 'C'
# letter = 'B'
letter = 'A'
size = 'small'
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
    num_lines1, num_lines2 = [int(x) for x in lines.next().split(' ')]
    case_lines1 = []
    case_lines2 = []
    for j in range(num_lines1):
        case_lines1.append(lines.next())
    for j in range(num_lines2):
        case_lines2.append(lines.next())
    result = solve_case_multi(case_lines1, case_lines2)
    print "Case #%d: %s" % (i + 1, result)
    print >> outf, "Case #%d: %s" % (i + 1, result)


