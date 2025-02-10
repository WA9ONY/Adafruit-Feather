<P align="center"> - <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> - <A HREF="https://github.com/WA9ONY">GitHub</A> -<BR>
- <A HREF="https://github.com/WA9ONY/Adafruit-Feather/blob/main/Feather-RP2040/README.md">Adafruit Feather RP2040 Index</A> - 
</P>  

<p align="center">
       <img width="512" height="512" src="/Images/FeatherProjects.png">
</p>

# Adafruit Feather Projects

### **Overview of the Adafruit Feather and FeatherWing Product Line**

[Adafruit’s](https://www.adafruit.com/) **Feather and FeatherWing** ecosystem is a modular, compact, and extensible platform for embedded systems development. The **Feather** boards serve as microcontroller development boards, while **FeatherWings** are add-on boards that expand their functionality. 

Adafruit Feather ecosystem is extensive with great 
- [Broad product line](https://www.adafruit.com/category/943)
- [Documentation](https://learn.adafruit.com/adafruit-feather-rp2040-pico)
- [Videos](https://www.youtube.com/@adafruit/videos)  & [Live](https://www.youtube.com/@adafruit/streams)
  - Sun. 9:30am PST Desk of Ladyada, The Great Search
  - Mon. 11am PST on  CircuitPython Weekly Meeting
  - Tue. JP’s Product Pick of the Week
  - Wed. NewProducts
  - Wed. Live ASK AN ENGINEER
  - Wed. 4:30pm PST Live SHOW and TELL
  - Thr. 9pm PST Live JOHN PARK'S WORKSHOP LIVE
  - Fri. 2pm PST Live Deep Dive w/Scott
    - Discord Adafruit # live-broadcast-chat
  - EYE on NPI
  - Adafruit Top Secret
  - Tutorial:
  - John Park's CircuitPython Parsec
- [CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython)
- [GitHub software libraries](https://github.com/adafruit)
- [Learning system](https://learn.adafruit.com/)
- [Discord group](https://discord.com/channels/327254708534116352/330410763594498050)
- [The CircuitPython Show](https://www.circuitpythonshow.com/@circuitpythonshow)
  - An independent podcast with the people in and around CircuitPython. Created and hosted by Paul Cutler.
- [Blog](https://blog.adafruit.com/page/2/)
- etc.

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
  - [GitHub Adafruit_CircuitPython_Bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle)
  - [CircuitPython 9.2.4 for Adafruit Feather RP2040 as of Feb. 3, 2025](https://circuitpython.org/board/adafruit_feather_rp2040/)
  - [Libraries](https://circuitpython.org/libraries)
  - [Examples code](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/tag/20250205) >340 product, >1,400 Circuitpython example files as of February 05, 2025
  - [Community libraries](https://circuitpython.org/libraries)
  - [CircuitPython 2025](https://www.youtube.com/watch?v=klyVOe_1nUA)

 Adafruit
- [CircuitPython Made Easy on Circuit Playground Express and Bluefruit](https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/play-file)
- [John Park's CircuitPython Parsec](https://www.youtube.com/playlist?list=PLjF7R1fz_OOWFqZfqW9jlvQSIUmwn9lWr)

YouTube Tutorials and Lessions
-  [Circuit Python Tutorials](https://www.youtube.com/playlist?list=PL9VJ9OpT-IPSsQUWqQcNrVJqy4LhBjPX2) by Prof. John Gallaugher
  -  [Build With Prof. G](https://www.youtube.com/channel/UCY3yzXkS1vcqxN_RqKU17pg)
  -  [Prof. John Gallaugher](https://www.youtube.com/profgallaugher)
  -  [https://gallaugher.com/](https://gallaugher.com/)

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


<HR>

<p align="center">
       <img width="103" height="113" src="/Images/I2C_bus_logo.png">
</p>

# 10. I2C Bus

Hello everyone! Today, we’ll be diving into an overview of the [I2C (Inter-Integrated Circuit)](https://en.wikipedia.org/wiki/I%C2%B2C) bus—a fundamental communication protocol used extensively in embedded systems and electronics. Understanding I2C is crucial because it’s one of the most popular ways to connect microcontrollers with sensors, memory devices, and other peripherals in both hobbyist and industrial applications.

---

## 1. What Is I2C?

**I2C Overview:**
- **Definition:** I2C is a synchronous, multi-master, multi-slave, packet-switched, single-ended, serial communication bus.
- **Developer:** It was originally developed by Philips Semiconductor (now NXP) in the early 1980s.
- **Primary Use:** It allows multiple integrated circuits to communicate over just two wires, making it an ideal choice for connecting various low-speed peripheral devices to a microcontroller or processor.

---

## 2. Physical Layer

**Two-Wire Interface:**
- **SDA (Serial Data Line):** This line carries the data.
- **SCL (Serial Clock Line):** This line carries the clock signal generated by the master device to synchronize data transmission.

**Electrical Characteristics:**
- **Open-Drain Configuration:** Both SDA and SCL are typically implemented as open-drain (or open-collector) lines. This means that devices can only pull the line low; when they release it, the line goes high due to external pull-up resistors.
- **Pull-Up Resistors:** These resistors are essential because they ensure that the lines are at a known high level when no device is pulling them low. The values of these resistors are chosen based on factors like bus capacitance and desired speed.

---

## 3. Communication Protocol

**Master-Slave Architecture:**
- **Master Device:** Initiates communication, generates the clock signal, and controls the data flow.
- **Slave Devices:** Respond to commands from the master. Each slave has a unique address (typically 7-bit, though 10-bit addressing is also available).

**Basic Communication Flow:**
1. **Start Condition:** Communication begins when the master pulls SDA low while SCL is high. This signals all devices on the bus to listen.
2. **Address Frame:** The master sends out a unique address (7 or 10 bits) followed by a read/write bit to indicate the direction of data transfer.
3. **Data Transfer:** Data is sent in 8-bit bytes. After each byte, the receiver must send an acknowledgment bit (ACK) by pulling SDA low during the ninth clock pulse.
4. **Stop Condition:** Communication ends when the master releases SDA to high while SCL remains high.

**Additional Concepts:**
- **Repeated Start Condition:** Sometimes, the master may need to initiate another communication without releasing the bus. It does so by issuing another start condition instead of a stop condition.
- **Clock Stretching:** A slave device can hold the clock line low to delay the master if it needs more time to process data. This feature ensures reliable communication even if the slave is momentarily busy.

---

## 4. Bus Speeds and Modes

I2C supports several speed modes:
- **Standard Mode:** Up to 100 kbit/s
- **Fast Mode:** Up to 400 kbit/s
- **Fast-Mode Plus:** Up to 1 Mbit/s
- **High-Speed Mode:** Up to 3.4 Mbit/s

Each mode has specific requirements for timing and pull-up resistor values to ensure reliable operation.

---

## 5. Advantages and Applications

**Advantages:**
- **Simplicity:** Only two wires are required, which minimizes PCB complexity.
- **Multi-Device Support:** Multiple devices can share the same bus without complex wiring.
- **Low Cost:** Fewer pins and simpler wiring contribute to cost-effective design.

**Common Applications:**
- **Sensor Networks:** Connecting temperature sensors, accelerometers, and other devices.
- **EEPROM Access:** Reading from and writing to non-volatile memory.
- **Display Drivers:** Communicating with LCDs or LED displays.
- **Embedded System Peripherals:** ADCs, DACs, and other modules in microcontroller systems.

---

## 6. Practical Considerations in Design

**Design Tips:**
- **Choose Appropriate Pull-Up Resistors:** The resistor values must be calculated based on bus capacitance and desired speed. Too high a resistance might lead to slow rise times, while too low a resistance could increase power consumption.
- **Bus Length and Capacitance:** Keep the bus as short as possible to minimize capacitance, which can adversely affect signal integrity.
- **Handling Bus Contention:** In multi-master systems, be aware of arbitration procedures that help determine which master takes control when two devices attempt to communicate simultaneously.

---

## 7. Laboratory Applications

In upcoming labs, you will have hands-on experiences with I2C communication. Here are a few lab activities you might expect:

- **Lab 1: I2C Bus Setup and Communication**
  - **Objective:** Set up a basic I2C bus on a breadboard using a microcontroller.
  - **Activities:** Connect a sensor or an EEPROM via I2C, configure the microcontroller’s I2C peripheral, and implement a simple read/write routine.
  
- **Lab 2: Analyzing I2C Signals**
  - **Objective:** Use an oscilloscope or logic analyzer to observe I2C communication.
  - **Activities:** Capture start/stop conditions, analyze the timing of data and clock signals, and identify ACK/NACK sequences.
  
- **Lab 3: Multi-Device I2C Bus**
  - **Objective:** Interface multiple I2C devices on a single bus and manage address conflicts.
  - **Activities:** Learn about address assignment, implement proper pull-up resistor strategies, and experiment with clock stretching if applicable.

---

## Conclusion

The I2C bus is a powerful and versatile communication protocol that plays a key role in modern electronic systems. By understanding its physical layer, communication protocol, and design considerations, you will be better prepared to implement and troubleshoot I2C in your projects. In our subsequent lectures and labs, we’ll build on this foundation by exploring real-world applications and hands-on circuit design.

Feel free to ask questions if any part of the I2C protocol isn’t clear, or if you’d like more detailed examples of its implementation!

I2C (Inter-Integrated Circuit) bus [Adafruit address list](https://learn.adafruit.com/i2c-addresses/the-list).

Adafruit_CircuitPython_DisplayIO_SH1107 0x3C
[DPS310 Barometric Sensor](https://adafru.it/RKd) 0x76 or 0x77
PCF8523 RTC (0x68 only) (https://adafru.it/sd5)
https://www.adafruit.com/product/3295


<HR>

<p align="center">
       <img width="103" height="113" src="/Images/I2C_bus_logo.png">
</p>

# 11. Circup

[Circup](https://github.com/adafruit/circup)

[Use circup to easily keep your CircuitPython libraries up to date](https://learn.adafruit.com/keep-your-circuitpython-libraries-on-devices-up-to-date-with-circup/install-command)



Coxxect
[Blog](https://coxxect.blogspot.com/)
[YouTube](https://www.youtube.com/@coxxect)
