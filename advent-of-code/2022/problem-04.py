from helpers import get_lines
import math


def get_min_max(text):
    return (int(x) for x in text.split("-"))

def solve1(data):
    total_count = 0
    for line in data:
        first_range, second_range = line.split(",")
        first_min, first_max = get_min_max(first_range)
        second_min, second_max = get_min_max(second_range)
        if first_min <= second_min and first_max >= second_max or first_min >= second_min and first_max <= second_max:
            print(line)
            total_count += 1
    print(total_count)

def solve2(data):
    total_count = 0
    for line in data:
        first_range, second_range = line.split(",")
        first_min, first_max = get_min_max(first_range)
        second_min, second_max = get_min_max(second_range)
        doesnt_overlap = first_max < second_min or first_min > second_max
        if not doesnt_overlap:
            print(line)
            total_count += 1
    print(total_count)

test_data = '''
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''

# data = test_data.strip().split("\n")
data = get_lines("input-04.txt")

solve2(data)