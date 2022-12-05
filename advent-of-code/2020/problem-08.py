from helpers import get_lines

accumulator_value = 0

class Instruction:
    def __init__(self, line):
        instr, value = line.strip().split(" ")
        self.value = int(value)
        self.instruction  = instr
        self.order_visited = -1
    
    def has_been_visited(self):
        return self.order_visited >= 0

    def run(self, current_visit_order, line_idx):
        global accumulator_value
        if self.order_visited != -1:
            raise Exception(f"instruction {self.instruction} {self.value} already visited")
        self.order_visited = current_visit_order
        if self.instruction == "nop":
            return line_idx + 1
        elif self.instruction == "acc":
            accumulator_value += self.value
            return line_idx + 1
        elif self.instruction == "jmp":
            return line_idx + self.value
        raise Exception(f"invalid instruction {self.instruction}")

    def try_swap_nop_jmp(self):
        if self.instruction == "nop":
            self.instruction = "jmp"
        elif self.instruction == "jmp":
            self.instruction = "nop"
        else:
            return False
        return True

    def reset(self):
        self.order_visited = -1

def solve():
    global accumulator_value
    accumulator_value = 0
    run_program([Instruction(line) for line in get_lines("input-08.txt")])

    print(f"part 1: {accumulator_value}")

def run_program(instructions):
    ''' Returns whether program infinite loops'''
    current_instruction = instructions[0]
    current_visit_order = 1
    line_idx = 0
    while not current_instruction.has_been_visited():
        line_idx = current_instruction.run(current_visit_order, line_idx)
        if line_idx >= len(instructions):
            return False
        current_visit_order += 1
        current_instruction = instructions[line_idx]
    return True

def solve2():
    instructions = [Instruction(line) for line in get_lines("input-08.txt")]
    global accumulator_value
    test_idx = 0
    while test_idx < len(instructions):
        accumulator_value = 0
        for instruction in instructions:
            instruction.reset()
        
        if instructions[test_idx].try_swap_nop_jmp():
            if not run_program(instructions):
                print(f"part 2: {accumulator_value}")
                return
            else:
                instructions[test_idx].try_swap_nop_jmp()
        
        test_idx += 1
    
    print(f"none found")
    
solve()