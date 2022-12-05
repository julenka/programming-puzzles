from helpers import get_lines
from functools import reduce
class Group:
    def __init__(self):
        self.answer_set = set()
        self.answer_set_all = None

    def add_line(self, line):
        new_set = set(line)
        self.answer_set = self.answer_set | new_set
        if self.answer_set_all is None:
            self.answer_set_all = new_set
        else:
            self.answer_set_all = self.answer_set_all & new_set
        
    
    def get_num_answer_yes(self):
        return len(self.answer_set)
    
    def get_num_all_yes(self):
        return len(self.answer_set_all)

def solve():
    groups = []
    cur_group = Group()
    for line in get_lines('input-06.txt'):
        line = line.strip()
        if(len(line) == 0):
            groups.append(cur_group)
            cur_group = Group()
        else:
            cur_group.add_line(line)
    sum_groups_any = reduce(lambda acc, grp: acc + grp.get_num_answer_yes(), groups, 0)
    sum_groups_all = reduce(lambda acc, grp: acc + grp.get_num_all_yes(), groups, 0)
    print(f"part 1: {sum_groups_any}")
    print(f"part 2: {sum_groups_all}")
solve()