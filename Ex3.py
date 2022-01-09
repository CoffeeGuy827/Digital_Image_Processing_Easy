# import cv2, numpy, matplotlib
import cv2
import numpy as np
import matplotlib.pyplot as plt


def hist_plot(img):
    count = []

    r = []

    for k in range(0, 256):
        r.append(k)
        count1 = 0

        for i in range(m):
            for j in range(n):
                if img[i, j] == k:
                    count1 += 1
        count.append(count1)

    return (r, count)


img = cv2.imread('Lenna.png', 0)

m, n = img.shape
r1, count1 = hist_plot(img)

plt.bar(r1, count1)
plt.xlabel('intensity value')
plt.ylabel('number of pixels')
plt.title('Histogram of the original image')
plt.savefig('Ex3.png')

constant = (255 - 0) / (img.max() - img.min())
img_stretch = img * constant
r, count = hist_plot(img_stretch)

plt.stem(r, count)
plt.xlabel('intensity value')
plt.ylabel('number of pixels')
plt.title('Histogram of the stretched image')
plt.savefig('Ex3_.png')

# cv2.imwrite('Ex3.png', img_stretch)