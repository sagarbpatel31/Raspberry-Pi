import picamera
from time import sleep
from subprocess import call
fil="pyvideo.h"
with picamera.PiCamera() as camera:
    camera.start_recording(fil)
    sleep(5)
    camera.stop_recording()

print("We are going to convert video to .mp4 format")
command=MP4Box -add pyvideo.h -out convideo.mp4

#call([command],shell=True)
print("Video converted....")
