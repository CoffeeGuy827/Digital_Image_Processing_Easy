import numpy as np
import cv2

img = cv2.imread('salt.png')

height = img.shape[0]
width = img.shape[1]

dst = np.zeros((height, width, 3), np.uint8)
filter_size = 7
filter = np.ones((filter_size, filter_size)) / (filter_size*filter_size)

for h in range(3, height - 3):
    for w in range(3, width - 3):
        sb = 0.0
        sg = 0.0
        sr = 0.0
        for y in range(-3, 4):
            for x in range(-3, 4):
                sb += img[h + y, w + x, 0] * filter[y + 3, x + 3]
                sg += img[h + y, w + x, 1] * filter[y + 3, x + 3]
                sr += img[h + y, w + x, 2] * filter[y + 3, x + 3]

        dst[h, w, 0] = sb.astype(np.uint8)
        dst[h, w, 1] = sg.astype(np.uint8)
        dst[h, w, 2] = sr.astype(np.uint8)

cv2.imwrite('meansalt7.png'.format(str(filter_size)), dst)