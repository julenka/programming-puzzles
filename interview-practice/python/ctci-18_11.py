#!/usr/bin/env python
__author__ = 'julenka'
''' CTCI #18.11

Imagine you have a square matrix, where each cell is either black or white. Design an algorithm to find the
maximum subsquare such that all four corners are filled with black pixels.

'''


import sys
import random

grid_size = int(sys.argv[1])

grid = []

for r in xrange(grid_size):
    grid.append([random.randint(0,1) for c in xrange(grid_size)])


print "grid:"
for row in grid:
    print row

max_width = grid_size

# For every possible width, starting from largest...
for width in range(max_width, 1, -1):
    # Examine every possible top left corner
    for r in xrange(0, max_width - width):
        for c in xrange(0, max_width - width):
            coords = [[r,c],[r+width, c], [r, c + width], [r + width, c + width]]
            if reduce(lambda x,y: x + y, [grid[r1][c1] for r1,c1 in coords]) == 4:
                print coords, width
                exit()

print 'none found'


