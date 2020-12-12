from helpers import get_lines
import math
test_data = '''
F10
N3
F7
R90
F11
'''

class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.facing = "E"
        self.way_x = 10
        self.way_y = 1

    def print_coords(self):
        print(f"({self.x}, {self.y}) wp({self.way_x}, {self.way_y})")

    def manhattan(self):
        return abs(self.x) + abs(self.y)
    
    def applyrot(self, dir, amt):
        directions = "NESW"
        cur_dir = directions.index(self.facing)
        if dir == "L":
            amt = -amt
        new_dir = (cur_dir + int(amt / 90)) % 4
        self.facing = directions[new_dir]
    
    def wp_applyrot(self, dir, amt):
        rad = math.radians(amt)
        if dir == "R":
            rad = -rad
        old_x = self.way_x
        old_y = self.way_y
        self.way_x = int(round(old_x * math.cos(rad) - old_y * math.sin(rad)))
        self.way_y = int(round(old_x * math.sin(rad) + old_y * math.cos(rad)))

    def applycardinal(self, crdnal, amt):
        dx, dy = self.cardinal_to_delta(crdnal)
        self.x += dx * amt
        self.y += dy * amt
    
    def wp_applycardinal(self, cardinal, amt):
        dx, dy = self.cardinal_to_delta(cardinal)
        self.way_x += dx * amt
        self.way_y += dy * amt
    
    def applyforward(self, amt):
        dx, dy = self.cardinal_to_delta(self.facing)
        self.x += dx * amt
        self.y += dy * amt

    def wp_applyforward(self, amt):
        self.x += self.way_x * amt
        self.y += self.way_y * amt
    
    def cardinal_to_delta(self, crdnal):
        if crdnal == "E":
            return (1, 0)
        elif crdnal == "W":
            return (-1, 0)
        elif crdnal == "N":
            return (0, 1)
        elif crdnal == "S":
            return (0, -1)
        else:
            raise Exception(f"Invalid cardinal {crdnal}")




def solve1():
    data = test_data.strip().split("\n")
    data = get_lines("input-12.txt")
    ship = Ship()
    for line in data:
        command = line[0]
        amt = int(line[1:])
        print(f"{command} {amt}")
        if command == "L":
            ship.applyrot(command, amt)
        elif command == "R":
            ship.applyrot(command, amt)
        elif command == "F":
            ship.applyforward(amt)
        else:
            ship.applycardinal(command, amt)
    print(f"part 1: {ship.manhattan()}")

def solve2():
    data = test_data.strip().split("\n")
    data = get_lines("input-12.txt")
    ship = Ship()

    for line in data:
        command = line[0]
        amt = int(line[1:])
        if command == "L":
            ship.wp_applyrot(command, amt)
        elif command == "R":
            ship.wp_applyrot(command, amt)
        elif command == "F":
            ship.wp_applyforward(amt)
        else:
            ship.wp_applycardinal(command, amt)
    print(f"part 2: {ship.manhattan()}")



solve2()