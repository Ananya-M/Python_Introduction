import cv2
import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt

img = cv2.imread('messi5.jpg')
ball = img[280:340, 330:390]
print (img.size)
plt.imshow(img)
#img[273:333, 100:160] = ball
