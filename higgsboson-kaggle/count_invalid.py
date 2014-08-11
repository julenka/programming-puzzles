#!/usr/bin/env python
__author__ = 'julenka'


from csv import DictReader
from collections import Counter

def get_invalid_counts(in_path):
    invalid_counts = Counter()

    for row in DictReader(open(in_path, "rU")):
        for k,v in row.iteritems():
            if k in ["Weight", "Label"]:
                continue
            if k not in invalid_counts:
                invalid_counts[k] = 0
            if float(v) == -999.0:
                invalid_counts[k] += 1
    return invalid_counts

def main(in_path):
    print "reading from ", in_path
    invalid_counts = get_invalid_counts(in_path)
    print 'feature, count'
    for k,v in invalid_counts.iteritems():
        print k, ',', v         

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print "usage: {0} in_file".format(sys.argv[0])
        exit()
    main(sys.argv[1])


