from helpers import get_lines
import math

from typing import NamedTuple
import re



def main():
    test_data = '''
    1 + 2 * 3 + 4 * 5 + 6
    ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
'''

    data = test_data.strip().split("\n")
    data = get_lines("input-18.txt")
    solve2(data)


class Token(NamedTuple):
    type: str
    value: str

class Node:
    left = None
    right = None

    def __init__(self):
        self.left = None
        self.right = None

    def evaluate(self):
        return None

class SumNode(Node):
    def __init__(self, leftNode, rightNode):
        self.left = leftNode
        self.right = rightNode
    
    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()

class ProductNode(Node):
    def __init__(self, leftNode, rightNode):
        self.left = leftNode
        self.right = rightNode
    
    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()

class IntNode(Node):
    def __init__(self, valuestr):
        self.intvalue = int(valuestr)
    
    def evaluate(self):
        return self.intvalue


def tokenize(expression):
    token_specification = [
    ('NUMBER',   r'\d+(\.\d*)?'),  # Integer or decimal number
    ('OP',       r'[+\-*/]'),      # Arithmetic operators
    ('PAREN',    r'[()]')
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    for mo in re.finditer(tok_regex, expression):
        kind = mo.lastgroup
        value = mo.group()
        yield Token(kind, value)

def check_paren(tokens):
    if tokens[0].type != "PAREN" or tokens[-1].type != "PAREN":
        return False
    paren_count = 1
    for t in tokens[1:-1]:
        if paren_count == 0:
            return False
        if t.value == "(":
            paren_count += 1
        if t.value == ")":
            paren_count -= 1
    return True

def check_multiply(tokens):
    return check_helper(tokens, "*")

def check_sum(tokens):
    return check_helper(tokens, "+")

def check_helper(tokens, needle):
    paren_count = 0
    for i,t in enumerate(tokens):
        if t.value == "(":
            paren_count += 1
        if t.value == ")":
            paren_count -= 1
        if t.value == needle and paren_count == 0:
            return i
    return -1

def build_tree(tokens):
    while check_paren(tokens):
        tokens = tokens[1:-1]
    
    multiply_idx = check_multiply(tokens)
    if multiply_idx > 0:
        # print(f"mult idx: {multiply_idx}")
        return ProductNode(build_tree(tokens[:multiply_idx]), build_tree(tokens[multiply_idx + 1:]))
    elif multiply_idx == 0:
        raise Exception("multiply idx should not be 0")
    else:
        sum_idx = check_sum(tokens)
        if sum_idx > 0:
            # print(f"sum idx: {sum_idx}")
            return SumNode(build_tree(tokens[:sum_idx]), build_tree(tokens[sum_idx + 1:]))
        elif sum_idx == 0:
            raise Exception("sum idx should not be 0")
        else:
            if len(tokens) > 1:
                raise Exception("hit number case but more than one token")
            else:
                return IntNode(tokens[0].value)

def solve2(data):
    result = 0
    for line in data:
        line = line.strip()
        print(line)
        tokens = list(tokenize(line))
        v = build_tree(tokens).evaluate()
        print(str(v))
        result += v

    print(f"part2: {result}")


token_index = 0
tokens = None

def evaluate_tokens(pfx=""):
    global tokens, token_index

    result = 0
    cur_operand = None
    while token_index < len(tokens):
        token = tokens[token_index]
        token_index += 1
        if token.type == "NUMBER":
            val = int(token.value)
            if cur_operand is None:
                result = val
            elif cur_operand == '+':
                result += val
            elif cur_operand == '*':
                result *= val
            else:
                raise Exception("invalid operand " + cur_operand)
        elif token.type == "OP":
            cur_operand = token.value
        elif token.type == "PAREN":
            if token.value == ")":
                return result
            if token.value == "(":
                val = evaluate_tokens(pfx + "  ")
                if cur_operand is None:
                    result = val
                elif cur_operand == '+':
                    result += val
                elif cur_operand == '*':
                    result *= val
                else:
                    raise Exception("invalid operand " + cur_operand)
        print(f"{token_index}: {token.value} {result}")
    return result

def evaluate_expression(expression):
    global token_index, tokens
    token_index = 0
    tokens = list(tokenize(expression))
    return evaluate_tokens()

def solve1(data):
    result = 0
    for line in data:
        s = evaluate_expression(line)
        print(s)
        result += s
    print(f"part 1: {result}")
    
if __name__ == "__main__":
    main()
