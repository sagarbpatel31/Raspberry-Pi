from time import sleep
import sys
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
button1=16
button2=12
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
while(1):
    try:
        if GPIO.input(button1)==0:
            print("Button1 was pressed")
            sleep(0.05)
        if GPIO.input(button2)==0:
            print("Button2 was pressed")
            sleep(0.05)
    except KeyboardInterrupt:
        print("Interrupted")
        GPIO.cleanup()
        sys.exit(0)
