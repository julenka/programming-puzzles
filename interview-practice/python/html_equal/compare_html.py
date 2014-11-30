#!/usr/bin/env python

from lxml.html import parse

def compare(file1, file2):
	doc1 = parse(file1)
	doc2 = parse(file2)
	doc1_root = doc1.getroot()
	doc2_root = doc2.getroot()

	doc1_iter = doc1.iter()
	doc2_iter = doc2.iter()

	doc1_words = []
	doc2_words = []

	doc1_ptr = -1
	doc2_ptr = -1

	doc1_done = False
	doc2_done = False

	while not (doc1_done and doc2_done):
		if not doc1_done:
			try:
				doc1_cur = doc1_iter.next()
				doc1_words += [x for x in doc1_cur.text.split() if len(x) > 0]
			except StopIteration:
				doc1_done = True
		if not doc2_done:
			try:
				doc2_cur = doc2_iter.next()
				doc2_words += [x for x in doc2_cur.text.split() if len(x) > 0]
			except StopIteration:
				doc2_done = True
		l1 = len(doc1_words)
		l2 = len(doc2_words)
		for i in xrange(min(l1,l2) - 1,doc1_ptr, -1):
			print i
			if doc1_words[i] != doc2_words[i]:
				print "{} != {}".format(doc1_words[i], doc2_words[i])
				return False
		doc1_ptr = min(l1,l2)
		doc2_ptr = min(l1,l2)
	if len(doc1_words) != len(doc2_words):
		return False

	print " ".join(doc1_words)
	print "*" * 80
	print " ".join(doc2_words)
	return True


f1 = open("1.html")
f2 = open("2.html")
result = compare(f1,f2)
print "*" * 80
print "result is", result