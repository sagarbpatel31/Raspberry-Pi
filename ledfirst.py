import RPi.GPIO as GPIO
import time
import sys
GPIO.setmode(GPIO.BCM)
red=17

GPIO.setup(red,GPIO.OUT)
blink = int(input("How many times do you want to blink: "))
for i in range(blink):
    GPIO.output(red,True)
    time.sleep(1)
    GPIO.output(red,False)
    time.sleep(1)
GPIO.cleanup()
