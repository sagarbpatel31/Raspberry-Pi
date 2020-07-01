from time import sleep
import sys
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
first=8
second=10
third=11
GPIO.setup(first,GPIO.OUT)
GPIO.setup(second,GPIO.OUT)
GPIO.setup(third,GPIO.OUT)

sleeptime=0.1
while True:
    try:
        GPIO.output(first,True)
        GPIO.output(second,False)
        GPIO.output(third,False)
        sleep(sleeptime)
        GPIO.output(first,False)
        GPIO.output(second,True)
        sleep(sleeptime)
        GPIO.output(first,True)
        sleep(sleeptime)
        GPIO.output(first,False)
        GPIO.output(second,False)
        GPIO.output(third,True)
        sleep(sleeptime)
        GPIO.output(first,True)
        sleep(sleeptime)
        GPIO.output(first,False)
        GPIO.output(second,True)
        sleep(sleeptime)
        GPIO.output(first,True)
        sleep(sleeptime)
    except KeyboardInterrupt:
        print("Exit")
        GPIO.cleanup()
        sys.exit(0)

GPIO.cleanup()
