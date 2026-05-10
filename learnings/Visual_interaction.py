import cv2
import numpy as np

img = np.zeros((512,700,3),np.uint8)
# this is a black image of 512x700 pixels with 3 color channels (BGR)

cv2.rectangle(img,(128,128),(192,256),(0,165,255),cv2.FILLED)
# this draws a filled rectangle on the image with the top-left corner at (128,128) and the bottom-right corner at (192,256) using the color (0,165,255) which is orange in BGR format.
cv2.line(img,(128,128),(128,384),(0,165,255),5)
# this draws a line on the image from the point (128,128) to the point (128,384) using the color (0,165,255) and a thickness of 5 pixels. 
cv2.line(img,(128,256),(256,384),(0,165,255),5)
# this draws a line on the image from the point (128,256) to the point (256,384) using the color (0,165,255) and a thickness of 5 pixels.
cv2.circle(img,(192,192),64,(0,165,255),cv2.FILLED)
# this draws a filled circle on the image with the center at (192,192) and a radius of 64 pixels using the color (0,165,255).
cv2.putText(img,'ahul',(256,320),cv2.FONT_HERSHEY_SIMPLEX,5,(0,165,255),2)
# this puts the text 'ahul' on the image at the position (256,320) using the font cv2.FONT_HERSHEY_SIMPLEX with a font scale of 5, color (0,165,255) and thickness of 2 pixels.

# Finally the Output image is Rahul
cv2.imshow('image',img)
cv2.waitKey(0)