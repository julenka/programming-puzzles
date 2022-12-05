from helpers import parse_lines_regex
import re
from collections import Counter

def solve():
    lines = parse_lines_regex("input-02-a.txt", r"^(\d+)-(\d+) (\w): (\w+)$")
    
    valid_count_p1 = 0
    valid_count_p2 = 0
    for int1, int2, letter, pswd in lines:
        int1 = int(int1)
        int2 = int(int2)
        pswd_counter = Counter(pswd)
        letter_count = pswd_counter[letter]
        if letter_count >= int1 and letter_count <= int2:
            valid_count_p1 += 1
        
        pos1_contains = pswd[int1 - 1] == letter
        pos2_contains = pswd[int2 - 1] == letter
        if pos1_contains != pos2_contains:
            valid_count_p2 += 1
    
    print("part 1: " + str(valid_count_p1))
    print("part 2: " + str(valid_count_p2))

solve()