

# light red bags contain 1 bright white bag, 2 muted yellow bags.
from helpers import get_lines
import re
from collections import defaultdict

def build_map(lines):
    result = defaultdict(list)
    for line in lines:
        containing_bag, bags_inside = line.split(" bags contain ")
        bags_inside = bags_inside.replace(".", "").strip()
        if bags_inside == "no other bags":
            continue
        bags_inside = bags_inside.split(", ")
        for bag in bags_inside:
            m = re.match(r"\d+ ([\w\s]+) (bag|bags)", bag.strip())
            if m is None:
                raise Exception("Invalid input " + bag.strip())
            color = m.group(1)
            result[color].append(containing_bag)   
    return result

def solve():
    # map from color -> list (colors that contain this color immediately)
    # list = bags that can contains shiny gold bag
    # list of candidates to explore
    # list to explore = map [ shiny gold ]
    # for each candidate in to explore:
    #   pus it onto answer list
    #   for each candidate that can contain this color, push that onto to explore

    bag_map = build_map(get_lines("input-07.txt"))

    containing_gold = set()
    to_explore = ["shiny gold"]
    while len(to_explore) > 0:
        cur = to_explore.pop()
        if cur != "shiny gold":
            containing_gold.add(cur)
        contains_cur = bag_map[cur]
        for container in contains_cur:
            if container not in containing_gold:
                to_explore.append(container)
                containing_gold.add(container)
    print(f"part 1: {len(containing_gold)}")

bag_map_2 = defaultdict(list)

def build_map_2(lines):
    global bag_map_2
    for line in lines:
        containing_bag, bags_inside = line.split(" bags contain ")
        bags_inside = bags_inside.replace(".", "").strip()
        if bags_inside == "no other bags":
            bag_map_2[containing_bag] = []
        else:
            bags_inside = bags_inside.split(", ")
            for bag in bags_inside:
                m = re.match(r"(\d+) ([\w\s]+) (bag|bags)", bag.strip())
                if m is None:
                    raise Exception("Invalid input " + bag.strip())
                count = int(m.group(1))
                color = m.group(2)
                bag_map_2[containing_bag].append((count, color))
    pass

def helper(color):
    global bag_map_2
    must_contain = bag_map_2[color]
    if len(must_contain) == 0:
        return 0
    result = 0
    for count, color in must_contain:
        result += count
        result += count * helper(color)
    return result

def solve2():
    # global map from color_str -> list((count, str)) tracking bag rules
    # if no other bags, make sure color_str is in list of empty children
    # total helper("shiny gold")
    # helper(color): returns number of bags that it must contain
    # base case: if map[color] has 0 bags, return 0
    # for each child in the map:
    # result = child_count + child_count * helper(child_color)
    # return result
    global bag_map_2
    build_map_2(get_lines("input-07.txt"))
    shiny_gold_must_contain = helper("shiny gold")
    print(f"part 2: {shiny_gold_must_contain}")

solve2()
