#!/usr/bin/env python
# coding=utf-8
""" 
"""
__author__ = 'julenka'

import random
def make_testcase(N, M, path):
    with open(path, "w") as f:
        f.write("2\n")
        f.write("%d %d\n" % (N, M))
        for _ in range(M):
            edge_from = random.randint(1, N)
            edge_to = random.randint(1, N)
            f.write("%d %d\n" % (edge_from, edge_to))

        f.write("%d %d\n" % (N, M))
        for i in range(1, M + 1):
            edge_from = i
            edge_to = i + 1
            if edge_to == M + 1:
                edge_to = 1
            f.write("%d %d\n" % (edge_from, edge_to))
            f.write("%d %d\n" % (edge_to, edge_from))


if __name__ == '__main__':

    make_testcase(10**6, 2 * 10**6, "cabalistic_input2.txt")