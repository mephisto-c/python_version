#  -*- coding:utf-8 -*-
'''
 create on Thr Nov 7 19:02

 @author: mephisto-c

'''
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
