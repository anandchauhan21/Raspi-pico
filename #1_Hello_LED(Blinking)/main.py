
import machine
import utime

#Define on-board led whitch pin is no 25.

led_onboard = machine.Pin(25,machine.Pin.OUT)

#Start while loop.
while True:
  #give led value 1 so led get turn on
  led_onboard.value(1)
  
  #sleep(1) it turn led on for one sec.
  utime.sleep(1)
  
  #give led value 0 so led get turn off
  led_onboard.value(0)
  
  #sleep(0) it turn led off for one sec
  utime.sleep(1)
  
