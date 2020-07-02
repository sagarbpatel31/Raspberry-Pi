from nanpy import (ArduinoApi,SerialManager)
from time import sleep

ledPin = 7
buttonPin = 8
ledState = False
buttonState=0
try:
    connection = SerialManager()
    a=ArduinoApi(connection=connection)
except:
    print("Failed to connect to Arduino")

a.pinMode(ledPin,a.OUTPUT)
a.pinMode(buttonPin,a.INPUT)

while True:
    try:
        buttonState=a.digitalRead(buttonPin)
        print("Button state is ",buttonState)
        if buttonState:
            if ledState:
                a.digitalWrite(ledPin,a.LOW)
                ledState=False
                print("LED off")
                sleep(1)
            else:
                a.digitalWrite(ledPin,a.HIGH)
                ledState=True
                print("LED on")
                sleep(1)
    except KeyboardInterrupt:
        a.digitalWrite(ledPin,a.LOW)

