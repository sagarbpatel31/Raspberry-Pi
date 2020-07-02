import pigpio
import tempsensor
from time import sleep

pi = pigpiod.pi()
dht11 = tempsensor.sensor(pi,27)
dht11.trigger()

sleepTime = 3

def readDHT11():
    dht11.trigger()
    humidity = '%.2f' %(dht11.humidity())
    temp = '%.2f' %(dht11.temperature())
    return (humidity,temp)

while True:
    humidity,temperature = readDHT11()
    print("Humidity is: " +humidity + " %")
    print("Temperature is: "+temperature+" C")
    sleep(sleepTime)
