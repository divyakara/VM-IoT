# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
# Complete project details at https://RandomNerdTutorials.com/micropython-hc-sr04-ultrasonic-esp32-esp8266/
from hcsr04 import HCSR04
from time import sleep
import network

def connect_wifi(ssid, password):
#while True:
  #try:
    #sleep(2)    
  
  #connect to wifi
  wlan = network.WLAN(network.STA_IF)
  wlan.active(True)
  if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        pass
  print('Network config:', wlan.ifconfig())
  print('Connected to ', ssid)


# ESP32
'''
sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)

# ESP8266
#sensor = HCSR04(trigger_pin=12, echo_pin=14, echo_timeout_us=10000)

while True:
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')
    sleep(1)
'''
ssid = 'Virtual-GBG'
password = 'awellhiddensecret'

print("Booting up!")
connect_wifi(ssid, password)