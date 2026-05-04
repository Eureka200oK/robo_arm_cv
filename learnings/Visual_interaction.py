import cv2
import numpy as np

# remeber this while resizing and cropping always remeber that the image is in (height , width) format and not in (width , height) format as we are used to in mathematics 
# also first try to know the shape of the image using img.shape and then use that shape to resize or crop the image accordingly

""" img resizing , one thing to notice that the image has 
[ +y in south direction(↓) and +x in east direction ], 
    while in mathematics we have 
[ +y in north direction(↑) and +x in east direction ]
"""
img = cv2.imread('Resources/lena.png')
print(img.shape) # (512, 512, 3) height , width , channels(blue , green , red)

imgresize = cv2.resize(img ,[1024,1024]) # [width , height] , here we are resizing the image to 1024 x 1024
print(imgresize.shape) # (1024, 1024, 3)

imgcropped = img[0:1000, 250:500] # [y1:y2 , x1:x2] [height , width] , here we are cropping the image from (0,250) to (1000,500)
print(imgcropped.shape) # (1000, 250, 3)

img_crop_resized = cv2.resize(imgcropped, [img.shape[1],img.shape[0]]) # img.shape[1] is width and img.shape[0] is height , here we are resizing the cropped image to the original image size
print(img_crop_resized.shape) # (512, 512, 3) 

cv2.imshow('image', img)
cv2.imshow('resized image', imgresize)
cv2.imshow('cropped image', imgcropped)
cv2.imshow('cropped and resized image', img_crop_resized)
cv2.waitKey(0)