# Complete project details at https://RandomNerdTutorials.com

from machine import Pin
from time import sleep
import dht
import network

from umqtt.simple import MQTTClient

CLIENT_NAME = 'Divya'
BROKER_ADDR = '172.16.2.7'
mqttc = MQTTClient(CLIENT_NAME, BROKER_ADDR, keepalive=60)
mqttc.connect()

BTN_TOPIC_TEMP = CLIENT_NAME.encode() + b'/DiviPad/temp'
BTN_TOPIC_HUM = CLIENT_NAME.encode() + b'/DiviPad/humidity'

#sensor = dht.DHT22(Pin(14))
sensor = dht.DHT11(Pin(19))


while True:
  try:
    sleep(30)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    print('Temperature: %3.1f C' %temp)
    #print('Temperature: %3.1f F' %temp_f)
    print('Humidity: %3.1f %%' %hum)
    mqttc.publish( BTN_TOPIC_TEMP, str(temp).encode() )
    mqttc.publish( BTN_TOPIC_HUM, str(hum).encode() )
  except OSError as e:
    print('Failed to read sensor.')