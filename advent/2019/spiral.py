# read in space separated tokens from a file and put them in a 2d array, in a spiral
# first line: columns x rows
# next line: the data. Lenght of data guaranteed to be columns x rows
import math
def print_grid(grid):
    for row in grid:
        print(row)

infile=open("spiral.txt")
cols, rows = [int(x) for x in infile.readline().split()]
grid = [['.' for _ in range(cols)] for _ in range(rows)]
data = infile.readline().split()

idx = 0
i = 0
while True:
    # i from 0 to 1
    # top
    top = i
    right = cols - i - 1
    bottom = rows - i - 1
    left = i

    # top
    for col in range(left, right):
        grid[top][col] = data[idx]
        idx += 1
    # right
    for row in range(top, bottom):
        grid[row][right] = data[idx]
        idx+=1
    # bottom
    for col in range(right, left, -1):
        grid[bottom][col] = data[idx]
        idx += 1
        if idx >= rows * cols:
            break
    # left
    for row in range(bottom, top, -1):
        grid[row][left] = data[idx]
        idx += 1
        if idx >= rows * cols:
            break
    if(left == right and top == bottom):
        grid[top][left] = data[idx]
        break
    if idx >= rows * cols:
        break
    i += 1

print_grid(grid)