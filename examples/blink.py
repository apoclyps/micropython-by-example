from machine import Pin
from time import sleep

# GPIO16 (D0) is the internal LED for NodeMCU
led_blue = Pin(2, Pin.OUT)
led_red = Pin(16, Pin.OUT)

# The internal LED turn on when the pin is LOW
while True:
    led_blue.value(0)
    led_red.value(0)
    sleep(1)
    led_blue.value(1)
    led_red.value(1)
    sleep(1)
