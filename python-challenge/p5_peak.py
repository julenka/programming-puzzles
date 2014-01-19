__author__ = 'julenka'

from pickle import Unpickler
unpickled = Unpickler(open('p5_data.p', 'r')).load()
for line in unpickled:
    print ''.join([v * cnt for (v,cnt) in line])
