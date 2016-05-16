from picam import capture
import numpy as np
import cv2
import time

#base = np.asarray(cv2.imread('base.jpg'))
base = np.asarray(capture())

while True:
    image = np.asarray(capture())
    diff = image - base
    norm = np.linalg.norm(diff)
    print(norm)
    time.sleep(10)
