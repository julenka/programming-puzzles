# 5 amplifiers
# each amplifier is running a copy of the program

# it will first use an input instruction to ask the amplifier for its current phase setting (an integer from 0 to 4).
# Each phase setting is used exactly once, but the Elves can't remember which amplifier needs which phase setting.

# The program will then call another input instruction to get the amplifier's input signal, compute the correct output signal, and supply it back to the amplifier with an output instruction. 

# each program calls input twice

# thrusters by trying every possible combination of phase settings on the amplifiers. Make sure that memory is not shared or reused between copies of the program.

# try every ombo of 0 - 4  collections.permutations range(0,4)

import itertools
combos = itertools.permutations(range(0,5))

class Amplifier:
    def __init__(self, program_file, name):
        ''' Initialize amplifier with a file containing the program
        '''
        self.name = name
        with open(program_file) as f:
            line = f.readline()
            self.cells =  [int(x) for x in line.split(",")]
        self.cells_initial = self.cells
        self.i = 0
    
    
    def reset_program(self):
        self.cells = self.cells_initial
        self.i = 0

    
    def run_program(self, input):
        print(f"Running program for {self.name} input {input}")
        outputs = list()
        cur_inst = self.cells[self.i]
        opcode = get_opcode(cur_inst)
        while(opcode != 99):
            print(f"running opcode {opcode}")
            if opcode < 3:
                a = read_param_number(cur_inst, 1, self.cells, self.i)
                b = read_param_number(cur_inst, 2, self.cells, self.i)

                # assume when writing that you always get the position
                writepos = self.cells[self.i+3]
                print(f"i = {self.i} instruction = {cur_inst} a = {a} b = {b} writepos = {writepos}")
                rslt = a + b if opcode == 1 else a * b
                self.cells[writepos] = rslt
                self.i = self.i + 4
            if opcode == 3:
                print(f"i = {self.i} inst = {cur_inst}")
                print(f"OPCODE 3 input {input} to index {self.cells[self.i+1]}")

                if (input is not None):
                    self.cells[self.cells[self.i+1]] = input
                    self.i = self.i + 2
                    input = None
                else:
                    print(f"returning early because waiting for input. Outputs collected: {outputs}")
                    return "continue", outputs
            if opcode == 4:
                a = read_param_number(cur_inst, 1, self.cells, self.i)
                print(f"OPCODE 4 i = {self.i} inst = {cur_inst} a = {a}")
                outputs.append(a)
                self.i = self.i + 2
            if opcode == 5:
                # Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
                a = read_param_number(cur_inst, 1, self.cells, self.i)
                b = read_param_number(cur_inst, 2, self.cells, self.i)
                print(f"OPCODE 5 i = {self.i} inst = {cur_inst} a = {a} b = {b}")
                if a != 0:
                    self.i = b
                else:
                    self.i = self.i + 3
            if opcode == 6:
                a = read_param_number(cur_inst, 1, self.cells, self.i)
                b = read_param_number(cur_inst, 2, self.cells, self.i)
                print(f"OPCODE 6 i = {self.i} inst = {cur_inst} a = {a} b = {b}")
                if a == 0:
                    self.i = b
                else:
                    self.i = self.i + 3
            if opcode == 7:
                # Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
                a = read_param_number(cur_inst, 1, self.cells, self.i)
                b = read_param_number(cur_inst, 2, self.cells, self.i)
                c = self.cells[self.i+3]
                print(f"OPCODE 7 i = {self.i} inst = {cur_inst} a = {a} b = {b} c = {c}")

                if a < b:
                    self.cells[c] = 1
                else:
                    self.cells[c] = 0
                self.i = self.i + 4
            if opcode == 8:
                # Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
                a = read_param_number(cur_inst, 1, self.cells, self.i)
                b = read_param_number(cur_inst, 2, self.cells, self.i)
                c = self.cells[self.i+3]
                print(f"OPCODE 8 i = {self.i} inst = {cur_inst} a = {a} b = {b} c = {c}")
                if a == b:
                    self.cells[c] = 1
                    print(f"write 1 to position {c}")
                else:
                    self.cells[c] = 0
                    print(f"write 0 to position {c}")
                self.i = self.i + 4
            cur_inst = self.cells[self.i]
            opcode = get_opcode(cur_inst)
        print(f"reached end, returning {outputs}")
        return "done", outputs
    
def read_param(mode, cells, param):
    ''' Utility function to read a param
    '''
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
    ''' Utility function to get opcode
    '''
    return cell % 100

def read_param_number(cell, param_number, cells, inst_pointer):
    ''' Utility function to read params
    '''
    cell = cell // 100
    ptmp = param_number
    while ptmp > 1:
        ptmp -= 1
        cell = cell // 10
    param_mode = cell % 10
    return read_param(param_mode, cells, cells[inst_pointer + param_number])

def do_guess(amplifier_settings, program_file):
    ''' Run through a guess and return output of each amplifier
    '''
    amps = [Amplifier(program_file, f"amp{i}") for i in range(5)]
    next_input = 0
    for i, amp in enumerate(amps):
        status, outputs = amp.run_program(amplifier_settings[i])
        assert(len(outputs) == 0)
        status, outputs = amp.run_program(next_input)
        assert(len(outputs) == 1)
        next_input = outputs[0]
    return next_input


def do_guess_2(amplifier_settings, program_file):
    amps = [Amplifier(program_file, f"amp{i}") for i in range(5)]
    # provide each amp a setting as its first input instruction
    for i, amp in enumerate(amps):
        status, outputs = amp.run_program(amplifier_settings[i])
        assert(len(outputs) == 0)
    
    next_input = 0
    while (True):
        for i, amp in enumerate(amps):
            status, outputs = amp.run_program(next_input)
            assert(len(outputs) == 1)
            next_input = outputs[0]
        if status == "done":
            return next_input
            
        



    

        

def main():
    # do_guess_2([9,7,8,5,6], "input7-test.txt")
    # program has two input instructions

    max_output = 0
    for guess in itertools.permutations(range(5,10)):
        out = do_guess_2(guess, "input7.txt")
        if (out > max_output):
            max_output = out
    print(max_output)


    # 5 amplifiers
    # for each guess
    # amp 1:
    # set amp setting
    # provide input 0, save output
    # for each amp in list:
    # set the guessed amp setting
    # if first, set zero. else set 

if __name__ == '__main__':
    main()
    

