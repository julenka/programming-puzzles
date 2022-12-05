from helpers import get_lines
import math



def solve1(data):
    total_cal = 0
    max_cal = 0
    for line in data:
        if len(line) == 0:
            if total_cal > max_cal:
                max_cal = total_cal
            total_cal = 0
        else:
            total_cal += int(line)
    print(f"solve1 max_cal result is: {max_cal}")

def solve2(data):
    total_cal = 0
    calories_per_elf = list()
    for line in data:
        if len(line) == 0:
            calories_per_elf.append(int(total_cal))
            total_cal = 0
        else:
            total_cal += int(line)
    calories_per_elf.append(total_cal)
    calories_per_elf = sorted(calories_per_elf)
    first = calories_per_elf[-1]
    second = calories_per_elf[-2]
    third = calories_per_elf[-3]
    print(f"{first} + {second} + {third} = {first + second + third}")

test_data = '''
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
'''

# data = test_data.strip().split("\n")
data = get_lines("input-01.txt")

# solve1(data)
solve2(data)