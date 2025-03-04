<P align="center"> - <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> - <A HREF="https://github.com/WA9ONY">GitHub</A> - <BR>
- <A HREF="https://github.com/WA9ONY/Adafruit-Feather/tree/main">Adafruit Feather Projects</A> - 
</P>  

<p align="center">
       <img width="512" height="512" src="/Images/KiteAltimeterBanner.png">
</p>

# Kite Altimeter

The goal is to develop an altimeter that is attached to an 8' delta kite with 1,000 ft of kite line that is flown at Cannon Beach, Oregon.

Kite altimeter CircuitPython code is in Vxx directories at Adafruit-Feather/Kite-Altimeter/codeVxx.py.  

<HR>

# Kite Altimeter Testing

Altimeter Progress YouTube Videos
- [Altimeter Walk Test](https://youtube.com/shorts/cqNSkFrghns?si=oUt2FXK8ya5LukTG) YouTube
  - Observation:
    - Need to understand the pressure changes at the base position.
    - Need a smaller food container for the altimeter case.
    - Need to get the logging SD card working.

<HR>

# Kite Altimeter Hardware

Adafruit Feather System
- [Adafruit Feather RP2040](https://www.adafruit.com/product/4884)
- [Adafruit DPS310 Precision Barometric Pressure / Altitude Sensor](https://www.adafruit.com/product/4494)
- [STEMMA QT / Qwiic JST SH 4-Pin Cable - 50mm Long](https://www.adafruit.com/product/4399)
- [Adafruit FeatherWing OLED - 128x64](https://www.adafruit.com/product/4650)
- [Adalogger FeatherWing - RTC pcf8523 + SD ](https://www.adafruit.com/product/2922)
- [FeatherWing Tripler](https://www.adafruit.com/product/3417)
- [Adafruit Lithium Ion Polymer Battery with Short Cable - 3.7V 420mAh](https://www.adafruit.com/product/4236)
- {Adafruit_CircuitPython_MAX1704x GiyHub](https://github.com/adafruit/Adafruit_CircuitPython_MAX1704x/tree/main)

<HR>

# Development Tools

<p align="center">
       <img width="640" height="360" src="/Images/KAdev.jpeg">
</p>

Above image is a early photo of the the development system for creating a kite altimeter.

Software tools
- Raspberry Pi 500 Rev 1.0 computer
- OS: Debian GNU/Linux 12 (bookworm) aarch64 
- Thonny IDE Version 4.1.4 Comes with Raspberry OS install. https://thonny.org/
- Circup (for managing CircuitPython libraries) https://github.com/adafruit/circup
- Circup is a Terminal CLI tool

<HR>

# Altimeter Research

YouTube
- [17 | Measure altitude with the BMP280 barometric sensor](https://youtu.be/rabWc5W84ug?si=DWZH9ALgdRfxRoQ3)
  - Nice graph showing sensor noise problem
  - [Carbon Aeronautics](https://github.com/CarbonAeronautics)
  - [Part XVII: Measure altitude with the BMP280 barometer](https://github.com/CarbonAeronautics/Part-XVII-MeasureAltitude)
- [Arduino Uno R4 WiFi LESSON 56: Measure Altitude with an Arduino and BMP180 Project](https://youtu.be/dBZQhYCuCEY?si=91WeISXrhJqAhRd6)
  - Great tutorial on using a LF to reduce BMP180 noise.
- []()
- []()
- []()
- 


<HR>

# Note

Read Only Filesystem problem
- Thonny Shell
- import storage
- storage.erase_filesystem()



<HR>

# Data Logging Note

Update and install boot.py
- Thonny Shell

A digital input is used for CircuitPython or Ciomputer writes to RP2040 built-in memory.
- D5 example default
  - D5 is used OLE 128x64 bush button


Process to start logging
- Close editors, Thonny
- Unmount Feather RP2040 from computer
- Unplug Feather RP2040 from computer
- Close the Feather RP2040 Dx swith to ground
- Turn on the Feather RP2040 with battery
- Check Feather RP2040 LED for logging status.
  - 1 second flashes writing to memory
  - 0.25 or 2 second flashes error
- When done logging power of Feather RP2040 by disconnecting the battery.

Process to check logging file
- Feather RP2040 is off
- Open the Feather RP2040 Dx swith to ground
- Plug the Feather RP2040 USB into the computer
- Computer Removable medium is inserted, OK
- datalog.txt is listed if things worked correctly.
- Copy datalog.txt to computer.
- Delete datalog.txt on Feather RP2040
- If needed open Text Editor to update code.py
