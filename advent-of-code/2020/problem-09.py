from helpers import get_int_values
from itertools import combinations

def find_two_prev(num_list, goal):
    for x, y in combinations(num_list, 2):
        if x + y == goal:
            return x, y
    return None

def solve2():
    goal_val = 3199139634
    input = get_int_values("input-09.txt")
    
    contig_min_len = 2
    contig_max_len = 100
    max_line_idx = 684
    for region_len in range(contig_min_len, contig_max_len):
        for start_idx in range(max_line_idx - region_len):
            candidate = input[start_idx:start_idx+region_len]
            if sum(candidate) == goal_val:
                print(f"part 2: {min(candidate) + max(candidate)}")
                return

def solve1():
    input = get_int_values("input-09.txt")
    preamble_len = 25
    for start_i in range(len(input) - preamble_len - 1):
        test_lst = input[start_i:start_i+preamble_len]
        test_val = input[start_i+preamble_len]
        if find_two_prev(test_lst, test_val) is None:
            print (f"part 1: {test_val}")
    pass

solve2()