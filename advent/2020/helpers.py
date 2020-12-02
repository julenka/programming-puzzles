import re

def get_int_values(filename):
    return list(int(x) for x in open(filename).readlines())

def get_lines(filename):
    return open(filename).readlines()

def parse_lines_regex(filename, regex_per_line):
    ''' For each line, parses the line using the given regex, returning groups.
    
    Example regex from problem 2: r"^(\d+)-(\d+) (\w): (\w+)$"
    '''
    lines = get_lines(filename)
    for line in lines:
        match = re.match(regex_per_line, line)
        if not match:
            print("match failed: " + line)
        else:
            yield match.groups()

