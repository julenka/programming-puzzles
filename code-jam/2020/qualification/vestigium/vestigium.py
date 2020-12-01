#!/usr/bin/env python2

import fileinput
import math

# url to the problem goes here
# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020993c


def solve_case_multi(lines):
    N = len(lines)
    rows = [[int(x) for x in line.split(" ")] for line in lines]
    cols = [[row[i] for row in rows] for i in range(N)]
    row_uniq = [len(set(row)) for row in rows]
    col_uniq = [len(set(col)) for col in cols]
    trace = 0
    for row_num, row in enumerate(rows):
        trace += row[row_num]
    return "%d %d %d" % (trace, 
        sum([1 if i != N else 0 for i in row_uniq]), 
        sum([1 if i != N else 0 for i in col_uniq]))


# Input is now coming from system.in
# output is system.out
lines = (line.strip() for line in fileinput.input())
num_cases = int(lines.next())

for i in range(num_cases):
    num_lines = int(lines.next())
    case_lines = []
    for j in range(num_lines):
        case_lines.append(lines.next())
    result = solve_case_multi(case_lines)
    print "Case #%d: %s" % (i + 1, result)