from helpers import get_lines, get_int_values

def solve1(lines):
    input = sorted(lines)
    print(str(input))
    num_1 = 0
    num_3 = 0
    cur = 0
    for i in range(len(input)):
        next = input[i]
        if (next - cur) == 1:
            num_1 += 1
        if (next - cur) == 3:
            num_3 += 1
        cur = next
    num_3 += 1
    print(f"part1: {num_1} * {num_3} = {num_1 * num_3}")
    pass

saved_results = dict()

def helper(lines, start_i, pfx):
    print(f"{pfx}helper {start_i}")
    global saved_results
    if start_i in saved_results:
        return saved_results[start_i]
    if start_i >= len(lines) - 1:
        saved_results[start_i] = 0
        print("{pfx}ret 0")
        return 0
    if start_i == len(lines) - 2:
        saved_results[start_i] = 1
        print("{pfx}ret 1")
        return 1
    cur_val = lines[start_i]
    result = 0
    for i in range(1, 4):
        if lines[start_i + i] <= cur_val + 3 and start_i < len(lines):
            result += helper(lines, start_i + i, pfx + "  ")
        else:
            break
    saved_results[start_i] = result
    print(f"{pfx}return {result}")
    return result

def solve2(lines):
    input = sorted(lines)
    input.insert(0, 0)
    input.append(input[-1] + 3)
    num_ways = helper(input, 0,"")
    print(f"part 2: {num_ways}")


solve2(get_int_values("input-10.txt"))