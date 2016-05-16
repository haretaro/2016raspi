import cv2
import numpy as np
import picam
import time

im0 = picam.capture()
gray0 = np.asarray(cv2.cvtColor(im0, cv2.COLOR_RGB2GRAY))

print('wait 5 sec')
time.sleep(5)

im1 = picam.capture()
gray1 = np.asarray(cv2.cvtColor(im1, cv2.COLOR_RGB2GRAY))

diff = gray1 - gray0
cv2.imwrite('diff.jpg',diff)
