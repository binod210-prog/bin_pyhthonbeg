import numpy as np
import imageio
import scipy.ndimage

import cv2


img = "ratan.jpg"

def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.2989,0.5870,0.1140])
     #its 2 dimensional array formula to convert image to gray scale

def dodge(front, back):
    final_sketch = front*255/(255-back)

    #if image is greater than 255 then it will convert it to 255

    final_sketch[final_sketch>255]=255
    final_sketch[back==255]=255      # convert any suitable coloumn to categorial  type we will use aspect function

    # uint8 is for 8 bit signed integer

    return final_sketch.astype('uint8')
    


imgread = imageio.imread(img)   # To read the given image
gray = rgb2gray(imgread)        #First we will image to black  and white to gray scale


i = 255-gray    # 0, 0, 0 for darketst color and 255, 255, 255 for brightest color


# To convert it to blur image

blur = scipy.ndimage.filters.gaussian_filter(i, sigma=15)

#sigma is the intensity  of blurness of image

r = dodge(blur, gray)   # this function will convert image to sketch  by taking two parameters


cv2.imwrite('ratan-sketch.png',r)

