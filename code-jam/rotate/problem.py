__author__ = 'julenka'

# url to the problem goes here

def solve_case_multi(board, k):

    r = len(board)
    # shift
    shifted_board = []
    for row in board:
        l1 = len(row)
        row = row.replace('.','')
        row = '.' * (l1 - len(row)) + row
        shifted_board.append(row)

    board = shifted_board
    print '\n'.join(board)
    # look for k in a row
    players = ['Red','Blue']
    winners = []
    print k
    for p in players:
        pc = p[0]
        found = False
        for i in xrange(r):
            for j in xrange(r):
                if found:
                    continue

                if i <= r - k:
                    # vertical down, up
                    found = True
                    for l in xrange(k):
                        if board[i + l][j] != pc:
                            found = False
                            break
                    if found:
                        winners.append(p)
                        continue

                    if j >= k - 1:
                        found = True
                        # diagonal left
                        for l in xrange(k):
                            if board[i + l][j - l] != pc:
                                found = False
                                break
                        if found:
                            winners.append(p)
                            continue

                    if j <= r - k:
                        # diagonal right
                        found = True
                        for l in xrange(k):
                            if board[i + l][j + l] != pc:
                                found = False
                                break
                        if found:
                            winners.append(p)
                            continue

                if j <= r - k:
                    # horizontal right, left
                    # vertical
                    found = True
                    for l in xrange(k):
                        if board[i][j + l] != pc:
                            found = False
                            break
                    if found:
                        winners.append(p)
                        continue



    if len(winners) == 2:
        return 'Both'
    if len(winners) == 0:
        return 'Neither'
    return winners[0]

def solve_case_single(line):
    return None

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
    num_lines1, num_lines2 = [int(x) for x in lines.next().split(' ')]
    case_lines = []
    for j in range(num_lines1):
        case_lines.append(lines.next())
    result = solve_case_multi(case_lines, num_lines2)
    print "Case #%d: %s" % (i + 1, result)
    print >> outf, "Case #%d: %s" % (i + 1, result)


# num_lines1, num_lines2 = [int(x) for x in lines.next().split(' ')]


