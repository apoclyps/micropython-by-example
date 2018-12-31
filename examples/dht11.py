import dht
from machine import Pin
from time import sleep

# GPIO04 (D2) is the PIN used for data on the NodeMCU
sensor = dht.DHT11(Pin(4))

# For accurate results, it's best to allow the sensor time for voltage to dissipate in the sensor
while True:
    sensor.measure()
    print('Temp: {0:.2f}, Humidity {1:.2f}'.format(sensor.temperature(), sensor.humidity()))
    sleep(5)
