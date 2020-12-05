from helpers import get_lines
class SeatData:
    def __init__(self, line):
        line = line.strip()
        self.row_str = line[:7]
        self.col_str = line[7:]
        self.row = self.binary_partition(self.row_str, 0, 127, "B", "F")
        self.col = self.binary_partition(self.col_str, 0, 7, "R", "L")
        self.seat_id = 8 * self.row + self.col
    
    def binary_partition(self, code_str, min_val, max_val, upper_code, lower_code):
        row_min = min_val
        row_max = max_val
        for c in code_str[:-1]:
            if c == lower_code: # lower half
                row_max = int((row_min + row_max) / 2)
            elif c == upper_code: # upper half
                row_min = int((row_min + row_max) / 2) + 1
            else:
                raise Exception("invalid input character " + c)
        if code_str[-1] == upper_code:
            return row_max
        elif code_str[-1] == lower_code:
            return row_min
        else:
            raise Exception("invalid input character at end " + code_str[-1])
    

    

def solve():
    # read data
    seat_data = [SeatData(line) for line in get_lines("input-05.txt")]

    # solve
    max_seat_id = 0
    for d in seat_data:
        max_seat_id = max(d.seat_id, max_seat_id)
    print(f"part 1: {max_seat_id}")

    seat_ids_sorted = sorted(x.seat_id for x in seat_data)
    for i in range(len(seat_ids_sorted) - 1):
        if seat_ids_sorted[i + 1] - seat_ids_sorted[i] > 1:
            print(f"part 2: {seat_ids_sorted[i + 1]} {seat_ids_sorted[i]}")
            break
solve()