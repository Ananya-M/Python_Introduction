from cv2 import cv2
import numpy as np
img=cv2.imread('messi.jpg')
print (img.shape)
print (img.size)
print (img.dtype)
ball = img[280:340, 330:390]
img[273:333, 100:160] = ballexit
cv2.imshow('image',img)
cv2.waitKey(0)
