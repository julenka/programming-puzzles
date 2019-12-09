#!/usr/bin/env python
# coding=utf-8
"""
You are given two arrays A and B:

Array A consists of N elements. Ai (1≤i≤N) is the ith element of array A.
Array B consists of M elements. Bj (1≤j≤M) is the jth element of array B.
Initially Bj=j.
You are given three types of queries:

1 k V: Update the value at kth index in the array A to V, i.e., Ak=V.
2 S1 S2: Find total number of distinct pairs (i, j) such that S1≤Ai+Bj≤S2.
3 L R: Reverse the order of the elements of the array B in the range [L, R] inclusive.
Input Format

The first line of the test case contains three integers N, M and Q. The next line contains N
space separated integers denoting the array A. Each of the next Q lines contains three space
separated integers denoting one of the three queries.

Constraints

1≤N, M, Q≤10**5
1≤Ai, V≤105
1≤k≤N
1≤S1, S2≤2×105
S1≤S2
1≤L, R≤M
L<R
Output Format

Output total number of pairs for each of the second type of query in separate line.

Time Limit

Same as given here except for followings:

C, C++ and Pascal: 1s
C# and D: 2s
Java: 3s
Sample Input
"""
__author__ = 'julenka'

from collections import Counter
import bisect

def op1(A, A_counter, k, v):
    old_v = A[k-1]
    A[k-1] = v
    A_counter[old_v] -= 1
    A_counter[v] += 1

def get_count(s1, s2, k, M):
    max_ai_plus_bj = k + M
    min_ai_plus_bj = k + 1
    min_s1 = max(s1, min_ai_plus_bj)
    max_s2 = min(s2, max_ai_plus_bj)
    return max(0, max_s2 - min_s1 + 1)


def op2(A_counter, s1, s2, M):
    result = 0
    min_value = max(0, s1 - M - 1)
    max_value = s2
    for k in xrange(min_value, max_value + 1):
        v = A_counter[k]
        if v == 0:
            continue
        result += get_count(s1, s2, k, M) * v

    return int(result)

import numpy as np
if __name__ == '__main__':
    N, M, Q = [int(x) for x in raw_input().split()]
    A = [int(x) for x in raw_input().split()]
    A_counter = np.zeros(10**5 + 1)
    for a in A:
        A_counter[a] += 1
    for _ in xrange(Q):
        a, b, c = ([int(x) for x in raw_input().split()])
        if a == 1:
            op1(A, A_counter, b, c)
        elif a == 2:
            print op2(A_counter, b, c, M)
