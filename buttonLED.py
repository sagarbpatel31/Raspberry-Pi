import sys
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
button1=16
button2=12
led1=22
led2=18
GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
bs1=False
bs2=False

while(1):
    try:
        if GPIO.input(button1)==0:
            print("Button 1 was pressed...")
            if bs1==False:
                GPIO.output(led1,True)
                bs1=True
                sleep(0.5)
            elif bs1==True:
                GPIO.output(led1,False)
                bs1=False
                sleep(0.5)
        if GPIO.input(button2)==0:
            print("Button 2 was pressed...")
            if bs2==False:
                GPIO.output(led2,True)
                bs2=True
                sleep(0.5)
            elif bs2==True:
                GPIO.output(led2,False)
                bs2=False
                sleep(0.5)
    except KeyboardInterrupt:
        print("Interrupted...")
        GPIO.cleanup()
        sys.exit(0)
