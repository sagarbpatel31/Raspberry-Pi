import Adafruit_DHT
import paho.mqtt.client as mqtt
import json
import os
import sys
import time

host='demo.thingsboard.io'
INTERVAL=2
access_token ='DHT11_ACCESS_TOKEN'
dht_sensor=Adafruit_DHT.DHT11
pin=19
sensor_data = {'tem':0,'humidity':0}
next_reading = time.time()
client = mqtt.Client()
client.username_pw_set(access_token)
client.connect(host,1883,60)
client.loop_start()

while True:
    try:
        humidity,tem=Adafruit_DHT.read_retry(dht_sensor,pin)
        print(u"Temperature: {:g}\u00b0C, Humidity: {:g}%".format(tem,humidity))
        sensor_data['tem']=tem
        sensor_data['humidity']=humidity
        client.publish('v1/devices/me/telemetry',json.dumps(sensor_data),1)
        next_reading += INTERVAL
        sleep_time=next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
    except:
        print("Interrupted....")
        break
client.loop_stop()
client.disconnect()
