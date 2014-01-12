__author__ = 'julenka'

import urllib2
import re
pfx = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
# first val is 12345
vals=["12345"]
remaps = {"16044":"8022"}
strs = [""]
for i in range(400):
    next_str = urllib2.urlopen(pfx+vals[-1]).read()
    print i,":",next_str
    strs.append(next_str)
    m = re.search('and the next nothing is (\d+)', next_str)
    if not m:
        print "Error: string didn't match:", next_str
        break
    v = m.group(1)
    if v in remaps:
        vals.append(remaps[v])
    else:
        vals.append(m.group(1))