<P align="center"> - <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> -<BR>
- <A HREF="https://github.com/WA9ONY">GitHub WA9ONY</A>: 
<A HREF="https://github.com/WA9ONY/Adafruit-Feather/blob/main/Feather-RP2040/README.md">Adafruit Feather RP2040</A> - 
</P>  

<p align="center">
       <img width="512" height="512" src="/Images/FeatherProjects.png">
</p>

# Adafruit-Feather Projects

### **Overview of the Adafruit Feather and FeatherWing Product Line**

Adafruit’s **[Feather and FeatherWing](https://www.adafruit.com/category/943)** ecosystem is a modular, compact, and extensible platform for embedded systems development. The **Feather** boards serve as microcontroller development boards, while **FeatherWings** are add-on boards that expand their functionality. Adafruit Feather ecosystem is extensive with great documentation, [videos](https://www.youtube.com/@adafruit), software libraries, learning guides, [Discord group](https://discord.com/channels/327254708534116352/330410763594498050), etc.

---

## **1. Adafruit Feather: The Core [Boards](https://www.adafruit.com/category/946)**
Feathers are small, lightweight microcontroller boards designed for prototyping and embedded systems. They share a **standard form factor** (2.0" x 0.9") and **pinout**, making them interchangeable. 

### **Feather Categories**
1. **Microcontroller-Based Feathers**  
   - Feature an onboard microcontroller (e.g., ATmega32u4, ESP32, RP2040).
   - Designed for general-purpose embedded computing.

2. **Wireless Feathers**  
   - Include built-in **Wi-Fi, Bluetooth, LoRa, or Cellular** connectivity.
   - Popular models:
     - ESP32-S3 Feather (Wi-Fi + BLE)
     - Feather nRF52840 (Bluetooth)
     - Feather M0 LoRa (LoRaWAN)
     - Feather FONA (Cellular)

3. **SAMD, M4, and RP2040 Feathers**  
   - Use more powerful ARM Cortex-M chips or Raspberry Pi’s RP2040.
   - Suitable for **IoT, robotics, and edge computing**.

4. **Battery & Low Power Feathers**  
   - All Feather boards support **LiPo battery charging** via USB.
   - Many include **deep sleep modes** for battery efficiency.

---

## **2. Adafruit [FeatherWing](https://www.adafruit.com/category/945): Expansion Modules**
FeatherWings attach to Feathers and provide additional features. These include **displays, sensors, relays, motor drivers, GPS, and communication interfaces**.

### **Types of FeatherWings**
1. **Display & UI**
   - OLED FeatherWing (128x64 monochrome)
   - 7-Segment Display FeatherWing
   - TFT FeatherWing (Color LCD)

2. **Sensors**
   - ADXL345 3-axis Accelerometer FeatherWing
   - AirLift FeatherWing (Wi-Fi co-processor)

3. **Motor & Robotics**
   - DC Motor FeatherWing (for robotics)
   - Stepper Motor FeatherWing
   - Servo FeatherWing (16-channel PWM)

4. **Storage & Communication**
   - LoRa Radio FeatherWing
   - Ethernet FeatherWing
   - CAN Bus FeatherWing

5. **Power & Connectivity**
   - Power Relay FeatherWing
   - Ethernet + PoE FeatherWing
   - Wireless Charging FeatherWing

---

## **3. Why Use Feathers and FeatherWings?**
- **Standardized pinout** → Easy swapping of Feathers.
- **Compact & portable** → Great for IoT and wearable projects.
- **Battery support** → LiPo charging built-in.
- **Modular ecosystem** → Stackable FeatherWings.

---

## **4. Feather Ecosystem in Action**
- **IoT Sensor Node**: ESP32 Feather + LoRa FeatherWing + GPS.
- **Portable Game Console**: RP2040 Feather + TFT FeatherWing + Battery.
- **Weather Station**: Feather M4 + Sensor FeatherWing + Wi-Fi FeatherWing.

<HR>
<HR>
  
## 5. Project 1 Data Logger

<A HREF="https://github.com/WA9ONY/Adafruit-Feather/blob/main/Feather-RP2040/README.md">Adafruit Feather RP2040</A>

Data logger to attached to a kit.

- Log sequence number
- Log elapse time since turn on
- Log temp
- Log voltage
- NeoPixel color flash indicates PWS voltage.
- Log to Data.CSV file
- Flash LED during write to file as proof of life
- Check if Data.CSV file exist.
- Check available memory for Data.CSV file.
- Look into different ways to do time loops
- I2C sensor DPS310
- Sleep mode

<HR>

<p align="center">
       <img width="500" height="281" src="/Images/FeatherRP2040a.PNG">
</p>
  
## 6. Hardware

[Adafruit Feather RP2040](https://www.adafruit.com/product/4884)
- Product ID: 4884
- Old verson Bootsel switch faces up.
- New version Bootsel switch faces out the side and the switch can be used by the user program.
- [Desk of Ladyada - RP2040 Feather prepares to take flight!](https://www.youtube.com/watch?v=qkN2TXqj59M)
  - Pin layout, SWD pads, NeoPixel swirl test, 8 MB 
- [Introducing Adafruit Feather RP2040](https://learn.adafruit.com/adafruit-feather-rp2040-pico)
- [What Is Feather?](https://youtu.be/W9jjgKaE1_k?si=ynulODlL1M82y7RH)

<p align="center">
       <img width="500" height="348" src="/Images/DPS310.PNG">
</p>


[Adafruit DPS310 Precision Barometric Pressure / Altitude Sensor - STEMMA QT / Qwiic](https://www.adafruit.com/product/4494)
-  Product ID: 4494

[Adafruit STEMMA QT / Qwiic JST SH 4-pin Cable](https://www.adafruit.com/product/4210)

[Adafruit Lithium Ion Polymer Battery with Short Cable - 3.7V 420mAh](https://www.adafruit.com/product/4236)


<HR>

<p align="center">
       <img width="138" height="146" src="/Images/Adafruit_blinkaS.png">
</p>

# 7. Software

- [CircuitPython](https://circuitpython.org/)
  - [CircuitPython 9.2.4 for Adafruit Feather RP2040 as of Feb. 3, 2025](https://circuitpython.org/board/adafruit_feather_rp2040/)
  - [Libraries](https://circuitpython.org/libraries)

 Adafruit
- [CircuitPython Made Easy on Circuit Playground Express and Bluefruit](https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/play-file)
- [John Park's CircuitPython Parsec](https://www.youtube.com/playlist?list=PLjF7R1fz_OOWFqZfqW9jlvQSIUmwn9lWr)

YouTube Tutorials and Lessions
-  [Circuit Python Tutorials](https://www.youtube.com/playlist?list=PL9VJ9OpT-IPSsQUWqQcNrVJqy4LhBjPX2) by Prof. John Gallaugher
  -  [Build With Prof. G](https://www.youtube.com/channel/UCY3yzXkS1vcqxN_RqKU17pg)
  -  [Prof. John Gallaugher](https://www.youtube.com/profgallaugher)

- [Paul McWhorter playlist oof lessions](https://www.youtube.com/@paulmcwhorter/playlists)
  - [Raspberry Pi Pico W Lessons for Absolute](https://www.youtube.com/playlist?list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5)


<HR>

<p align="center">
       <img width="600" height="338" src="/Images/P500.PNG">
</p>

# 8. Development Tools

- [Raspberry Pi P500](https://www.raspberrypi.com/products/raspberry-pi-500/) running [Raspberry Pi OS 64-bit](https://www.raspberrypi.com/software/)
  - Help > Bookshelf > Books > Get Started with MicroPython on Raspberry Pi Pico
    - Free 139 page book on MicroPython and the Raspberry Pi Pico (RP2040)
- [Mu editor V1.0.3](https://codewith.mu/)



<HR>

<p align="center">
       <img width="295" height="80" src="/Images/OpenAI_LogoS.png">
</p>

# 9. AI Tools

As of Feb. 4, 2025 [OpenAI](https://en.wikipedia.org/wiki/OpenAI)  [ChatGPT o3-mini-high](https://en.wikipedia.org/wiki/OpenAI_o3) is used to:
- Research hardware operation
- Research software techniques
- Create CircuitPython code
- etc.
The world of AI is moving fast and in a few months there will be better AI coding models.

- [OpenAI](https://openai.com/) ChatGPT o3-mini-high
