from helpers import get_lines
import math
import numpy as np
import scipy.ndimage

def do_cycle_3D(cur_state):
    return do_cycle_ND(cur_state, 4)


def do_cycle_4D(cur_state):
    return do_cycle_ND(cur_state, 4)

def do_cycle_ND(cur_state, nd):
    '''Does cycle, returning new state
       If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
       If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
    '''
    kernel = np.ones([3] * nd)
    kernel[tuple([1] * nd)] = 0 # count all but current value
    adjacent_counts = scipy.ndimage.convolve(cur_state, kernel, mode='constant', cval=0)

    result = np.zeros(cur_state.shape)

    for idx, j in np.ndenumerate(cur_state):
        if j == 1:
            if adjacent_counts[idx] == 2 or adjacent_counts[idx] == 3:
                result[idx] = 1
            else:
                result[idx] = 0
        else:
            if adjacent_counts[idx] == 3:
                result[idx] = 1
    return result


def solve(data, n_dims, n_cycles):
    start_array = []
    for line in data:
        start_array.append([ 0 if c == "." else 1 for c in line])
    start_np = np.array(start_array)
    start_dim = start_np.shape
    print(f"{str(start_array)} \nstart np: {str(start_np)}, {str(start_dim)})")

    w,h = start_dim
    cur_state_shape = [n_cycles * 2 + w, n_cycles * 2 + h] + [n_cycles * 2 + 1] * (n_dims - 2)
    cur_state = np.zeros(cur_state_shape)
    i = [slice(n_cycles,n_cycles + w), slice(n_cycles,n_cycles+h)] + [n_cycles] * (n_dims - 2)
    cur_state[tuple(i)] = start_np

    print(f"start: {cur_state.sum()}")

    for i in range(n_cycles):
        cur_state = do_cycle_3D(cur_state)
        print(f"cycle {i}: {cur_state.sum()}")


def solve1(data):
    solve(data, 3, 6)

def solve2(data):
    solve(data, 4, 6)

test_data = '''
.#.
..#
###
'''

data = test_data.strip().split("\n")
# data = get_lines("input-17.txt")
solve2(data)