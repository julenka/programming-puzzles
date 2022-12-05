from helpers import get_lines
import math

all_rules = {}

def solve1(data):
    global all_rules
    part, result = 0, 0

    for line in data:
        if len(line) == 0:
            part += 1
            continue

        if part == 0:
            rule_num, rule_text = (x.strip() for x in line.split(":"))
            rule_num = int(rule_num)

            new_rule = None
            if "|" in rule_text:
                new_rule = Pipe(rule_text)
            elif "\"" in rule_text:
                new_rule = Character(rule_text)
            else:
                new_rule = Sequence(rule_text)
            all_rules[rule_num] = new_rule
    
        if part == 1:
            if all_rules[0].matches(line):
                print(f"{line} matches")
                result += 1
            else:
                print(f"{line} does not match")
    print(f"part 1: {result}")
    for k,v in all_rules.items():
        print(f"{k}: {v}")

def solve2(data):
    pass

class Sequence:
    def __init__(self, input):
        self.subrules = [int(x) for x in input.strip().split()]

    def matches(self, input):
        global all_rules
        return self.matches_helper(input, self.subrules)
    
    def matches_helper(self, input, rules):
        global all_rules
        if len(input) == 0:
            return len(rules) == 0
        if len(rules) == 0:
            return len(input) == 0
        
        for rule_num in rules:
            rule = all_rules[rule_num]
            if isinstance(rule, Character):
                head,*tail = list(input)
                return rule.matches(head) and self.matches_helper(tail, rules[1:])
            else:
                for i in range(1,len(input)):
                    head, *tail = input[:i]
                    if rule.matches(head) and self.matches_helper(tail, rules[1:]):
                        return True
        return False
    
    def __str__(self):
        return "->".join(str(rule) for rule in self.subrules)

class Pipe:
    def __init__(self, input):
        self.subrules = [Sequence(x) for x in input.strip().split("|")]

    def matches(self, input):
        global all_rules
        return any(subrule.matches(input) for subrule in self.subrules)

    def __str__(self):
        return "|".join(str(rule) for rule in self.subrules)

class Character:
    def __init__(self, input):
        self.character = input.strip().replace("\"","")
    
    def matches(self, input):
        print(f"matches {input} {self} gives {input.strip() == self.character}")
        return input.strip() == self.character
    
    def __str__(self):
        return "'" + self.character + "'"

test_data = '''
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
'''

data = test_data.strip().split("\n")
# data = get_lines("input-12.txt")

solve1(data)