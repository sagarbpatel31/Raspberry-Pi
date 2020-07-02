import picamera
#Setup the camera
print("About to take a picture")
with picamera.PiCamera() as camera:
    camera.resolution=(1280,720)
    camera.capture("/home/pi/Desktop/cookie/newimage1.jpg")
print("Picture Taken")
