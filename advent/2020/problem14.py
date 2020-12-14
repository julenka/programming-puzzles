from helpers import get_lines
import math
import re
import itertools

def apply_mask(mask, bit_values):
    '''returns mask applied to bit values'''
    mask = list(mask)
    bit_values = list(bit_values)
    for i in range(len(mask)):
        if mask[i] == "0":
            bit_values[i] = "0"
        if mask[i] == "1":
            bit_values[i] = "1"
    return "".join(bit_values)

def apply_mask_p2(mask, bit_values):
    '''
    If the bitmask bit is 0, the corresponding memory address bit is unchanged.
    If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
    If the bitmask bit is X, the corresponding memory address bit is floating. (X)
    '''
    mask = list(mask)
    bit_values = list(bit_values)
    for i in range(len(mask)):
        if mask[i] == "0":
            pass
        elif mask[i] == "1":
            bit_values[i] = "1"
        else:
            bit_values[i] = "X"
    return "".join(bit_values)

def bits_to_floating(bit_values):
    ''' Returns list of floating addresses accounting for floating mem values'''
    count_X = bit_values.count("X")
    floating_addresses = itertools.product("01", repeat = count_X)
    result = list()
    for a in floating_addresses:
        new_str = ""
        for c in bit_values:
            if c == "X":
                new_str += a[0]
                a = a[1:]
            else:
                new_str += c
        result.append(new_str)
    return result


def uint_to_bits(input):
    '''Converts an int to a 36 bit unsigned bit string'''
    result = ["0"] * 36
    idx = len(result) - 1
    while(input > 0):
        result[idx] = str(input % 2)
        input = input >> 1
        idx -= 1
    return "".join(result)

def bits_to_uint(bits):
    '''Converts ad 36 bit unsigned bit string to a uint, returns value'''
    result = 0
    for i in range(36):
        if bits[35 - i] == "1":
            result += 1 << i
    return result

def solve1(data):
    mem_values = dict()
    for line in data:
        try:
            cmd, val = line.split(" = ")
        except Exception as e:
            print("Exception at " + line)
            raise e
        if cmd == "mask":
            cur_mask = val
        else:
            val = int(val)
            m = re.match(r"^mem\[(\d+)]$", cmd)
            if m is None:
                raise Exception("invalid input " + cmd)
            else:
                mem_idx = int(m.group(1))
                mem_values[mem_idx] = apply_mask(cur_mask, uint_to_bits(val))
    mem_value_ints = [bits_to_uint(x) for x in mem_values.values()]
    print("part 1: " + str(sum(mem_value_ints)))

def solve2(data):
    mem_values = dict()
    for line in data:
        try:
            cmd, val = line.split(" = ")
        except Exception as e:
            print("Exception at " + line)
            raise e
        if cmd == "mask":
            cur_mask = val
        else:
            val = int(val)
            m = re.match(r"^mem\[(\d+)]$", cmd)
            if m is None:
                raise Exception("invalid input " + cmd)
            else:
                mem_idx = int(m.group(1))
                mem_idx_bits = uint_to_bits(mem_idx)
                mem_idx_bits_masked = apply_mask_p2(cur_mask, mem_idx_bits)
                all_mem_values = bits_to_floating(mem_idx_bits_masked)
                for v in all_mem_values:
                    idx = bits_to_uint(v)
                    mem_values[idx] = val

    print("part 2: " + str(sum(mem_values.values())))

test_data = '''
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
'''

data = test_data.strip().split("\n")
data = get_lines("input-14.txt")

solve2(data)