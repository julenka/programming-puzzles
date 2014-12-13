#!/usr/bin/env python
''' Solves the MIU puzzle presented in GEB book

given: 
- r1: *I -> *IU
- r2: Mx -> Mxx
- r3: III -> U
- r4: UU -> 
- string MI

find: 
- derive MU
'''
from collections import defaultdict
import sys
from heapq import *

class Node:
	def __init__(self, value):
		self.children = []
		self.value = value

	def apply_r1(self):
		v = self.value
		if v[-1] == 'I':
			return [Node(self.value + "U")]
		return []

	def apply_r2(self):
		v = self.value
		if v[0] == 'M':
			return [Node(v + v[1:])]
		return []

	def apply_r3(self):
		v = self.value
		result = []
		for i in xrange(len(v) - 2):
			if(v[i:i+3] == "III"):
				result.append(Node(v[:i] + "U" + v[i+3:]))
		return result

	def apply_r4(self) :
		v = self.value
		result = []
		for i in xrange(len(v) - 1):
			if(v[i:i+2] == "UU"):
				result.append(Node(v[:i] + v[i+2:]))
		return result

	def __hash__(self):
		return hash(self.value)
	def __eq__(self, other):
		return other.value == self.value

	def __repr__(self):
		return "Node({})".format(self.value)

# BFS, for every string, check each rule and add child
start = Node("MI")
to_visit = [(2,start)]
# node -> derivation [(node, rule), (node, rule), node]
derivations = {start: [start]}
maxdepth = 0
lengthmap = defaultdict(list)

def extend_to_visit(rule, to_add):
	global maxdepth
	for candidate in to_add:
		if len(candidate.value) > int(sys.argv[1]):
			continue
		if candidate not in derivations:
			derivations[candidate] = derivations[cur] + [(candidate, rule)]
			if len(derivations[candidate]) > maxdepth:
				maxdepth = len(derivations[candidate])
			heappush(to_visit, (len(candidate.value), candidate))
			


while len(to_visit) > 0:
	# cur = to_visit.popleft()
	length, cur = heappop(to_visit)
	lengthmap[length].append(cur)
	print length, cur
	if cur.value == "MU":
		print "FOUND IT!", derivations[cur]
		sys.exit(0)

	to_add = cur.apply_r3()
	extend_to_visit("r3", to_add)
	
	to_add = cur.apply_r4()
	extend_to_visit("r4", to_add)
		
	to_add = cur.apply_r1()
	extend_to_visit("r1", to_add)
	
	to_add = cur.apply_r2()
	extend_to_visit("r2", to_add)
	

for k,v in lengthmap.iteritems():
	if k > 5:
		continue
	print "{}:".format(k)
	for v1 in v:
		print v1, len(derivations[v1]), derivations[v1]
	print 

print maxdepth