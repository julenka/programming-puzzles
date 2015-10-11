#!/usr/bin/env python
# coding=utf-8
""" 
"""
__author__ = 'julenka'
from collections import defaultdict
import numpy as np


def read_tuple_int():
    s = raw_input()
    return [int(x) for x in s.split()]

def fail():
    print "Danger!! Lucifer will trap you"

def success():
    print "Go on get the Magical Lamp"

def merge_colors(npar, c1, c2):
    global num_colors
    npar[npar == c2] = c1
    num_colors -= 1


def get_color(npar, n):
    global max_color, num_colors
    c = npar[n]
    if c == 0:
        max_color += 1
        c = max_color
        npar[n] = c
        num_colors += 1
    return c

def process_case():
    N, M = read_tuple_int()
    outgoing_edges = defaultdict(list)
    out_counts = defaultdict(int)
    in_counts = defaultdict(int)
    colors = np.zeros(N)

    for _ in range(M):
        f, t = [int(x) for x in raw_input().split()]
        outgoing_edges[f].append(t)
        out_counts[f] += 1
        in_counts[t] += 1
        f_color = get_color(colors, f - 1)
        t_color = get_color(colors, t - 1)
        if f_color != t_color:
            merge_colors(colors, f_color, t_color)

    if num_colors != 1:
        return fail()

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


    return success()


if __name__ == '__main__':
    global num_colors, max_color
    T = input()
    for i in range(T):
        max_color = 0
        num_colors = 0
        process_case()
