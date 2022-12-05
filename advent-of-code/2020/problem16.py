from helpers import get_lines
import math
import numpy as np

# for each column, maintain list of constraints that match that column

class Constraint:
    def __init__(self, line : str):
        name, all_constr = line.split(":")
        self.name = name
        self.constr = list()
        all_constr = all_constr.strip()
        constrs = all_constr.split(" or ")
        for c in constrs:
            a, b = (int(x) for x in c.split("-"))
            self.constr.append((a, b))
    
    def satisfies(self, fields:list):
        '''Return true if all fields satisfy this constraint'''
        for f in fields:
            if not self.satisfy(f):
                return False
        return True
    
    def satisfy(self, n:int):
        for cx in self.constr:
            if n >= cx[0] and n <= cx[1]:
                return True
        return False

    def __str__(self):
        return f"{self.name}: {str(self.constr)}"

def split_into_parts(data_lst : list):
    '''Split data list into the 3 part, separated by empty lines'''
    parts = [[],[],[]]
    cur_part = 0
    for line in data_lst:
        if len(line) == 0:
            cur_part += 1
            continue
        if line.startswith("your ticket"):
            continue
        if line.startswith("nearby tickets"):
            continue
        parts[cur_part].append(line)
    return parts

def read_constraints2(data: list):
    return [Constraint(line) for line in data]

def read_constraints(data: list):
    ''' return list of constraints, [(min, max),...]'''
    result = list()
    for line in data:
        cur_constr = list()
        _, all_constr = line.split(":")
        all_constr = all_constr.strip()
        constrs = all_constr.split(" or ")
        for c in constrs:
            a, b = (int(x) for x in c.split("-"))
            cur_constr.append((a, b))
        result.append(cur_constr)
    return result

def read_nearby(data : list):
    ''' Return list of ints per line'''
    result = []
    for line in data:
        result.append([int(x) for x in line.split(",")])
    return result

def read_nearby2(data : list, cxs : list):
    '''Return numpy array of fields'''
    initial = read_nearby(data)
    valid = list()
    for lst in initial:
        invalid = False
        for n in lst:
            if not const_sat2(cxs, n):
                invalid = True
                break
        if not invalid:
            valid.append(lst)
    return np.array(valid)

def const_sat(cxs, n):
    for cxl in cxs:
        for cx in cxl:
            if n >= cx[0] and n <= cx[1]:
                return True          
    return False

def const_sat2(cxs, n):
    for cx in cxs:
        if cx.satisfy(n):
            return True
    return False

def solve1(data : list):
    part1, part2, part3 = split_into_parts(data)    

    # part 1: read ticket constraints
    cxs = read_constraints(part1)     
    
    # part 2: read 'your ticket'

    # part 3: read 'nearby tickets'
    nby = read_nearby(part3)

    invalid_sum = 0
    for lst in nby:
        for n in lst:
            if not const_sat(cxs, n):
                invalid_sum += n
    print(f"part 1: {invalid_sum}")

def solve2(data):
    part1, part2, part3 = split_into_parts(data)    

    constraints = read_constraints2(part1)

    my_ticket = [int(x) for x in part2[0].split(",")]
    
    part3.insert(0, part2[0])
    nearby_tickets = read_nearby2(part3, constraints)
    print(str(nearby_tickets))

    num_fields = len(my_ticket)
    valid_constraints = list()

    for i in range(num_fields):
        field_values = nearby_tickets[:,i]
        valid = list()
        for cx in constraints:
            if cx.satisfies(field_values):
                valid.append(cx)
        valid_constraints.append(valid)
    
    
    # prune until only 1 left?
    did_prune = True
    while did_prune:
        did_prune = False
        for i, vs in enumerate(valid_constraints):
            if len(vs) == 1:
                for j in valid_constraints[:i] + valid_constraints[i+1:]:
                    to_remove = vs[0]
                    if to_remove in j:
                        did_prune = True
                        j.remove(to_remove)
    
    for i, vs in enumerate(valid_constraints):
        if len(vs) != 1:
            raise Exception(f"Incorrect number of valid constraints: {','.join(str(x) for x in vs)} {nearby_tickets[:,i]}")
        vs[0].field_index = i

    result = 1
    for vs in valid_constraints:
        cx = vs[0]
        print(f"{cx.name}: {cx.field_index} {my_ticket[cx.field_index]}")
        if cx.name.startswith("departure"):
            result *= my_ticket[cx.field_index]
        
    print(f"part 2: {result}")

test_data = '''
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
'''

data = list(test_data.strip().split("\n"))
data = get_lines("input-16.txt")

solve2(data)