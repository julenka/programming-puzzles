# problem5.py


def init_program():
    infile = "input5.txt"
    with open(infile) as f:
        line = f.readline()
        return [int(x) for x in line.split(",")]

def read_param(mode, cells, param):
    print(f"read_param({mode}, cells, {param})")
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

def run_program(cells, input):
    i = 0
    outputs = list()
    cells_outputs = list()
    cur_inst = cells[i]
    opcode = get_opcode(cur_inst)
    prev_cell = -1
    while(opcode != 99):
        inst_1 = cur_inst
        if opcode < 3:
            inst_1 = inst_1 // 100
            param_mode_a = inst_1 % 10
            inst_1 = inst_1 // 10
            param_mode_b = inst_1 % 10
            inst_1 = inst_1 // 10
            param_mode_c = inst_1 % 10

            a = read_param(param_mode_a, cells, cells[i+1])
            b = read_param(param_mode_b, cells, cells[i+2])
            # assume when writing that you always get the position
            writepos = cells[i+3]
            print(f"i = {i} instruction = {cur_inst} a = {a} b = {b} writepos = {writepos}")
            rslt = a + b if opcode == 1 else a * b
            cells[writepos] = rslt
            i = i + 4
        if opcode == 3:
            inst_1 = inst_1 // 100
            param_mode_a = inst_1 % 10
            print(f"i = {i} inst = {cur_inst}")
            
            if (param_mode_a != 0):
                raise("opcode 3 but param code is not zero")
            print(f"write value {input} to index {cells[i+1]}")
            cells[cells[i+1]] = input
            i = i + 2
        if opcode == 4:
            inst_1 = inst_1 // 100
            param_mode_a = inst_1 % 10
            print(f"OPCODE 4 i = {i} inst = {cur_inst}")
            a = read_param(param_mode_a, cells, cells[i+1])
            outputs.append(a)
            cells_outputs.append(prev_cell)
            i = i + 2
        prev_cell = cur_inst
        cur_inst = cells[i]
        opcode = get_opcode(cur_inst)

    for out, inst in zip(outputs, cells_outputs):
        print(f"{out}, {inst}")



cells = init_program()
run_program(cells, 1)