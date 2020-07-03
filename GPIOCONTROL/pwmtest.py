import RPi.GPIO as GPIO
import sys
GPIO.setmode(GPIO.BOARD)
red=11
GPIO.setup(red,GPIO.OUT)
mypwm=GPIO.PWM(red,100)
mypwm.start(0)
while(1):
    try:
        bright = int(input("How bright do you want for LED?(1-6) "))
        mypwm.ChangeDutyCycle(2**bright)
    except KeyboardInterrupt:
        print("Completed...")
        GPIO.cleanup()
        mypwm.stop()
        sys.exit(0)
mypwm.stop()
GPIO.cleanup()
