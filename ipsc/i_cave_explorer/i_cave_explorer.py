
from heapq import heappush, heappop, heapify
from collections import defaultdict

__author__ = 'julenka'

# in_f = open('i0.in')
# in_f = open('i1.in')
out_f = open('i2.out', 'w')
in_f = open('i2.in')

n_cases = int(in_f.readline())
import sys
sys.setrecursionlimit(100000)


def encode(symb2freq):
    """Huffman encode the given dict mapping symbols to weights"""
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))



class Node:
    def __init__(self, idx):
        self.idx = idx
        self.children = []
        self.n_descendants = 0
        self.mark = ""

    def __str__(self):
        return str(self.idx)

    def printMe(self):
        print self.idx, self.n_descendants, self.mark, [str(x) for x in self.children]
        for child in self.children:
            child.printMe()

    def addChild(self, child):
        self.children.append(child)

    def countDescendants(self):
        if len(self.children) == 0:
            self.n_descendants = 0
            return 0
        for child in self.children:
            self.n_descendants += child.countDescendants()
        self.n_descendants += len(self.children)
        return self.n_descendants

    def markLength(self):
        result = len(self.mark)
        for child in self.children:
            result += child.markLength()
        return result

    def computeMark(self):
        symb2freq = defaultdict(int)
        if(len(self.children)== 0):
            return
        for i, child in enumerate(self.children):
            symb2freq[str(i)] = child.n_descendants + 1
        huff = encode(symb2freq)
        for p in huff:
            k = p[0]
            v = p[1]
            child = self.children[int(k)]
            # print child.idx, "=>", self.mark + v
            self.children[int(k)].mark = self.mark + v
        for child in self.children:
            child.computeMark()


def addNode(nodes, idx, parent_idx):
    new_node = Node(idx)
    nodes.append(new_node)
    nodes[parent_idx].addChild(new_node)

def solve_case(node_info):
    root = Node(0)
    nodes = [root]
    for idx, n in enumerate(node_info):
        addNode(nodes, idx + 1, n - 1)
    root.countDescendants()
    root.computeMark()
    # root.printMe()
    markLength = root.markLength()
    print markLength
    print >> out_f, markLength


for case in xrange(n_cases):
    in_f.readline()
    n_nodes = int(in_f.readline())
    node_info = [int(x) for x in in_f.readline().split(' ')]
    solve_case(node_info)



