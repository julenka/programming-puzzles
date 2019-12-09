# problem3.py
# approach
# record the coordinates of every cell in line 1
# For each cell that intersects line 2,
# get manhattan distance, if it is the closest, save that



def main():
    # infile = "input3_test.txt"
    infile = "input3.txt"
    f = open(infile)
    l1 = f.readline()
    tokens = l1.split(",")
    l1_coords = set()
    l1_distances = dict()
    for x,y,i in walk_line(tokens):
        l1_coords.add((x,y))
        l1_distances[(x,y)] = i

    result = 1000000000
    l2 = f.readline()
    tokens2 = l2.split(",")
    for x,y,i in walk_line(tokens2):
        if (x,y) in l1_coords:
            dst = i + l1_distances[(x,y)]
            print(f"{x}, {y} dst {dst}")
            if dst < result:
                result = dst
    print(result)
            

def walk_line(tokens):
    cur_x = 0
    cur_y = 0
    steps = 0
    for t in tokens:
        dr = t[0]
        dist = int(t[1:])
        delta_x = 0
        delta_y = 0
        if dr == "L":
            delta_x = -1
        elif dr == "R":
            delta_x = 1
        elif dr == "U":
            delta_y = 1
        elif dr == "D":
            delta_y = -1
        else:
            print("invalid input " + dr)
            exit(1)

        for i in range(dist):
            steps += 1
            cur_x += delta_x
            cur_y += delta_y
            yield (cur_x, cur_y, steps)

if __name__ == "__main__":
    main()
