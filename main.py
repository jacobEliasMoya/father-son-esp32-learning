from machine import Pin
from time import sleep

red = Pin(2, Pin.OUT)
blue = Pin(42, Pin.OUT)
green = Pin(41, Pin.OUT)

while True:
    red.value(1)
    sleep(.1)

    blue.value(1)
    sleep(.1)

    green.value(1)
    sleep(.1)

    red.value(0)
    sleep(.1)

    blue.value(0)
    sleep(.1)

    green.value(0)
    sleep(.1)
