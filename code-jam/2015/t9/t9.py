__author__ = 'julenka'

import re

letter = 'C'
# size = 'small'
size = 'large'
input = '%s-%s-practice.in' % (letter,size)
output = input.replace('.in', '.out')
lines = [line.replace('\n','') for line in open(input).readlines()]
outf = open(output, 'w')
num_cases = int(lines[0])

num_map = {
    2: 'abc',
    4: 'ghi',
    5: 'jkl',
    3: 'def',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}
char_map = {' ' : 0}
for num, letters in num_map.iteritems():
    for i,letter in enumerate(letters):
        char_map[letter] = str(num) * (i + 1)

def solve_case(line):
    last_char = ''
    result = ""
    for letter in line:
        if letter == ' ':
            new_char = '0'
            if(new_char[0] == last_char):
                result += ' '
            result += new_char

            last_char = new_char
        else:
            new_char = char_map[letter]
            if(new_char[0] == last_char):
                result += ' '
            result += new_char
            last_char = new_char[0]
    return result


for i in range(num_cases):
    print >> outf, "Case #%d: %s" % (i + 1, solve_case(lines[i + 1]))

