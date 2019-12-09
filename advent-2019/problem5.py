# problem5.py


def init_program():
    infile = "input5.txt"
    # infile = "input5-test.txt"
    with open(infile) as f:
        line = f.readline()
        return [int(x) for x in line.split(",")]

def read_param(mode, cells, param):
    # print(f"read_param({mode}, cells, {param})")
    if mode == 0:
        # position mode
        return cells[param]
    if mode == 1:
        # immedaite mode
        return param
    else:
        print(f"invalid param mode {mode}")
        exit(1)

def get_opcode(cell):
    return cell % 100

def read_param_number(cell, param_number, cells, inst_pointer):
    # cut off the opcode
    cell = cell // 100
    ptmp = param_number
    while ptmp > 1:
        ptmp -= 1
        cell = cell // 10
    param_mode = cell % 10
    return read_param(param_mode, cells, cells[inst_pointer + param_number])

def run_program(cells, input):
    print(cells)
    i = 0
    outputs = list()
    cur_inst = cells[i]
    opcode = get_opcode(cur_inst)
    while(opcode != 99):
        if opcode < 3:
            a = read_param_number(cur_inst, 1, cells, i)
            b = read_param_number(cur_inst, 2, cells, i)

            # assume when writing that you always get the position
            writepos = cells[i+3]
            print(f"i = {i} instruction = {cur_inst} a = {a} b = {b} writepos = {writepos}")
            rslt = a + b if opcode == 1 else a * b
            cells[writepos] = rslt
            i = i + 4
        if opcode == 3:
            print(f"i = {i} inst = {cur_inst}")
            print(f"OPCODE 3 input {input} to index {cells[i+1]}")
            cells[cells[i+1]] = input
            i = i + 2
        if opcode == 4:
            a = read_param_number(cur_inst, 1, cells, i)
            print(f"OPCODE 4 i = {i} inst = {cur_inst} a = {a}")
            outputs.append(a)
            i = i + 2
        if opcode == 5:
            # Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
            a = read_param_number(cur_inst, 1, cells, i)
            b = read_param_number(cur_inst, 2, cells, i)
            print(f"OPCODE 5 i = {i} inst = {cur_inst} a = {a} b = {b}")
            if a != 0:
                i = b
            else:
                i = i + 3
        if opcode == 6:
            a = read_param_number(cur_inst, 1, cells, i)
            b = read_param_number(cur_inst, 2, cells, i)
            print(f"OPCODE 6 i = {i} inst = {cur_inst} a = {a} b = {b}")
            if a == 0:
                i = b
            else:
                i = i + 3
        if opcode == 7:
            # Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
            a = read_param_number(cur_inst, 1, cells, i)
            b = read_param_number(cur_inst, 2, cells, i)
            c = cells[i+3]
            print(f"OPCODE 7 i = {i} inst = {cur_inst} a = {a} b = {b} c = {c}")

            if a < b:
                cells[c] = 1
            else:
                cells[c] = 0
            i = i + 4
        if opcode == 8:
            # Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
            a = read_param_number(cur_inst, 1, cells, i)
            b = read_param_number(cur_inst, 2, cells, i)
            c = cells[i+3]
            print(f"OPCODE 8 i = {i} inst = {cur_inst} a = {a} b = {b} c = {c}")
            if a == b:
                cells[c] = 1
                print(f"write 1 to position {c}")
            else:
                cells[c] = 0
                print(f"write 0 to position {c}")
            i = i + 4



        cur_inst = cells[i]
        opcode = get_opcode(cur_inst)

    for out in outputs:
        print(out)
    return outputs



cells = init_program()
run_program(cells,5)
