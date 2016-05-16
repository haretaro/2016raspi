import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
print(frame)
cv2.imwrite('hoge.jpg',frame)
cap.release()
