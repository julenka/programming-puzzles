
__author__ = 'julenka'

import Image

im = Image.open("p11_cave.jpg")
im_c,im_r = im.size
im1 = Image.new("RGB", (im_c/2,im_r/2))
im2 = Image.new("RGB", (im_c/2,im_r/2))

pix,pix1,pix2 = im.load(),im1.load(),im2.load()

for r in xrange(im_r):
    for c in xrange(im_c):
        p = pix[c,r]
        i = r * im_r + c
        if i % 2 == 0:
            pix1[c/2,r/2] = p
        else:
            pix2[c/2,r/2] = p

im1.show()
im2.show()

