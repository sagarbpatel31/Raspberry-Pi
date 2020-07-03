import Adafruit_DHT
from time import sleep

dht = Adafruit_DHT.DHT11
pin=19
hum,temp = Adafruit_DHT.read_retry(dht,pin)
while True:
    try:
        hum,temp=Adafruit_DHT.read_retry(dht,pin)
        print("Humidity: ",hum)
        print("Temperature: ",temp)
    except:
        print("Interrupted...")
        break
    sleep(2)
