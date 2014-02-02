__author__ = 'julenka'

evil2 = open("p12_evil2.gfx", 'rb').read()
out = [
    open('p12_im1.jpg', 'wb'),
    open('p12_im2.jpg', 'wb'),
    open('p12_im3.jpg', 'wb'),
    open('p12_im4.jpg', 'wb'),
    open('p12_im5.jpg', 'wb')
]

for i in range(5):
    bytes = evil2[i::5]
    out[i].write(bytes)

for f in out:
    f.close()



