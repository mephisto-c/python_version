#  -*-  coding: utf-8 -*-
'''
create on Thr Noe 7  16:11

@author: mephisto-c

'''
import numpy as np
import matplotlib.pyplot as plt
import cv2
import imutils

img_2 = cv2.imread('F:\python_version\image_sample\sample\\nut\M20\\1 (1).jpg')
plt.figure('image')
plt.imshow(imutils.opencv2matplotlib(img_2))
plt.axis('off')
plt.show()


