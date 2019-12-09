#problem2.py
import itertools
import random

def init_program():
    infile = "input-2.txt"
    with open(infile) as f:
        line = f.readline()
        return [int(x) for x in line.split(",")]

def run_program(cells, noun, verb):
    i = 0
    cells[1] = noun
    cells[2] = verb
    opcode = cells[i]
    while(opcode != 99):
        a = cells[cells[i+1]]
        b = cells[cells[i+2]]
        writepos = cells[i+3]
        rslt = a + b if opcode == 1 else a * b
        cells[writepos] = rslt
        i = i + 4
        opcode = cells[i]
    result = cells[0]
    print(f"run_program({noun}, {verb}) = {result}")
    return result

def part1():
    cells = init_program()    
    run_program(cells, 12, 2)

def part2():
    pairs = itertools.product(range(0, 99), repeat=2)
    for noun, verb in pairs:
        cells = init_program()    
        output = run_program(cells, noun, verb)
        if (output == 19690720):
            exit(0)

part2()