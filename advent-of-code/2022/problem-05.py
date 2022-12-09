from helpers import get_lines
import math
import re


def solve1(data):
    stacks = []
    for line in test_stacks.strip().split("\n"):
        stacks.append(list(line))
    print(stacks)

    for line in data:
        if not line.startswith("move"):
            continue
        # r"^(\d+)-(\d+) (\w): (\w+)$"
        regex_instruction = r"^move (\d+) from (\d+) to (\d+)$"
        match = re.match(regex_instruction, line)
        if match:
            move_quantity, move_from, move_to = match.groups()
            for i in range(int(move_quantity)):
                print(i)
                from_idx = int(move_from) - 1
                to_idx = int(move_to) - 1
                item_to_move = stacks[from_idx].pop()
                stacks[to_idx].append(item_to_move)
                print(stacks)
        else:
            raise(f"line {line} did not match regex")
    result = ""
    for stack in stacks:
        result += stack[-1]
    print(result)

def solve2(data):
    stacks = []
    for line in test_stacks.strip().split("\n"):
        stacks.append(list(line))
    print(stacks)

    for line in data:
        if not line.startswith("move"):
            continue
        regex_instruction = r"^move (\d+) from (\d+) to (\d+)$"
        match = re.match(regex_instruction, line)
        if match:
            move_quantity, move_from, move_to = match.groups()
            move_quantity = int(move_quantity)
            move_from_idx = int(move_from) - 1
            move_to_idx = int(move_to) - 1
            chunk_to_move = []
            for _ in range(move_quantity):
                chunk_to_move.append(stacks[move_from_idx].pop())
            for _ in range(move_quantity):
                stacks[move_to_idx].append(chunk_to_move.pop())
        else:
            raise(f"line {line} did not match regex")
    result = ""
    for stack in stacks:
        result += stack[-1]
    print(result)

# test_stacks ='''
# ZN
# MCD
# P
# '''

test_stacks='''
HRBDZFLS
TBMZR
ZLCHNS
SCFJ
PGHWRZB
VJZGDNMT
GLNWFSPQ
MZR
MCLGVRT
'''

test_data = '''
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''

# data = test_data.strip().split("\n")
data = get_lines("input-05.txt")

solve2(data)