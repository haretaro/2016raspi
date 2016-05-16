from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2
import time

camera = PiCamera()

def capture(resolution=(480,320)):
    camera.resolution = resolution
    rawCapture = PiRGBArray(camera, size=resolution)

    time.sleep(0.1)

    camera.capture(rawCapture, format='bgr')
    image = rawCapture.array
    return image
