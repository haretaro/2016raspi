import cv2
import picap

cap = picap.get_capturer(False)
ret, frame = cap.read()
print(frame)
cv2.imwrite('hoge.jpg',frame)
cap.release()
