__author__ = 'julenka'

import re
import os
from zipfile import ZipInfo,ZipFile

base='p6_channel'
next = "90052"

z = ZipFile(open('channel.zip'))
comments = [x.comment for x in z.infolist()]
comments_collected = []
names = {x.filename.replace('.txt',''):i for i,x in enumerate(z.infolist())}

for i in range(1818):
    with open(os.path.join(base, "%s.txt" % next)) as f:
        next_str = f.read()
        print i,":",next_str
        m = re.search('Next nothing is (\d+)', next_str)
        if not m:
            print "Error: string didn't match:", next_str
            break
        next = m.group(1)
        comments_collected.append(comments[names[next]])

print ''.join(comments_collected)