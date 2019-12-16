def main():    
    infile = "input6.txt"
    # infile = "input6-test.txt"
    f = open(infile)
    # str => node
    node_map = dict()
    you_orbiting = None
    santa_orbiting = None 

    for line in f:
        p1,p2 = (x.strip() for x in line.split(")"))
        n1 = node_map[p1] if p1 in node_map else Node(p1)
        n2 = node_map[p2] if p2 in node_map else Node(p2)
        n1.add_child(n2)
        if p1 not in node_map:
            node_map[p1] = n1
        if p2 not in node_map:
            node_map[p2] = n2
        
        if p2 == "YOU":
            you_orbiting = n1
        if p2 == "SAN":
            santa_orbiting = n1
    node_map["COM"].compute_depth_recursive(0)

    for v in node_map.items():
        print(str(v))
    print("num_orbits: {}".format(node_map["COM"].compute_depth_sum()))

    # perform bfs
    # when we remove an item: 
    # for each child, if the child has not been searched, set its distance and add to list
    you_orbiting.parent.search_dist = 1
    to_search = [you_orbiting.parent]
    while to_search:
        cur = to_search.pop(0)
        if cur == santa_orbiting:
            cur.path = cur.path + "=>" + cur.value
            print("santa dst: {} path: {}".format(cur.search_dist, cur.path))
            break
        candidates = [cur.parent] + cur.children
        for c in candidates:
            if c and c.search_dist == -1:
                c.search_dist = cur.search_dist + 1
                c.path = cur.path + "=>" + cur.value
                to_search.append(c)
        

# count number of orbits
# orbit system can be thought of as tree
# A)B means A orbits B, or B is child of A
# if we want to know total indirect and direct orbits, we just want
# to know the sum of depths of each node in the tree

# so first we build the tree
# then count the depth of each node, and take the sum

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None
        self.depth = 0
        self.depth_sum = -1
        self.searches = False
        self.search_dist = -1
        self.path = ""
        
    def __repr__(self):
        return "%s children: %d depth:%d " % (self.value, len(self.children), self.depth)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def compute_depth_recursive(self, start_depth):
        self.depth = start_depth
        for c in self.children:
            c.compute_depth_recursive(start_depth + 1)
    
    def compute_depth_sum(self):
        if self.depth_sum >= 0:
            return self.depth_sum

        children_result = sum((x.compute_depth_sum() for x in self.children))
        self.depth_sum = self.depth + children_result
        return self.depth_sum

if __name__ == '__main__':
    main()

