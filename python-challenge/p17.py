__author__ = 'julenka'

from PIL import Image

im = Image.open("p17_mozart.gif")
# Convert to RGB because gifs store indices into color pallettes
im_rgb = im.convert("RGB")
im_width, im_height = im_rgb.size
im_seq = list(im_rgb.getdata())

im_out = Image.new("RGB", (im_width, im_height))
im_out_pix = im_out.load()

for y in range(im_height):
    full_row = im_seq[im_width * y : im_width * (y + 1)]
    i = 0
    for r,g,b in full_row:
        if r == 255 and g == 0 and b == 255:
            new_row = full_row[i:] + full_row[:i]
            for x in range(im_width):
                    im_out_pix[x, y] = new_row[x]
            break
        i += 1
    else:
        print "magenta in row {} not found".format(r)

im_out.show()
