import dht
from machine import Pin
from time import sleep

led_blue = Pin(2, Pin.OUT)
led_red = Pin(16, Pin.OUT)
sensor = dht.DHT11(Pin(4))


def toggle_leds():
    led_blue.value(0)
    led_red.value(0)
    sleep(1)
    led_blue.value(1)
    led_red.value(1)
    sleep(1)

def toggle_leds_on():
    led_blue.value(0)
    led_red.value(0)

def toggle_leds_off():
    led_blue.value(1)
    led_red.value(1)

def read_sensor():
    sensor.measure()
    return sensor.temperature(), sensor.humidity()
