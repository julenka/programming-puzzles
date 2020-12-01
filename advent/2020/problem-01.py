import itertools
from functools import reduce
from helpers import get_int_values

def helper(int_values, comb_len, required_sum=2020):
    for candidates in itertools.combinations(int_values, comb_len):
        sum = reduce(lambda x, y: x + y, candidates, 0)
        if (sum == required_sum):
            product = reduce(lambda x, y: x * y, candidates, 1)
            print(" * ".join([str(x) for x in candidates]) + " = " + str(product))
            return True
    return False


def solve():
    input = get_int_values("input-01.txt")
    print("part 1")
    helper(input, 2)
    print("part 2")
    helper(input, 3)

solve()