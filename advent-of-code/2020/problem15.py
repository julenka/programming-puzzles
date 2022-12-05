from helpers import get_lines
import math

def search_backward(v, lst, start_i):
    '''Return first index that v appears in lst, backward'''
    for i, v2 in enumerate(reversed(lst)):
        if i < start_i:
            continue
        if v2 == v:
            return len(lst) - i - 1
    return -1

def solve2(data, stop_idx):
    last_seen = dict()
    for i, d in enumerate(data[:-1]):
        last_seen[d] = i
    
    cur_idx = len(data)
    last_val = data[-1]
    while(cur_idx <= stop_idx - 1):
        prev_idx = cur_idx - 1
        if last_val not in last_seen:
            next_val = 0
            last_seen[last_val] = prev_idx
        else:
            next_val = prev_idx  -  last_seen[next_val]
            last_seen[last_val] = prev_idx

        last_val = next_val        
        cur_idx += 1
        if cur_idx % 1e6 == 0:
            print(str(cur_idx))
    print("part 2: " + str(last_val))
    

def solve1(data, stop_idx):
    while(len(data) < stop_idx):
        last_val = data[-1]
        prev_idx = search_backward(last_val, data, 1)
        if prev_idx == -1:
            data.append(0)
        else:
            data.append(len(data) - 1 - prev_idx)
    print("part 1: " + str(data[-1]))
    # print(str(data))

test_data = [6,3,15,13,1,0]
solve2(test_data, 30000000)