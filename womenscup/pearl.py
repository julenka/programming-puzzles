#!/usr/bin/env python
# coding=utf-8
"""
The state of California is facing a serious drought. Antony wants to save the state by winning the heart of Tialoc, the supreme rain god. Tialoc gives Antony a task to complete first. He gives Antony N pearls. These pearls are magical. When Antony restrings two pearls together, the two pearls combine to make a single pearl. Each pearl has an associated cost. When the two pearls become one, the value of each individual pearl is added together to become the value of the combined pearl. Antony has to restring N pearls together in such a way that the cost of the final pearl is the absolute minimum. Antony can only restring two pearls at a time. Succeeding in this task will cause Tialoc to shower California with rain! Help Antony restring the pearls!

Input Format

The first line contains N: the number of pearls. The next line contains ci of N pearls separated by a space.

Constraints
1≤N≤2×106
1≤ci≤109 where ci is cost of ith pearl

Output Format

One and only line of output is the minimum cost for making the necklace. As the cost can be very large, output cost modulo (109+7).
"""
__author__ = 'julenka'

import heapq
from collections import deque

if __name__ == '__main__':
    N = input()
    line = raw_input()
    print "reading costs.."
    costs = [int(x) for x in line.split()]
    print "done reading costs"
    total_cost = 0
    print "heapify"
    heapq.heapify(costs)
    print "heapify done"
    while len(costs) > 1:
        c1 = heapq.heappop(costs)
        c2 = heapq.heappop(costs)
        c3 = c1 + c2
        total_cost += c3
        heapq.heappush(costs, c3)
    print total_cost % (10 ** 9 + 7)

    # costs = deque(costs)
    # while len(costs) > 1:
    #     c1 = costs.popleft()
    #     c2 = costs.popleft()
    #     c3 = c1 + c2
    #     total_cost += c3
    #     costs.append(c3)
