from helpers import get_lines
import math

def get_priority(char):
    ord_char = ord(char)
    if ord_char < ord('a'): # Upper case,  A-Z is 27 - 52
        return 27 + ord_char - ord('A')
    # lower case a-z is 1 - 26
    return 1 + ord_char - ord('a')

def solve1(data):
    total_count = 0
    for line in data:
        half_line_len = int(len(line) / 2)
        first_half_set = set(line[:half_line_len])
        for char in line[half_line_len:]:
            if char in first_half_set:
                total_count += get_priority(char)
                print(char)
                break
    print(total_count)

def solve2(data):
    total_count = 0
    for i in range(0, len(data), 3):
        first_elf_set = set(data[i])
        second_elf_set = set(data[i + 1])
        third_elf_set = set(data[i + 2])
        for badge in first_elf_set:
            if badge in second_elf_set and badge in third_elf_set:
                print(badge)
                total_count += get_priority(badge)
                break
    print(total_count)

test_data = '''
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''

# data = test_data.strip().split("\n")
data = get_lines("input-03.txt")

solve2(data)