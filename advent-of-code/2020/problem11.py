from helpers import get_lines

test_data = '''
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
'''

# test_data = '''
# #.##.##.##
# #######.##
# #.#.#..#..
# ####.##.##
# #.##.##.##
# #.#####.##
# ..#.#.....
# ##########
# #.######.#
# #.#####.##
# '''

data = test_data.split("\n")[1:-1]

data = get_lines("input-11.txt")


def num_adjacent_occupied(map, row, col):
    num_rows = len(map)
    num_cols = len(map[0])
    result = 0
    for row_offset in range(-1,2):
        for col_offset in range(-1, 2):
            if row_offset == 0 and col_offset == 0:
                continue
            new_row = row + row_offset
            new_col = col + col_offset
            if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
                continue
            if map[new_row][new_col] == "#":
                result += 1
    return result

def num_see_cardinal(map, row, col):
    num_rows = len(map)
    num_cols = len(map[0])
    result = 0
    #n
    for step in range(row):
        test_row = row - step - 1
        test_col = col
        if map[test_row][test_col] == "#":
            result += 1
            break
        if map[test_row][test_col] == "L":
            break
    #ne
    n_steps = min(row, num_cols - col - 1)
    for step in range(n_steps):
        test_row = row - step - 1
        test_col = col + step + 1
        if map[test_row][test_col] == "#":
            result += 1
            break
        if map[test_row][test_col] == "L":
            break
    
    #e
    for step in range(num_cols - col - 1):
    
        test_col = col + step + 1
        test_row = row
        if map[test_row][test_col] == "#":
            result += 1
            break
        if map[test_row][test_col] == "L":
            break
    #se
    n_steps = min(num_rows - row - 1, num_cols - col - 1)
    for step in range(n_steps):
        test_row = row + step + 1
        test_col = col + step + 1
        if map[test_row][test_col] == "#":
            result += 1
            break
        if map[test_row][test_col] == "L":
            break
    #s
    n_steps = num_rows - row - 1
    for step in range(n_steps):
        test_row = row + step + 1
        test_col = col
        if map[test_row][test_col] == "#":
            result += 1
            break
        if map[test_row][test_col] == "L":
            break
    #sw
    n_steps = min(col, num_rows - row - 1)
    for step in range(n_steps):
        test_row = row + step + 1
        test_col = col - step - 1
        if map[test_row][test_col] == "#":
            result += 1
            break
        if map[test_row][test_col] == "L":
            break
    #w
    n_steps = col
    for step in range(n_steps):
        test_row = row
        test_col = col - step - 1
        if map[test_row][test_col] == "#":
            result += 1
            break
        if map[test_row][test_col] == "L":
            break
    #nw
    n_steps = min(col, row)
    for step in range(n_steps):
        test_row = row - step - 1
        test_col = col - step - 1
        if map[test_row][test_col] == "#":
            result += 1
            break
        if map[test_row][test_col] == "L":
            break
    return result

def apply_round(map):
    result = map.copy()
    num_rows = len(map)
    num_cols = len(map[0])
    for row in range(num_rows):
        for col in range(num_cols):
            spot = map[row][col]
            if spot == ".":
                continue
            num_adj_oc = num_see_cardinal(map, row, col)
            if spot == "L":
                if num_adj_oc == 0:
                    l = list(result[row])
                    l[col] = "#"
                    result[row] = "".join(l)
            if spot == "#":
                if num_adj_oc >= 5:
                    l = list(result[row])
                    l[col] = "L"
                    result[row] = "".join(l)
    return result

def tostring(map):
    return "\n".join(map)

# print(f"{num_see_cardinal(data, 0, 0)}")

prev_round = data
round_num = 0
while True:
    round_num += 1
    cur_round = apply_round(prev_round)
    print(tostring(cur_round))
    # if round_num == 3:
    #     break
    if tostring(cur_round) == tostring(prev_round):
        break
    print()
    prev_round = cur_round
num_occupied = sum([1 if x == "#" else 0 for x in tostring(cur_round)])
print(f"part1: {num_occupied}")
    
