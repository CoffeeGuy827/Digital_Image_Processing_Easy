import cv2
import numpy as np


def median():
    img = cv2.imread('Lenna.png')
    height, width, channel = img.shape
    noise = img.copy()
    salt = int(height * width * channel * 0.1)
    for i in range(salt):
        row = int(np.random.randint(99999, size=1) % height)
        col = int(np.random.randint(99999, size=1) % width)
        ch = int(np.random.randint(99999, size=1) % channel)
        noise[row][col][ch] = 255 if np.random.randint(99999, size=1) % 2 == 1 else 0

    out1 = np.zeros((height + 2, width + 2, channel), dtype=float)
    out1[1: 1 + height, 1: 1 + width] = img.copy().astype(float)
    temp1 = out1.copy()

    out2 = np.zeros((height + 4, width + 4, channel), dtype=float)
    out2[2: 2 + height, 2: 2 + width] = img.copy().astype(float)
    temp2 = out2.copy()



    out1 = out1[1:1 + height, 1:1 + width].astype(np.uint8)
    cv2.imwrite('salt.png', noise)
    cv2.imwrite('median.png', out1)
    cv2.waitKey(0)

median()

