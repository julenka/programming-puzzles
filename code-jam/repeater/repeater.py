__author__ = 'julenka'

# url to the problem goes here
# https://code.google.com/codejam/contest/2994486/dashboard

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

def solve_case(lines):
    # [[ (char, repeat),... ], ... ]
    e1 = []
    chars = set()
    for line in lines:
        e2 = [[line[0], 1]]
        for i in range(1, len(line)):
            c = e2[-1][0]
            if(line[i] == c):
                e2[-1][1] = e2[-1][1] + 1
            else:
                e2.append([line[i],1])
        e1.append(e2)
        chars.add(''.join([pair[0] for pair in e2]))
    if len(chars) > 1:
        return "Fegla Won"

    total = 0
    for i in range(len(e1[0])):
        repeats = [p[i][1] for p in e1]
        median = sorted(repeats)[len(repeats) / 2]
        for r in repeats:
            total += abs(r - median)
    return str(total)

for i in range(num_cases):
    num_lines = int(lines.next())
    case_lines = []
    for j in range(num_lines):
        case_lines.append(lines.next())
    print "Case #%d: %s" % (i + 1, solve_case(case_lines))
    print >> outf, "Case #%d: %s" % (i + 1, solve_case(case_lines))



