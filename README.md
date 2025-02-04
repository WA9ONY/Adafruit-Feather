<P align="center"> - <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> -<BR>
- <A HREF="https://github.com/WA9ONY">GitHub WA9ONY</A>: 
<A HREF="https://github.com/WA9ONY/Adafruit-Feather/blob/main/Feather-RP2040/README.md">Adafruit Feather RP2040</A> - 
</P>  

<p align="center">
       <img width="512" height="512" src="/Images/FeatherProjects.png">
</p>

# Adafruit-Feather Projects

<HR>
  
## Project Goal

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

<HR>

<p align="center">
       <img width="500" height="281" src="/Images/FeatherRP2040a.PNG">
</p>
  
## Hardware

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


<HR>

<p align="center">
       <img width="600" height="338" src="/Images/P500.PNG">
</p>

## Tools

- [Raspberry Pi P500](https://www.raspberrypi.com/products/raspberry-pi-500/) running [Raspberry Pi OS 64-bit](https://www.raspberrypi.com/software/)
  - Help > Bookshelf > Books > Get Started with MicroPython on Raspberry Pi Pico
    - Free 139 page book on MicroPython and the Raspberry Pi Pico (RP2040)
- [Mu editor V1.0.3](https://codewith.mu/)
- [CircuitPython](https://circuitpython.org/)
  - [CircuitPython 9.2.4 for Adafruit Feather RP2040 as of Feb. 3, 2025](https://circuitpython.org/board/adafruit_feather_rp2040/)
  - [Libraries](https://circuitpython.org/libraries)
- [OpenAI](https://openai.com/) ChatGPT o3-mini-high
