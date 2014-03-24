__author__ = 'julenka'

from PIL import Image

im = Image.open("p14_wire.png")
im_seq = list(im.getdata())

out_im = Image.new("RGB", (100, 100))
out_pix = out_im.load()

n = 100
r = 0
c = 0
i = 0
while n > 0:
    # copy the top
    for cur_c in range(c, c + n):
        out_pix[r, cur_c] = im_seq[i]
        i += 1

    right_c = c + n - 1
    # copy the right
    for cur_r in range(r + 1, r + n):
        out_pix[cur_r, right_c] = im_seq[i]
        i += 1

    # copy the bottom
    bottom_r = r + n - 1
    for cur_c in range(right_c - 1, c - 1, -1):
        out_pix[bottom_r, cur_c] = im_seq[i]
        i += 1

    # copy the left
    left_c = c
    for cur_r in range(bottom_r - 1, r, -1):
        out_pix[cur_r, left_c] = im_seq[i]
        i += 1

    r += 1
    c += 1
    n -= 2
# im = Image.new("RGB", (512, 512), "white")

out_im.show()
out_im.save("p14_answer.png")