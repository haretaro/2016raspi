import cv2
import numpy as np
import picam
import time

im0 = picam.capture()
gray0 = np.asarray(cv2.cvtColor(im0, cv2.COLOR_RGB2GRAY))
bin0 = cv2.threshold(gray0, 127, 256, cv2.THRESH_BINARY)
cv2.imwrite('1.jpg',gray0)
print(bin0)

print('wait 5 sec')
time.sleep(5)

im1 = picam.capture()
gray1 = np.asarray(cv2.cvtColor(im1, cv2.COLOR_RGB2GRAY))
bin1 = cv2.threshold(gray1, 127, 256, cv2.THRESH_BINARY)
cv2.imwrite('2.jpg',gray1)

diff = gray1 - gray0
print(diff)
cv2.imwrite('diff.jpg',diff)

print(np.linalg.norm(diff))
