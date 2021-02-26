import machine
import utime

red_led = machine.Pin(15,machine.Pin.OUT)
yellow_led = machine.Pin(14,machine.Pin.OUT)
green_led = machine.Pin(13,machine.Pin.OUT)

while True:
    red_led.value(1)
    utime.sleep(5)
    yellow_led.value(1)
    utime.sleep(2)
    red_led.value(0)
    yellow_led.value(0)
    green_led.value(1)
    utime.sleep(5)
    green_led.value(0)
    yellow_led.value(1)
    utime.sleep(3)
    yellow_led.value(0)
