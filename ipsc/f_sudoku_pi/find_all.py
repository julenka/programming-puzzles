__author__ = 'julenka'

import urllib2
import itertools
import json

# urllib2.urlopen('http://www.angio.net/newpi/piquery?q=123456789').read()

# format:
# digits offset
out_file = open('test.out', 'w')

all_permutations = itertools.permutations('123456789')

for i, permutation_tuple in enumerate(all_permutations):
    permutation = "".join(list(permutation_tuple))
    result_str = urllib2.urlopen('http://www.angio.net/newpi/piquery?q=%s' % permutation).read()
    result_json = json.loads(result_str)
    if(result_json['results'][0]['status'] == 'notfound'):
        continue
    out_str = "%s %s" % (permutation, result_json['results'][0]['p'])
    print >> out_file, out_str
    print out_str