# Streaming sensor data to Grafana dashboard using MQTT, Node-RED and InfluxDb
Divya Kara 

###### tags: `IoT` `MQTT` `MicroPython` `ESP32` 
---
**Table of Contents**


[TOC]

### Project Overview
This project shows how to set up a temperature/humidity- and distance sensor and visualize the data on a Grafana dashboard using MQTT broker, Node-RED and InfluxDb. 

Following this guide, I expect it to take approximately 8-10h to have everything running, including some unexpected time to troubleshoot.

``` 
Give a short and brief overview of what your project is about.
What needs to be included:
- [x] Title
- [x] Your name and student credentials (xx666xxx)
- [x] Short project overview
- [x] How much time it might take to do (an approximation)
```

### Objectives
In the office I'm working at the temperature in a room has been a big discussion because of its sudden and fast temperature changes. It can go between 19 degrees Celsius and 26 degrees during a working day. My objective with this project is to monitor the temperature and humidity in this room in order to analyze the temperature deviations and try to find a pattern to when and why this happens. I've added a distance sensor to this as well too in order to monitor if someone enters the room and specifically sits at the desk close to sensor. Number of people is a small factor that could affect the temperature, in this project I'll track one person. After using this setup, I believe I can get an idea or even an answer to why this happen and inform the building janitor in order to fix this problem.  

```
Describe why you have chosen to build this specific device. What purpose does it serve? What do you want to do with the data, and what new insights do you think it will give?
- [x] Why you chose the project
- [x] What purpose does it serve
- [x] What insights you think it will give
```

### Material


```
Explain all material that is needed. All sensors, where you bought them and their specifications. Please also provide pictures of what you have bought and what you are using.
- [x] List of material
- [x] What the different things (sensors, wires, controllers) do - short specifications
- [x] Where you bought them and how much they cost
>In this project I have chosen to work with the Pycom device as seen in Fig. 1, it's a neat little device programmed by MicroPython and has several bands of connectivity. The device has many digital and analog input and outputs and is well suited for an IoT project.

```

I've decided to choose work with the ESP32 device in this project see Fig 1. It is small and has Wi-Fi built in which will be used in this project. To this I've added a small temperature and humidity sensor see Fig 2, together with a distance sensor see Fig 3.

![image](https://user-images.githubusercontent.com/44947706/202860688-213a5af8-7c18-4d28-80f9-af5b62b98129.png)
>Fig. 1. ESP32 Microcontroller with Wi-Fi

![image](https://user-images.githubusercontent.com/44947706/202860707-0a8499ea-6664-4a50-acae-42cd58124e41.png)
>Fig. 2. Digital temperature and humidity sensor DHT11 (0\*C - 50\*C)

![image](https://user-images.githubusercontent.com/44947706/202860728-c3ccac67-ddfc-421f-8d99-2e3cc3d8aa6a.png)
>Fig. 3. Ultrasonic Sensor HC-SR04 (measuring range: 20 mm - 4 m and 15° measuring angle)

A list of the material that was used in this project, where it can be found to buy and its price.
| IoT Thing                | From                      | Price (SEK)|
| ---------                | ----------------          | ------ |
| ESP32 devkitc v4         |  [Amazon](https://www.amazon.se/AZDelivery-ESP32-NodeMCU-Development-Efterf%C3%B6ljarmodul/dp/B07Z83MF5W/ref=asc_df_B07Z83MF5W/?tag=shpngadsglede-21&linkCode=df0&hvadid=476551177109&hvpos=&hvnetw=g&hvrand=11855222708416699519&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9062355&hvtargid=pla-898234157885&psc=1)    | 125 kr    |
| Ultrasonic Sensor HC-SR04 | [Elfa](https://www.elfa.se/en/hc-sr04-ultrasonic-distance-sensor-5v-adafruit-3942/p/30139186?ext_cid=shgooaqsesv-Shopping-PerformanceMax-CSS&&cq_src=google_ads&cq_cmp=18208288444&cq_con=&cq_term=&cq_med=pla&cq_plac=&cq_net=x&cq_pos=&cq_plt=gp&gclsrc=aw.ds&gclid=Cj0KCQiA99ybBhD9ARIsALvZavXpKyaKploFa4YCGR7lEYw9_48EFfpWBXGeCyqkvJlPmJfkQlxNtf4aAglyEALw_wcB&gclsrc=aw.ds)  | 50 kr     |
| Digital temperature and humidity sensor DHT11 | [Electrokit](https://www.electrokit.com/en/product/digital-temperature-and-humidity-sensor-dht11/)         | 50 kr   |
| Jumper wires Male-Male |   [Electrokit](https://www.electrokit.com/en/product/jumper-wires-40-pin-30cm-male-male/)       |  50 kr  |
| Jumper wires Male-Female |    [Electrokit](https://www.electrokit.com/en/product/jumper-wires-40-pin-30cm-female-female-2/)       |  50 kr  |
| Bread board |    [Electrokit](https://www.electrokit.com/en/product/solderless-breadboard-400-tie-points/)      |  60 kr  |
| USB-cable A-male micro B male 15cm |    [Electrokit](https://www.electrokit.com/en/product/usb-kabel-a-hane-micro-b-hane-15cm/)     |  16 kr  |
| Power bank 10 000mA |  [Jula](https://www.jula.se/catalog/hem-och-hushall/hemelektronik/tillbehor-for-surfplattor-och-mobiler/batterier-och-powerbanks/powerbank-002630/)        |  200 kr   |
| Led Display (not necessary) | [Amazon](https://www.amazon.se/ZHITING-seriell-LED-displaymodul-hallon-Arduino/dp/B08GM1XW31/ref=sr_1_41?crid=WQT82A1ZSX6F&keywords=lcd+oled+display&qid=1668767941&sprefix=lcd+oled+display%2Caps%2C72&sr=8-41)          |   40 kr |

In total it will cost around 640 SEK. This can of course differ depending on how many you buy and where you buy it from. 


### Environment setup


```
How is the device programmed. Which IDE are you using. Describe all steps from flashing the firmware, installing plugins in your favorite editor. How flashing is done on MicroPython. The aim is that someone should be able to understand how to reproduce your project.

- [x] Chosen IDE         Thonny 
- [x] How the code is uploaded  ?? 
- [x] How is your project structured (important) ??? 
- [x] Steps that you needed to do for your computer. Installation of Node.js, extra drivers, etc.

```

I chose to write my code using the Thonny IDE, which is a beginner friendly python editor. I downloaded it from their webpage https://thonny.org/. My main file and the libraries I've used is uploaded on my [Github](https://github.com/divyakara/VM-IoT). I've one library for each sensor I have (temperature/humidity, distance and a OLED screen for debugging). I have one boot file which will boot up and connect the ESP32 to wifi then a main file which holds everything together.

Before flashing the firmware MicroPython on the ESP32, it is needed to install esptool.py and setuptools using Python. 
Write following code into your command prompt to install the requirements.
```
pip install esptool
pip install setuptools
python -m esptool
```
Now we can begin to download and flash the MicroPython Firmware on ESP32.
Connect your ESP32 to your computer using your usb cable, find and remember which COM port is used by opening the Device manager on Windows and see the COM port under "Ports". If Port is not detected you might only have a charging cable or you need to install USB drivers, in the ESP32 the CP2102 chip is used. Download the driver for CP2102 from the [Silicion Labs website](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers).

#### MicroPython
Download the latest version of MicroPython from [MicroPython webpage](https://micropython.org/download/#esp32).
Open the command prompt where the downloaded bin is located. Hold the BOOT/FLASH button while running this code in the prompt: 
```
python -m esptool –-chip esp32 erase_flash
```
Release the button after ""Erasing..." begins.
Now the erasing process is finished, and we need to flash the MicroPython Firmware with esptools.py

Now replace your COM port and bin file name to your name, hold the BOOT/FLASH button and run:
```
python -m esptool --chip esp32 --port COM3 write_flash -z 0x1000 esp32-20190113-v1.9.4-779-g5064df207.bin
```
Your ESP32  should now be flashed with MicroPython firmware.


#### InfluxDb
How to download Influx to Windows.
Go to https://docs.influxdata.com/influxdb/v2.0/install/?t=Windows and download latest version
Install by running following commands in PowerShell.

```
> Expand-Archive .\influxdb2-2.0.9-windows-amd64.zip -DestinationPath 'C:\Program Files\InfluxData\'
> mv 'C:\Program Files\InfluxData\influxdb2-2.0.9-windows-amd64' 'C:\Program Files\InfluxData\influxdb'
```
Start Influx 
```
> cd -Path 'C:\Program Files\InfluxData\influxdb'
> ./influxd
```

#### Node-RED
In order to install Node-RED you need to first download nodejs from their webpage: https://nodejs.org/en/
Then open a command prompt and enter 
```
>npm install -g --unsafe-perm node-red
```
Then run node-red by typing in the command prompt
```
>node-red start 
```
Go to http://localhost:1880/ (default) in your browser to start node-red.

#### Grafana
Download the Grafana installer from https://grafana.com/grafana/download?platform=windows and run it.
Go to the Grafana port http://localhost:3000/ (default)


### Putting everything together

How is all the electronics connected? Describe all the wiring, good if you can show a circuit diagram. Be specific on how to connect everything, and what to think of in terms of resistors, current and voltage. Is this only for a development setup or could it be used in production?

The ultrasonic sensor, temperature sensor is connected as follows:
![circuit (1)](https://user-images.githubusercontent.com/44947706/202500320-57a9241d-7576-4ee7-90d5-d1e47466bbea.png)

The ESP32 was supposed to be connected to a power bank which according to the manufacturer had a battery capacity of 10 000mAh. Doing some research on the internet it seems like when the Wi-Fi is used on the ESP32 it is active mode and draws around 240mA. The battery life for this setup can then be calculated as

$$ \text{Battery life (h)} = { \text{Battery capacity (mAh)} \over  \text{current (mA)} } $$

which gives approximately 

$$ {10 000 \over 240 }= 41 \text{ hours} $$ 

Making this calculation made me rethink. I thought it might be a bit too much to charge the power bank almost every other day and since the setup has some other alternative around its setup, I decided to not use the power bank. I will instead connect the ESP32 to a stationary computer we have in the room. If I would have gone with the battery I would have looked more into the deep sleep and see if I could have saved some energy there. I could have also transmitted the data less often to draw less power.

``` 
- [x] Circuit diagram (can be hand drawn)
- [x] Electrical calculations
- [ ] Limitations of hardware depending on design choices.
- [x] Discussion about a way forward - is it possible to scale?

``` 
### Platforms and infrastructure
``` 
Describe your choice of platform(s). You need to describe how the IoT-platform works, and also the reasoning and motivation about your choices. Have you developed your own platform, or used 

Is your platform based on a local installation or a cloud? Do you plan to use a paid subscription or a free? Describe the different alternatives on going forward if you want to scale your idea.

- [x] Describe platform in terms of functionality
- [x] Explain and elaborate what made you choose this platform
- [ ] Provide a pricing discussion. What are the prices for different platforms, and what are the pros and cons of using a low-code platform vs. developing yourself?

``` 


The end visualization of the data will be shown in Grafana. It is an opensource data visualization and data analytics solution, where you can create dashboards and customize how the data will be shown in different types of modules. I've heard about this platform before and was curious to try it out hence this choice.

I needed a database to save all my data into and checked into MySQL and InfluxDb. The choice fell on the database InfluxDb, which is easy to set up and handles large volumes of time series data better which I thought was preferable in this case. The data in InfluxDb will be saved there for 30 days and then be deleted, which is more than enough for this case. 

From the MQTT to the database Influx I use Node-RED which will act as a data bridge to capture and send the data from the MQTT to InfluxDb. An alternative to this would be the Telegraf, but since I'm a little familiar with Node-RED already I chose that instead. All the chosen tools are open source and free and which was also a reason to choose them.



### The code
```
Import core functions of your code here, and don't forget to explain what you have done. Do not put too much code here, focus on the core functionalities. Have you done a specific function that does a calculation, or are you using clever function for sending data on two networks? Or, are you checking if the value is reasonable etc. Explain what you have done, including the setup of the network, wireless, libraries and all that is needed to understand.
```

When the ESP32 is started up it will boot up and connect to the Wifi in the office using this function:
```
def connect_wifi(ssid, password):    
  
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

```

Then it will continue to the main.py file where it starts to import all necessary libraries. 

```python
from machine import Pin, I2C
import ssd1306
from hcsr04 import HCSR04
from time import sleep
import dht
import network
from umqtt.simple import MQTTClient
```

It will to begin to connect to our broker and define the topics that will be sent.

```python
#Broker
CLIENT_NAME = 'Office'
BROKER_ADDR = '172.16.2.7'
mqttc = MQTTClient(CLIENT_NAME, BROKER_ADDR, keepalive=60)
mqttc.connect()

#Topics
BTN_TOPIC_TEMP = CLIENT_NAME.encode() + b'/LMP/temp'
BTN_TOPIC_HUM = CLIENT_NAME.encode() + b'/LMP/humidity'
BTN_TOPIC_DIST = CLIENT_NAME.encode() + b'/LMP/distance'
```

Pins numbers are also defined according to the circuit diagram. The main loop I have that will run every second is as follows:

```python
graph = ""
timerCount = 0
while True:
  try:
    sleep(1)
    timerCount = timerCount + 1
    #read temp sensor
    temp, hum = read_tempsensor()

    #Read distance
    oled.fill(0)
    distance = sensorDist.distance_mm()
    print('Distance:', distance, 'mm')
    print('--------------------------')
    
    #Show text on display
    oled.text("Distance: " + str(distance) + " mm", 0, 15)
    oled.text("Temp: " + str(temp) + "'C", 0, 35)
    oled.text("Humidity: " + str(hum) + " %", 0, 55)
    oled.show()

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
```

As can be seen I send the distance data transmits every second this in order to capture if someone passes the distance sensor quite fast. The temperature however won't change that fast, so I don't want to send that data as often. Therefore, I've added a counter which makes it possible to send the temperature data every x seconds instead.
I started to send the temp data with a lot of time in between almost every 15 minutes. But then I noticed I didn't catch the temperature deviations if someone opens the window for example. Hence, I lowered it to every minute instead.

### The physical network layer

``` 
How is the data transmitted to the internet or local server? Describe the package format. All the different steps that are needed in getting the data to your end-point. Explain both the code and choice of wireless protocols.

- [x] How often is the data sent?   Every minute
- [x] Which wireless protocols did you use (WiFi, LoRa, etc ...)?       Wifi
- [x] Which transport protocols were used (MQTT, webhook, etc ...)      MQTT
- [ ] Elaborate on the design choices regarding data transmission and wireless protocols. That is how your choices affect the device range and battery consumption.
- [ ] What alternatives did you evaluate?
- [ ] What are the design limitations of your choices?

``` 


The data is transmitted to the office's local server using Wi-Fi every second for the distance measurements and every minute the temperature measurements are sent. The reason for using Wi-Fi is because it is very easily accessible from a room in the office. With Wi-Fi I'll only be able to use this setup in an area where Wi-Fi is connected, and in this case since I use it in office environment that is perfect for this case. I use MQTT (Message Queuing Telemetry Transport) which is often used to send the transport protocol to transmit data. To able to explore if data has been sent to the broker, I used MQTT explorer which was very helpful when troubleshooting.
![image](https://user-images.githubusercontent.com/44947706/202859355-e33d5a0e-7fde-48a5-8a01-119fd6b319e3.png)


The data flow will look like this:
![image](https://user-images.githubusercontent.com/44947706/202858909-a2e6aec2-31ff-4d2f-b8d3-75f2df89d22f.png)
>Fig. x. Data flow from sensors to visualization dashboard.





### Visualization and user interface
``` 
Describe the presentation part. How is the dashboard built? How long is the data preserved in the database?

- [x] Provide visual examples on how the visualization/UI looks. Pictures are needed.
- [x] How often is data saved in the database. What are the design choices?
- [x] Explain your choice of database. What kind of database. Motivate.
- [x] Automation/triggers of the data. Future
- [x] Alerting services. Are any used, what are the options and how are they in that case included. Future, email slack, discord....

``` 




In summary I'll subscribe data from my MQTT broker to Node-RED --> InfluxDb --> Grafana. Below follow steps on how to set it all up.


Create your database in InfluxDb. Go to Data-> Buckets and create a new bucket, mine is called nodered.
![image](https://user-images.githubusercontent.com/44947706/202447734-57032cb7-9555-45c3-8b52-59737c9295dd.png)

Then continue to the tab Tokens in Influx and click on the token called "{your username}'s Token" and copy the Token from there which we soon will paste into Node-RED.
![image](https://user-images.githubusercontent.com/44947706/202448171-0167b8cc-d63f-415c-a1a6-be37c75eb5ac.png)


Start Node-RED add a "MQTT in node", add your MQTT broker by entering server address port,
![image](https://user-images.githubusercontent.com/44947706/202446286-97d6c9da-cee3-4d72-90ff-4b84264a4fe3.png)
Then add the topic you want to subscribe to.
![image](https://user-images.githubusercontent.com/44947706/202446302-81ad4c73-6d21-4cd8-8fb0-fad6872a8eb2.png)

You should now be able to collect data from the broker, add a debug node to confirm that. After you receive data you want to save the data in a database in InfluxDb. Go to manage palette and install "node-red-contrib-influxdb" in order to get the InfluxDb nodes.

Add a "influxdb out" node and configure it as follows. In the server field add a new server, give it a name, choose version 2, enter the url of the influx http://localhost:8086. Paste the token that was copied from InfluxDb.

![image](https://user-images.githubusercontent.com/44947706/202449275-c6973afd-83f2-4d58-9540-d2f05cca0c67.png)

Continue to add your organization name, bucket name and give your measurement a name.
![image](https://user-images.githubusercontent.com/44947706/202449685-dc931f9b-2b57-4cb8-9c82-41b379be9206.png)

Deploy your changes in Node-RED.
![image](https://user-images.githubusercontent.com/44947706/202449911-bfb14dec-d638-4b8b-9567-54182c314be6.png)

In influx make sure you receive the data in your database. Go to explore, select your bucket, select measurements to display and value. Submit and you should see data visualized. 
![image](https://user-images.githubusercontent.com/44947706/202484636-694f5b03-1afc-42d4-afb9-f80797f54359.png)

Next step is to display this data in Grafana. Go to Grafana localhost:3000. configurations and add a data source. 
Name the data source, choose Query Language Flux, 
enter link to influx in url under HTTP. Under InfluxDb Details enter Organization, Token from Influx and bucket name. Save & test.

![image](https://user-images.githubusercontent.com/44947706/202486724-6baed792-dc9b-4ba8-ae11-495fbf22c00f.png)

Go to dashboards and create a new one in Grafana. Add a panel, and in the query you can paste code from Influx in order to input the right data to visualize. Simply select the data you want to visualize in InfluxDb, go to Script Editor, copy that code snippet and paste into Grafana query.
![image](https://user-images.githubusercontent.com/44947706/202489842-b8f8c291-1749-4620-b926-18aaf07496b3.png)



Final Grafana display 
![image](https://user-images.githubusercontent.com/44947706/202679499-663850ba-e8db-4fb1-9cde-bf54250b4f6c.png)


The in data will be saved to influx every second as the data is subscribed. 

The plan was to send an automatic alert notification when values exceeded the average. I started integrating to send an alert from Grafana to Discord, unfortunately I had trouble with that, and the time was not enough to make it work. That will be something to finish in the next step of this project. 
![image](https://user-images.githubusercontent.com/44947706/202859483-3ba52cf3-7d0a-4249-81cc-15421c94bc92.png)

It would have also been nice to add a trigger when the values deviate, such as turn a fan on when it gets too warm, or a heater when it gets too cold. This is something that can be developed in the future.



### Finalizing the design

``` 
Show the final results of your project. Give your final thoughts on how you think the project went. What could have been done in another way, or even better? Pictures are nice!

- [x] Show final results of the project
- [x] Pictures
- [ ] *Video presentation

``` 


Final result of the project:

![image](https://user-images.githubusercontent.com/44947706/202860541-f0f0dcdb-e21d-415f-a176-aa47e59a836a.png)

This has been a fun project to do, and I've learnt a lot from this. I wish I was able to put more time into this project than I was able to. I wanted to connect more sensors and make it more fun. It was bit disappointing that the alerting was not working in the end, that would have made the result much better. The setup could have been given a better case that could have been 3D printed for a stable setup. 



---

