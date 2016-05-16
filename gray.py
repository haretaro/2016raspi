import cv2
import picam

im = picam.capture()
gray = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
print(cv2.imwrite('../gray.jpg', gray))
