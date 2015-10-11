#!/usr/bin/env python
# coding=utf-8
""" 
"""
__author__ = 'julenka'
from collections import defaultdict
from collections import deque
def read_tuple_int():
    s = raw_input()
    return [int(x) for x in s.split()]

def fail():
    print "Danger!! Lucifer will trap you"

def success():
    print "Go on get the Magical Lamp"

import numpy as np
def process_case():
    N, M = read_tuple_int()
    outgoing_edges = defaultdict(list)
    out_counts = defaultdict(int)
    in_counts = defaultdict(int)
    dirty_bits_2 = np.zeros(N+1)
    dirty_bits = np.zeros(N+1)

    for _ in range(M):
        f, t = [int(x) for x in raw_input().split()]
        outgoing_edges[f].append(t)
        out_counts[f] += 1
        in_counts[t] += 1
        dirty_bits_2[f] = 1
        dirty_bits_2[f] = 1

    if out_counts[N] == 0:
        fail()
        return
    if out_counts[1] == 0:
        fail()
        return

    for k, v in out_counts.iteritems():
        if in_counts[k] != v:
            fail()
            return

    q = deque([1])

    while len(q) > 0:
        cur = q.popleft()
        dirty_bits[cur] = 1
        nodes_to_visit = outgoing_edges[cur]
        for node in nodes_to_visit:
            if dirty_bits[node] == 1:
                continue
            q.append(node)

    if dirty_bits[N] == 0:
        fail()
        return

    if dirty_bits.sum() != dirty_bits_2.sum():
        fail()
        return
    success()


if __name__ == '__main__':
    T = input()
    for i in range(T):
        process_case()
