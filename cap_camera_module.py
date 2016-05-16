import time
import picamera

camera = picamera.PiCamera()
camera.start_preview()
time.sleep(2)
camera.capture('hoge.jpg')
