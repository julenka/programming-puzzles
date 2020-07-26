#problem1.py
import math

def part1():
    f = open("input-1a.txt")
    lines = f.readlines()
    freq = 0
    for l in lines:
        i = int(l)
        freq += math.floor(i / 3) - 2
        print(freq)

def part2():
    f = open("input-1a.txt")
    lines = f.readlines()
    total = 0
    for l in lines:
        test = 0
        i = int(l)
        newfuel = max(0, math.floor(i / 3) - 2)
        while newfuel > 0:
            total += newfuel
            test += newfuel
            newfuel = max(0, math.floor(newfuel / 3) - 2)

        print(i, test)
    print("answer:", total)

part2()