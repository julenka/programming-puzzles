# 152085-670283
start = 152085
end = 670283

# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

count=0
for i in range(start,end):
    # at least two adjacent digits are the same
    cur = i
    prev_digit = i % 10
    adjacent = False
    adjacent_count = 1
    contains_adjacent_2 = False
    decreasing = False
    while cur > 0:
        cur = cur // 10
        cur_digit = cur % 10
        if (cur_digit == prev_digit):
            adjacent_count += 1
            adjacent = True
        else:
            if (adjacent_count == 2):
                contains_adjacent_2 = True
            adjacent_count = 1
        if (cur_digit > prev_digit):
            decreasing = True
            break
        
        prev_digit = cur_digit

    if (adjacent_count == 2):
        contains_adjacent_2 = True

    # if adjacent and not decreasing:
    if contains_adjacent_2 and not decreasing:
        print(i)
        count += 1

print(count)

