import cv2
import numpy as np

kernel = np.ones((5,5), np.uint8) # creating a kernel of size 5x5 with all values as 1 and data type as unsigned integer 8 bit , this kernel will be used for dilation and erosion

# thes are 5 important basic function in openCV for image processing

img = cv2.imread("Resources/lena.png")
# converting the image to grey scale , can also be done by cv2.imread("Resources/lena.png", 0) , but this is more efficient and better way to do it
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# applying Gaussian blur to the image in which [a,a] a should be an odd number and 0 is the standard deviation in X and Y direction , if we put 0 it will calculate the standard deviation based on the kernel size
imgBlur = cv2.GaussianBlur(imgGrey, [11,11] , 0)
# the lesser the threshold value the more edges will be detected and the higher the threshold value the less edges will be detected
imgCanny = cv2.Canny(imgGrey, 100,100)
# dilation is used to increase the white region in the image or to increase the size of the foreground object , it is also used to connect the broken parts of an object
imgDialate = cv2.dilate(imgCanny , kernel , iterations=1)
# kernel is the matrix which is used to dilate the image and iterations is the number of times we want to dilate the image
imgErosion = cv2.erode(imgDialate , kernel , iterations=1)
# erosion is used to decrease the white region in the image or to decrease the size of the foreground object , it is also used to disconnect the connected parts of an object

cv2.imshow("Image", img)
cv2.imshow("Image Grey", imgGrey)
cv2.imshow("Image Blur", imgBlur)
cv2.imshow("Image Canny", imgCanny)
cv2.imshow("Image Dialate", imgDialate)
cv2.imshow("Image Erosion", imgErosion)

cv2.waitKey(0)
# waitKey(0) is used to keep the window open until we press any key on the keyboard , if we put a number instead of 0 then the window will close after that many milliseconds