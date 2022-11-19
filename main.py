#Divya Kara

from machine import Pin, I2C
import ssd1306
from hcsr04 import HCSR04
from time import sleep
import dht
import network
from umqtt.simple import MQTTClient

#functions 
def read_tempsensor():
  sensorTemp.measure()
  temp = sensorTemp.temperature()
  hum = sensorTemp.humidity()
  #temp_f = temp * (9/5) + 32.0
  print('Temperature: %3.1f *C' %temp)
  #print('Temperature: %3.1f F' %temp_f)
  print('Humidity: %3.1f %%' %hum)
  return temp, hum


print("Sensors setting up!")

#Brooker
CLIENT_NAME = 'Office'
BROKER_ADDR = '172.16.2.7'
mqttc = MQTTClient(CLIENT_NAME, BROKER_ADDR, keepalive=60)
mqttc.connect()

#Topics
BTN_TOPIC_TEMP = CLIENT_NAME.encode() + b'/LMP/temp'
BTN_TOPIC_HUM = CLIENT_NAME.encode() + b'/LMP/humidity'
BTN_TOPIC_DIST = CLIENT_NAME.encode() + b'/LMP/distance'

# ESP32 Pin assignment 
i2c = I2C(scl=Pin(22), sda=Pin(21))
sensorDist = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)
sensorTemp = dht.DHT11(Pin(19))

#Display 
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

graph = ""
timerCount = 0
while True:
  try:
    sleep(1)
    timerCount = timerCount + 1
    #print('Counter', timerCount)
    #read temp sensor
    temp, hum = read_tempsensor()

    #Read distance
    oled.fill(0)
    #oled.show()
    distance = sensorDist.distance_mm()
    print('Distance:', distance, 'mm')
    print('--------------------------')
    
    #Show text on display
    oled.text("Distance: " + str(distance) + " mm", 0, 15)
    oled.text("Temp: " + str(temp) + "'C", 0, 35)
    oled.text("Humidity: " + str(hum) + " %", 0, 55)
    oled.show()
    #sleep(1)

    #Only send temp data every minute
    if timerCount == 60:
        #publish to Mqtt
        mqttc.publish( BTN_TOPIC_TEMP, str(temp).encode() )
        mqttc.publish( BTN_TOPIC_HUM, str(hum).encode() )
        #reset timer
        timerCount = 0
        
    mqttc.publish( BTN_TOPIC_DIST, str(distance).encode() )
    
    
  except OSError as e:
    print('Failed to read sensor.')
    