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
pwm1=GPIO.PWM(led1,1000)
pwm2=GPIO.PWM(led2,1000)
pwm1.start(0)
pwm2.start(0)
bright=1

while(1):
    try:
        if GPIO.input(button1)==0:
            print("Button 1 was pressed...")
            bright=bright/1.25
            if bright<0:
                bright=0
                print("Led is off 0 brightness")
            pwm1.ChangeDutyCycle(bright)
            pwm2.ChangeDutyCycle(bright)
            sleep(0.25)
            print("Your brightness is ",bright)
        if GPIO.input(button2)==0:
            print("Button 2 was pressed...")
            bright=bright*1.25
            if(bright>100):
                bright=100
                print("You are having full brightness...")
            pwm1.ChangeDutyCycle(bright)
            pwm2.ChangeDutyCycle(bright)
            sleep(0.25)
            print("Your brightness is ",bright)
    
    except KeyboardInterrupt:
        print("Interrupted...")
        GPIO.cleanup()
        sys.exit(0)
