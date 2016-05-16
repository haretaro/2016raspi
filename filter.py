#coding: utf-8
import cv2
import picam
import numpy as np

image = picam.capture()
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
cv2.imwrite('input.jpg', image)

#kernel = np.ones((3,3))/9 #移動平均フィルタ,ぼかし平滑化
kernel = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]) #ラプラシアンフィルタ,エッジ検出
#kernel = np.array([[1,0,-1],[2,0,-2],[1,0,-1]]) #横方向の微分

output = cv2.filter2D(image, -1, kernel)
cv2.imwrite('output.jpg', output)
