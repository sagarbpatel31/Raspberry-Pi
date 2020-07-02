import p3picam
import picamera
from datetime import datetime
from subprocess import call

picpath = "/home/pi/Desktop/cookie/imagesfinal/"
motionState=False
def captureImage(currentTime,picpath):
    picName = currentTime.strftime("%Y.%m.%d-%H%M%S") + '.jpg'
    with picamera.PiCamera() as camera:
        camera.resolution = (1280,720)
        camera.capture(picpath + picName)
    print("We have taken a picture")

    return picName

def getTime():
    currentTime = datetime.now()
    return currentTime

def timeStamp(currentTime,picpath,picName):

    filepath = picpath +picName
    message = currentTime.strftime("%Y.%m.%d - %H:%M:%S")
    command = "/usr/bin/convert " + filepath + " -pointsize 38 -fill red -annotate +700+650 '" + message + "' " + filepath
    call([command],shell=True)
    print("We have timestamped our picture..")

while True:
    motionState = p3picam.motion()
    print(motionState)
    if motionState:
        currentTime=getTime()
        picName = captureImage(currentTime,picpath)
        timeStamp(currentTime,picpath,picName)
    else:
        print("No motion detected")
