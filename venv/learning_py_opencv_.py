 #  -*- coding: utf-8 -*-

 '''
 create on Fri Nov 9 21.52
 
 @author: mephsto-c
 '''

 import cv2
 import numpy as np

 cap = cv2.VideoCapture(0)

 while(cap.isOpened()):
     ret,frame =