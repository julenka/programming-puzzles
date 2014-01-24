__author__ = 'julenka'
# compute see it say it sequence
# 1, 11, 21, 1211, 111211, 311221, 13212211, 111212112211, 31121112212211

from itertools import groupby

cur, result = '1',[]
for i in xrange(31):
    result.append(cur)
    cur = ''.join([str(len(list(g))) + k for k,g in groupby(cur)])

print result
print len(result[30])

