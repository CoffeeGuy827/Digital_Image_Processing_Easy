import math

from PIL import  Image
from PIL import ImageFilter

img = Image.open('Einstein.jpg')

# #Negative Transformation
# # read pixel and apply negative transformation
# for i in range(0, img.size[0]-1):
#     for j in range(0, img.size[1]-1):
#         # get pixel at (i,j) of the image
#         pix = img.getpixel((i,j))
#
#         r = 255 - pix[0]
#         g = 255 - pix[1]
#         b = 255 - pix[2]
#
#         img.putpixel((i,j),(r,g,b))
#
# img.save('NT.png')

# Log Transformation
c = 255/math.log(255+1,10)

for i in range(0, img.size[0]-1):
    for j in range(0, img.size[1]-1):
        # get pixel at (i,j) of the image
        pix = img.getpixel((i,j))

        r = round(c* math.log(float(1+pix[0]),10))
        g = round(c* math.log(float(1+pix[1]),10))
        b = round(c* math.log(float(1+pix[2]),10))

        img.putpixel((i,j),(r,g,b))

img.save('LT.png')

#Gamma Transformation
# gamma = 0.5
#
# for i in range(0, img.size[0]-1):
#     for j in range(0, img.size[1]-1):
#         pix = img.getpixel((i, j))
#         r = pow(pix[0]/255,(1/gamma))*255
#         g = pow(pix[1]/255,(1/gamma))*255
#         b = pow(pix[2]/255,(1/gamma))*255
#         if r >= 255 :
#             r = 255
#         if g >= 255 :
#             g = 255
#         if b >= 255 :
#             b = 255
#         img.putpixel((i, j), (int(r),int(g),int(b)))
#         # get pixel at (i,j) of the image
#
# img.save('GT.png')