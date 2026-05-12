import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")

width ,height = 250,350

pt1 = np.float32([[385,344],[449,274],[574,345],[504,428]])
pt2 = np.float32([[0,0],[width,0],[width,height],[0,height]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgOutput = cv2.warpPerspective(img, matrix, (width,height))

for i in range(4):
    cv2.circle(img,(int(pt1[i][0]), int(pt1[i][1])), 5, (0,255,0), cv2.FILLED)

cv2.imshow("Output", imgOutput)

cv2.imshow("Cards", img)
cv2.waitKey(0)