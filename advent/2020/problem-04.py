from helpers import get_lines
import re

def validate_p1(field, val):
    return True

def validate_p2(field, val):
    if field in ["byr", "iyr", "eyr"]:
        match = re.match(r"^\d{4}$", val)
        if match is None:
            return False
        n = int(val)
        min_val = 1920
        max_val = 2002
        if field == "iyr":
            min_val = 2010
            max_val = 2020
        elif field == "eyr":
            min_val = 2020
            max_val = 2030
        return n >= min_val and n <= max_val
    if field == "hgt":
        match = re.match(r"^(\d+)(cm|in)$", val)
        if match is None:
            return False
        n = int(match.group(1))
        unit = match.group(2)
        min_val = 150
        max_val = 193
        if unit == "in":
            min_val = 59
            max_val = 76
        return n >= min_val and n <= max_val
    if field == "hcl":
        match = re.match(r"^#[0-9a-f]{6}$", val)
        return match is not None
    if field == "ecl":
        match = re.match(r"^(amb|blu|brn|gry|grn|hzl|oth)$", val)
        return match is not None
    if field == "pid":
        match = re.match(r"^\d{9}$", val)
        return match is not None
    return True

def solve(validation_function, answer_prefix):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    lines = get_lines("input-04.txt")
    
    required_copy = list(required_fields)
    valid_count = 0
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            if len(required_copy) == 0:
                valid_count += 1
            required_copy = list(required_fields)
        else:
            for match in re.finditer(r"(\w+):([#\w]+)", line):
                field = match.group(1)
                val = match.group(2)
                if validation_function(field, val) and field in required_copy:
                    required_copy.remove(field)
 
    print(f"{answer_prefix}: {valid_count}")

solve(validate_p1, "part1")
solve(validate_p2, "part2")