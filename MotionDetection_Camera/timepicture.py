import picamera
from subprocess import call
from datetime import datetime
from time import sleep

filepath="/home/pi/Desktop/cookie/pics/"
pictotal=5
piccount=0

while piccount < pictotal:
    currentTime = datetime.now()
    pictime=currentTime.strftime("%Y.%m.%d-%H%M%S")
    picname=pictime+'.jpg'
    completefilepath = filepath+picname

    with picamera.PiCamera() as camera:
        camera.resolution = (1280,720)
        camera.capture(completefilepath)
        print("We have taken a picture")

    timest=currentTime.strftime("%Y.%m.%d - %H:%M:%S")
    command = "/usr/bin/convert " + completefilepath + " -pointsize 36 -fill red -annotate +700+650 '" + timest + "' " + completefilepath
    
    call([command],shell=True)
    print("We have timestampped our picture")

    piccount+=1
    sleep(5)
