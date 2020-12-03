from helpers import get_lines
def trees_encountered(toboggan_map, slope_col, slope_row):
    num_trees = 0
    num_cols = len(toboggan_map[0])
    for i in range(1, int(len(toboggan_map) / slope_row)):
        row = slope_row * i
        column = (i * slope_col) % num_cols
        num_trees += toboggan_map[row][column] 
    return num_trees

def solve():
    lines = get_lines("input-03.txt")
    toboggan_map = list()
    for line in lines:
        toboggan_map.append([0 if c == '.' else 1 for c in line.strip()])
    trees_1_1 = trees_encountered(toboggan_map, 1, 1)
    trees_3_1 = trees_encountered(toboggan_map, 3, 1)
    trees_5_1 = trees_encountered(toboggan_map, 5, 1)
    trees_7_1 = trees_encountered(toboggan_map, 7, 1)
    trees_1_2 = trees_encountered(toboggan_map, 1, 2)
    print("part1: " + str(trees_3_1))
    print("part2: " + str(trees_1_1 * trees_1_2 * trees_3_1 * trees_5_1 * trees_7_1))

solve()