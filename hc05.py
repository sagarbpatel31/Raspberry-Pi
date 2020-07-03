from gpiozero import DistanceSensor
from time import sleep

dist= DistanceSensor(echo=18,trigger=17)
while True:
    try:
        print("Distance: ",dist.distance*100)
        sleep(2)
    except:
        print("Interrupted")
        break
