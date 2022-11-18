# VM-IoT Title?

Divya Kara 

## Project report - IoT report template 

###### tags: `IoT` `MQTT` `MicroPython` `ESP32` 
---
**Table of Contents**


[TOC]

## How to write your report

We have chosen to streamline your assignment as a tutorial, written in the Markdown language using a standard template (below). The main reason behind this is to make it as simple as possible, still flexible and easy to share between all classmates and other peers.

The report should be available on a public Github repository.

```
Information want's to be free - let's keep everything open, shall we?
```

## Github
https://github.com/divyakara/VM-IoT/edit/main/README.md



## Some examples for inspiration

**Note these are from the basic courses.**

Check out this link: [Good examples from previous summer courses](https://hackmd.io/@lnu-iot/good-examples)

----

Some additional examples for inspiration.

- [GPS Car tracker with notification](https://www.instructables.com/id/GPS-Car-Tracker-With-SMS-Notification-and-Thingspe/)
- [Blynk style button](https://www.instructables.com/id/Arduino-Tutorial-BLYNK-Style-Button-and-ESP-01-Rel/)
- [IoT weather station](https://www.hackster.io/rijk_meurs/iot-weather-station-4c29c6)
- [Mini IoT weather station](https://www.hackster.io/FunguyPro/how-to-make-an-mini-iot-weather-station-58252d)
- [Distance sensor](https://community.mydevices.com/t/nodemcu-esp8266-hc-sr04/2872)

---

# Template

**Please keep the total length of the report below 40k characters.** You can include code that is linked to a repository. Keep the code snippets in the report short, and rather link to relevant sections in the repository. The code snippets should only be relevant for explaining on a higher level.

## Tutorial on how to build a temperature and humidity sensor

Give a short and brief overview of what your project is about.
What needs to be included:

- [ ] Title
- [ ] Your name and student credentials (xx666xxx)
- [ ] Short project overview
- [ ] How much time it might take to do (an approximation)

### Objectives
In the office I'm working at the temperature in a room has been a big discussion because of its sudden and fast temperature changes. It can go between 19 degrees celcius and 26 degrees during a working day. My objective with this project is to monitor the temperature and humidity in this room in order to analyze the temperature deviations and try to find a pattern to when and why this happen. I've added a distance sensor to this as well too in order to monitor if someone enters the room and specifically sits at the desk close to sensor. Number of people is a small factor that could affect the temperature, in this project I'll track one person. After using this setup I believe I can get an idea or even an answer to why this happen and inform the building janitor in order to fix this problem.  

Describe why you have chosen to build this specific device. What purpose does it serve? What do you want to do with the data, and what new insights do you think it will give?

- [x] Why you chose the project
- [x] What purpose does it serve
- [x] What insights you think it will give

### Material

Explain all material that is needed. All sensors, where you bought them and their specifications. Please also provide pictures of what you have bought and what you are using.
- [x] List of material
- [x] What the different things (sensors, wires, controllers) do - short specifications
- [x] Where you bought them and how much they cost
>In this project I have chosen to work with the Pycom device as seen in Fig. 1, it's a neat little device programmed by MicroPython and has several bands of connectivity. The device has many digital and analog input and outputs and is well suited for an IoT project.


I've decided to choose work with the ESP32 device in this project see Fig 1. It is small and has wifi built in which will be used in this project. To this I've added a small temperature and humidity sensor see Fig 2, together with a distance sensor see Fig 3.

![image](https://user-images.githubusercontent.com/44947706/202709160-c246adc9-8e1e-4779-ad5d-285a698b9827.png)
>Fig. 1. ESP32 Microcontroller with Wifi

![image](https://user-images.githubusercontent.com/44947706/202709279-e22d8ad0-b8fb-40d2-aced-34e718114988.png)
>Fig. 2. Digital temperature and humidity sensor DHT11 (0\*C - 50\*C)

![image](https://user-images.githubusercontent.com/44947706/202708805-e113e7b7-af84-475d-b14b-845855a76a41.png)
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
| Powerbank 10 000mA |  [Jula](https://www.jula.se/catalog/hem-och-hushall/hemelektronik/tillbehor-for-surfplattor-och-mobiler/batterier-och-powerbanks/powerbank-002630/)        |  200 kr   |
| Led Display (not necessary) | [Amazon](https://www.amazon.se/ZHITING-seriell-LED-displaymodul-hallon-Arduino/dp/B08GM1XW31/ref=sr_1_41?crid=WQT82A1ZSX6F&keywords=lcd+oled+display&qid=1668767941&sprefix=lcd+oled+display%2Caps%2C72&sr=8-41)          |   40 kr |

In total it will cost around 640 SEK. This can of course differ depending on how many you buy and where you buy it from. 


### Environment setup

How is the device programmed. Which IDE are you using. Describe all steps from flashing the firmware, installing plugins in your favorite editor. How flashing is done on MicroPython. The aim is that someone should be able to understand how to reproduce your project.

- [ ] Chosen IDE         Thonny 
- [ ] How the code is uploaded  ?? 
- [ ] How is your project structured (important) ??? 
- [ ] Steps that you needed to do for your computer. Installation of Node.js, extra drivers, etc.

I chose the IDE Thonny which was downloaded from their webpage https://thonny.org/.

Before flashing the firmware MicroPython on the ESP32, it is needed to install esptool.py and setuptools using Python. 
Write following code into your command prompt to install the requirements.
```
pip install esptool
pip install setuptools
python -m esptool
```
Now we can begin to download and flash the MicroPython Firmware on ESP32.
Connect your ESP32 to your copmputer using your usb cable, find and remember which COM port is used by opening the Device manager on Windows and see the COM port under "Ports". If Port is not detected you might only have a charging cable or you need to install USB drivers, in the ESP32 the CP2102 chip is used. Download the driver for CP2102 from the [Silicion Labs website](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers).

#### MicroPython
Download the latest version of MicroPython from [MicroPython webpage](https://micropython.org/download/#esp32).
Open the command prompt where the downloaded bin is located. Hold the BOOT/FLASH button while running this code in the prompt: 
```
python -m esptool –-chip esp32 erase_flash
```
Release the button after ""Erasing..." begins.
Now the erasing process is finished and we need to flash the MicroPython Firmware with esptools.py

Now replace your COM port and bin file name to your name, hold the BOOT/FLASH button and run:
```
python -m esptool --chip esp32 --port COM3 write_flash -z 0x1000 esp32-20190113-v1.9.4-779-g5064df207.bin
```
Your ESP32  should now be flashed with Micropython firmware.


#### InfluxDb
How to download Influx to Windows.
Go to https://docs.influxdata.com/influxdb/v2.0/install/?t=Windows and download latest veresion
Install by running following commands in Powershell.

```
> Expand-Archive .\influxdb2-2.0.9-windows-amd64.zip -DestinationPath 'C:\Program Files\InfluxData\'
> mv 'C:\Program Files\InfluxData\influxdb2-2.0.9-windows-amd64' 'C:\Program Files\InfluxData\influxdb'
```
Start Influx 
```
> cd -Path 'C:\Program Files\InfluxData\influxdb'
> ./influxd
```

#### Nodered
In order to install Nodered you need to first download nodejs from their webpage: https://nodejs.org/en/
Then open a command prompt and enter 
```
npm install -g --unsafe-perm node-red
```
Then run node-red by typing in the command prompt
```
node-red start 
```
Go to http://localhost:1880/ (default) in your browser to start node-red.

#### Grafana
Download the Grafana installer from https://grafana.com/grafana/download?platform=windows and run it.
Go to the Grafana port http://localhost:3000/ (default)


### Putting everything together

How is all the electronics connected? Describe all the wiring, good if you can show a circuit diagram. Be specific on how to connect everything, and what to think of in terms of resistors, current and voltage. Is this only for a development setup or could it be used in production?
![circuit (1)](https://user-images.githubusercontent.com/44947706/202500320-57a9241d-7576-4ee7-90d5-d1e47466bbea.png)

- [ ] Circuit diagram (can be hand drawn)
- [ ] Electrical calculations
- [ ] Limitations of hardware depending on design choices.
- [ ] Discussion about a way forward - is it possible to scale?

### Platforms and infrastructure
ESP32

Describe your choice of platform(s). You need to describe how the IoT-platform works, and also the reasoning and motivation about your choices. Have you developed your own platform, or used 

Is your platform based on a local installation or a cloud? Do you plan to use a paid subscription or a free? Describe the different alternatives on going forward if you want to scale your idea.

- [ ] Describe platform in terms of functionality
- [ ] Explain and elaborate what made you choose this platform
- [ ] Provide a pricing discussion. What are the prices for different platforms, and what are the pros and cons of using a low-code platform vs. developing yourself?

### The code

Import core functions of your code here, and don't forget to explain what you have done. Do not put too much code here, focus on the core functionalities. Have you done a specific function that does a calculation, or are you using clever function for sending data on two networks? Or, are you checking if the value is reasonable etc. Explain what you have done, including the setup of the network, wireless, libraries and all that is needed to understand.


```python=
import this as that

def my_cool_function():
    print('not much here')

s.send(package)

# Explain your code!
```

### The physical network layer

How is the data transmitted to the internet or local server? Describe the package format. All the different steps that are needed in getting the data to your end-point. Explain both the code and choice of wireless protocols.

- [ ] How often is the data sent?   Every minute
- [ ] Which wireless protocols did you use (WiFi, LoRa, etc ...)?       Wifi
- [ ] Which transport protocols were used (MQTT, webhook, etc ...)      MQTT
- [ ] Elaborate on the design choices regarding data transmission and wireless protocols. That is how your choices affect the device range and battery consumption.
- [ ] What alternatives did you evaluate?
- [ ] What are the design limitations of your choices?







### Visualisation and user interface
I will vizulize my data on Grafana. Grafana is opensource data visualizition create dashboard and so on.
To do so I will send data from my MQTT broker to NodeRed--> InfluxDb --> Grafana
Influx is an open source database where I 'll save my data. Install NodeRed, InfluxDb and Grafana as explained in the setup chapter.


Create your database in influxdb. Go to Data-> Buckets and create a new bucke, mine is called nodered.
![image](https://user-images.githubusercontent.com/44947706/202447734-57032cb7-9555-45c3-8b52-59737c9295dd.png)

Then continue to the tab Tokens in Influx and click on the token called "{your username}'s Token" and copy the Token from there which we soon will paste into nodered.
![image](https://user-images.githubusercontent.com/44947706/202448171-0167b8cc-d63f-415c-a1a6-be37c75eb5ac.png)


Start NodeRed add a "MQTT in node", add your MQTT broker by entering server adress port,
![image](https://user-images.githubusercontent.com/44947706/202446286-97d6c9da-cee3-4d72-90ff-4b84264a4fe3.png)
Then add the topic you wnat to subscribe to.
![image](https://user-images.githubusercontent.com/44947706/202446302-81ad4c73-6d21-4cd8-8fb0-fad6872a8eb2.png)

You should now be able to collect data from the brooker, add a debug node to confirm that. After you recevie data you want to save the data in a database in influx.Go to manage palette and install "node-red-contrib-influxdb" in order to get the influxdb nodes.

Add a "influxdb out" node and configure it as follows. In the server field add a new server, give it a name, choose version 2, enter the url of the influx http://localhost:8086. Paste the token that was copied from influxdb.

![image](https://user-images.githubusercontent.com/44947706/202449275-c6973afd-83f2-4d58-9540-d2f05cca0c67.png)

Continue to add your Organization name, bucketname and give your measurement a name.
![image](https://user-images.githubusercontent.com/44947706/202449685-dc931f9b-2b57-4cb8-9c82-41b379be9206.png)

Deploy your changes in nodered.
![image](https://user-images.githubusercontent.com/44947706/202449911-bfb14dec-d638-4b8b-9567-54182c314be6.png)

In influx make sure you receive the data in your database. Go to explore, select your bucket, select measurements to display and value. Submit and you should see data visulized. 
![image](https://user-images.githubusercontent.com/44947706/202484636-694f5b03-1afc-42d4-afb9-f80797f54359.png)

Next step is to display this data in Grafana. Go to grafana localhost:3000. configurations and add a datasource. 
Name the datasource, choose Query Language Flux, 
enter link to influx in url under HTTP. Under InfluxDB Details enter Organization, Token from Influx and bucketname. Save & test.

![image](https://user-images.githubusercontent.com/44947706/202486724-6baed792-dc9b-4ba8-ae11-495fbf22c00f.png)

Go to dashboards and create a new one in Grafana. Add a panel, and in the query you can paste code from Influx in order to input the right data to vizulize. Simply select the data you want to vizulize in Influxdb, go to Script Editor, copy that codesnippet and paste into Grafana query.
![image](https://user-images.githubusercontent.com/44947706/202489842-b8f8c291-1749-4620-b926-18aaf07496b3.png)



Final Grafana display 
![image](https://user-images.githubusercontent.com/44947706/202679499-663850ba-e8db-4fb1-9cde-bf54250b4f6c.png)



Describe the presentation part. How is the dashboard built? How long is the data preserved in the database?

- [x] Provide visual examples on how the visualisation/UI looks. Pictures are needed.
- [ ] How often is data saved in the database. What are the design choices?
- [ ] Explain your choice of database. What kind of database. Motivate.
- [ ] Automation/triggers of the data. Future
- [ ] Alerting services. Are any used, what are the options and how are they in that case included. Future, email slack, discord....

### Finalizing the design

Show the final results of your project. Give your final thoughts on how you think the project went. What could have been done in an other way, or even better? Pictures are nice!

- [ ] Show final results of the project
- [ ] Pictures
- [ ] *Video presentation

---

