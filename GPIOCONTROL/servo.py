import RPi.GPIO as GPIO
import time
import sys
GPIO.setmode(GPIO.BOARD)
servo=11
GPIO.setup(servo,GPIO.OUT)
mypwm=GPIO.PWM(servo,50)
mypwm.start(4)
for i in range(0,180):
    try:
        dc=(1./18)*(i)+2
        mypwm.ChangeDutyCycle(dc)
        time.sleep(0.01)
    except KeyboardInterrupt:
        print("Interrupted...")
        mypwm.stop()
        GPIO.cleanup()
        sys.exit(0)
mypwm.stop()
GPIO.cleanup()
