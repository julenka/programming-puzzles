__author__ = 'julenka'

import Image

im = Image.open("p7_oxygen.png")
pix = im.load()
print ''.join([chr(x) for x in [pix[x2,47][0] for x2 in xrange(5,629,7)]])

print ''.join([chr(x) for x in [105, 110, 116, 101, 103, 114, 105, 116, 121]])
