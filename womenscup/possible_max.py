#!/usr/bin/env python
# coding=utf-8
"""
You are given a set S = {1, 2, 3,…,N}.
Find two integers A and B (A<B) from the set S such that the value of A & B is the maximum possible and less than the given integer K.
In this case, & represents the operator bitwise AND.

Input Format

The first line of input is T: total number of test cases. Each of the next T lines contains two space separated integers N and K.
"""
__author__ = 'julenka'


def process_line(line):
    n, k = [int(x) for x in line.split()]
    for max_val in xrange (k - 1, -1, -1):
        for a in range(1, n+1):
            if a == max_val:
                continue
            if a & max_val == max_val:
                print max_val
                return
    # for a in xrange(1, n + 1):
    #     for b in xrange(1, a):
    #         if a & b < k and a & b > max_val:
    #             max_val = a & b
    # print max_val

if __name__ == '__main__':
    t = input()

    for _ in range(t):
        line = raw_input()
        process_line(line)

N, T = [int(x) for x in raw_input().split()]
