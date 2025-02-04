

Welcome to **Lab 1: Introduction to the Adafruit Feather RP2040**. Today, we’re going to get hands-on with the Feather RP2040 microcontroller, understand its features, and set up your development environment to run your very first program on the board.

---

## **1. Overview & Learning Objectives**

### **Overview**
In this lab, you will:
- **Familiarize Yourself with the Hardware:** Identify key components and interfaces on the Adafruit Feather RP2040.
- **Set Up the Development Environment:** Install necessary drivers and software to program the board.
- **Deploy Your First Program:** Write and upload a simple “blink” program to illuminate the onboard LED.

### **Learning Objectives**
By the end of this lab, you will be able to:
- Recognize and describe the main hardware components of the Feather RP2040.
- Install and configure an Integrated Development Environment (IDE) for programming.
- Write, upload, and execute a basic microcontroller program.
- Troubleshoot common issues that arise during setup and programming.

---

## **2. Lecture: Understanding the Adafruit Feather RP2040**

### **A. The RP2040 Microcontroller**
- **Architecture:**  
  - Dual-core ARM Cortex-M0+ processors.
  - Designed for versatility in embedded applications.
- **Memory:**  
  - 264 KB of SRAM.
  - External flash storage (typically 2 MB on the Feather RP2040).
- **Interfaces & Peripherals:**  
  - Multiple GPIO pins, PWM outputs, SPI, I²C, UART, ADC, etc.
  - Built-in USB interface for programming and communication.
- **Unique Features:**  
  - The Feather RP2040 is designed for low-power and battery-powered applications.
  - Onboard battery charging circuitry (if using a LiPo battery).

### **B. Board Layout & Key Components**
- **Onboard LED:**  
  - Used for basic debugging (blinking indicates that your program is running).
- **USB Port:**  
  - For both programming and serial communication.
- **GPIO Pins:**  
  - Various pins are available for connecting sensors, actuators, and other peripherals.  
  - Check the board’s schematic and pinout diagram provided in your lab manual.
- **Power Supply Options:**  
  - USB power and battery input.

### **C. Development Environment Options**
- **MicroPython/CircuitPython:**  
  - These high-level languages allow you to quickly prototype and test code.
- **C/C++ (Arduino IDE or SDK):**  
  - Offers more control and efficiency for resource-constrained applications.
  
For today’s lab, we will use **MicroPython** with the [Thonny IDE](https://thonny.org/), which is beginner-friendly and perfect for rapid prototyping.

---

## **3. Lab: Hands-On Session**

### **Step 1: Setting Up Your Hardware**
1. **Unbox and Inspect:**  
   - Examine your Adafruit Feather RP2040. Identify the onboard LED, USB port, and headers for GPIO pins.
2. **Connecting the Board:**  
   - Use a micro USB cable to connect the board to your computer.
3. **Driver Installation:**  
   - If your operating system does not automatically recognize the board, install the necessary USB drivers. (Refer to the Adafruit documentation if needed.)

### **Step 2: Setting Up the Development Environment**
1. **Download Thonny IDE:**  
   - Visit [thonny.org](https://thonny.org/) and install the IDE compatible with your operating system.
2. **Configure Thonny for MicroPython:**  
   - Open Thonny.
   - Go to **Tools > Options > Interpreter**.
   - Select “MicroPython (Raspberry Pi Pico)” (the RP2040 is compatible, and settings are similar).
   - Choose the correct serial port that corresponds to your Feather RP2040.

### **Step 3: Writing Your First Program – Blink LED**
1. **Understanding the Code:**
   - We will write a simple program that toggles the onboard LED on and off every second.
2. **Sample Code:**

   ```python
   import time
   from machine import Pin

   # Initialize the onboard LED pin (check your board's documentation for the correct pin number)
   # For many RP2040 boards, the onboard LED is connected to a specific GPIO (e.g., GP25 on the Raspberry Pi Pico).
   led = Pin(25, Pin.OUT)  

   while True:
       led.on()           # Turn LED on
       time.sleep(1)      # Wait for 1 second
       led.off()          # Turn LED off
       time.sleep(1)      # Wait for 1 second
   ```

3. **Uploading the Code:**
   - In Thonny, paste the above code into a new file.
   - Save the file (for example, as `blink.py`) on your board if it is mounted as a USB drive, or use Thonny’s “Run” functionality to upload it directly.
   - Once uploaded, the onboard LED should start blinking. If it doesn’t, check the serial output in Thonny’s shell for error messages.

### **Step 4: Troubleshooting**
- **Board Not Recognized:**  
  - Verify your USB cable and connection. Try another cable if necessary.
- **IDE Connection Issues:**  
  - Double-check the selected serial port in Thonny’s interpreter settings.
- **Code Errors:**  
  - Ensure you’ve typed the code correctly. Python is sensitive to indentation and syntax.

### **Step 5: Reflection and Questions**
- **Documentation:**  
  - Write a brief note in your lab notebook about your setup process and any issues you encountered.
- **Questions for Discussion:**
  - What are the advantages of using MicroPython for rapid prototyping on microcontrollers?
  - How might you modify the blink program to change the blink rate or pattern?

---

## **4. Lab Assignment & Next Steps**

### **Lab Assignment**
- **Document Your Process:**  
  - Create a short report (1–2 pages) describing:
    - The steps you took to set up the hardware and software.
    - How you uploaded and executed the blink program.
    - Any troubleshooting steps you followed.
- **Code Exploration:**  
  - Modify the blink program to create a different LED pattern (for example, a “double blink”).
  - Submit your modified code along with your report.

### **Next Lab Preview**
In our next session, we will explore:
- **Advanced I/O:**  
  - Reading sensor data using the ADC (Analog-to-Digital Converter).
- **Peripheral Integration:**  
  - Connecting and programming additional components like buttons and displays.
- **Introduction to Interrupts and Timers:**  
  - How to use these features for responsive applications.

---

## **5. Summary**

Today’s lab introduced you to the Adafruit Feather RP2040:
- We covered the hardware layout and key features of the board.
- You set up your development environment using Thonny IDE.
- You wrote and executed a simple program to blink the onboard LED.
- You learned some basic troubleshooting techniques.

Feel free to ask any questions if any part of the lab was unclear or if you encountered any difficulties. Happy coding, and I look forward to seeing your modifications and lab reports!
