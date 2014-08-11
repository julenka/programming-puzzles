# coding: utf-8
import count_invalid
invalid_counts = count_invalid.get_invalid_counts("data/training-small.csv")
no_invalid = [k for k,v in invalid_counts.iteritems() if v == 0]
