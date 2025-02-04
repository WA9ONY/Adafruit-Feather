[Index](https://github.com/WA9ONY/Adafruit-Feather/tree/main/Feather-RP2040)

---

# **Lab 1: Introduction to the Adafruit Feather RP2040 (Using Mu IDE)**

## **1. Overview & Learning Objectives**

### **Overview**
In this lab, you will:
- **Familiarize Yourself with the Hardware:** Identify key components and interfaces on the Adafruit Feather RP2040.
- **Set Up the Development Environment:** Install necessary drivers and software to program the board using the Mu IDE.
- **Deploy Your First Program:** Write and upload a simple “blink” program to illuminate the onboard LED.

### **Learning Objectives**
By the end of this lab, you will be able to:
- Recognize and describe the main hardware components of the Feather RP2040.
- Install and configure the Mu IDE for programming.
- Write, upload, and execute a basic microcontroller program.
- Troubleshoot common issues during setup and programming.

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
  - Designed for low-power and battery-powered applications.
  - Onboard battery charging circuitry (if using a LiPo battery).

### **B. Board Layout & Key Components**
- **Onboard LED:**  
  - Used for basic debugging (blinking indicates that your program is running).
- **USB Port:**  
  - For both programming and serial communication.
- **GPIO Pins:**  
  - Available for connecting sensors, actuators, and other peripherals.  
  - Refer to the board’s schematic and pinout diagram provided in your lab manual.
- **Power Supply Options:**  
  - USB power and battery input.

### **C. Development Environment Options**
- **MicroPython/CircuitPython:**  
  - High-level languages that allow quick prototyping.
- **C/C++ (Arduino IDE or SDK):**  
  - Provides more control and efficiency for resource-constrained applications.

For this lab, we will use **MicroPython** along with the **Mu IDE**, which is designed to be beginner-friendly and streamlined for microcontroller projects.

---

## **3. Lab: Hands-On Session**

### **Step 1: Setting Up Your Hardware**
1. **Unbox and Inspect:**  
   - Examine your Adafruit Feather RP2040. Identify the onboard LED, USB port, and headers for GPIO pins.
2. **Connecting the Board:**  
   - Connect the board to your computer using a micro USB cable.
3. **Driver Installation:**  
   - If your operating system does not automatically recognize the board, install the necessary USB drivers (refer to the Adafruit documentation as needed).

### **Step 2: Setting Up the Development Environment with Mu IDE**
1. **Download and Install Mu IDE:**  
   - Visit the [Mu Editor website](https://codewith.mu/) and download the installer for your operating system.
   - Follow the installation instructions to install Mu on your computer.
2. **Configure Mu for MicroPython:**
   - Launch the Mu IDE.
   - In the bottom-right corner of the window, you’ll see a “Mode” selector. Click on it and choose **MicroPython**. (Note: Although Mu labels this as “MicroPython,” it works well with boards like the RP2040.)
   - If prompted, select the serial port corresponding to your Feather RP2040. If you’re unsure which port to choose, disconnect and reconnect your board to see which port appears.
3. **Verify Connection:**
   - Mu should automatically connect to your board. You can verify this by checking the status indicator in the IDE, which will indicate a successful connection.

### **Step 3: Writing Your First Program – Blink LED**
1. **Understanding the Code:**
   - You’ll write a simple program to toggle the onboard LED on and off every second.
2. **Sample Code:**

   ```python
   import time
   from machine import Pin

   # Initialize the onboard LED pin.
   # For many RP2040 boards (like the Raspberry Pi Pico), the onboard LED is on GPIO 25.
   # Check your board’s documentation for the correct pin number.
   led = Pin(25, Pin.OUT)

   while True:
       led.on()          # Turn the LED on.
       time.sleep(1)     # Wait for 1 second.
       led.off()         # Turn the LED off.
       time.sleep(1)     # Wait for 1 second.
   ```

3. **Uploading and Running the Code:**
   - In Mu, paste the above code into a new file.
   - Click the **Flash** button (or select **Run > Flash** from the menu) to upload the code to your Feather RP2040.
   - Once the upload is complete, the onboard LED should start blinking. If it doesn’t, check the output console in Mu for any error messages.

### **Step 4: Troubleshooting**
- **Board Not Recognized:**  
  - Ensure your USB cable is properly connected and functioning. Try another cable if necessary.
- **IDE Connection Issues:**  
  - Verify you have selected the correct serial port in the Mu IDE’s mode settings.
- **Code Errors:**  
  - Double-check your code for typos, especially in indentation and syntax since Python is sensitive to these details.

### **Step 5: Reflection and Questions**
- **Documentation:**  
  - In your lab notebook, note the steps you took for setting up the hardware and software, as well as any issues encountered.
- **Discussion Questions:**
  - What advantages does using MicroPython offer for rapid prototyping on microcontrollers?
  - How might you modify the blink program to change the blink rate or introduce a different LED pattern (such as a “double blink”)?

---

## **4. Lab Assignment & Next Steps**

### **Lab Assignment**
- **Process Documentation:**  
  - Prepare a short report (1–2 pages) outlining:
    - The steps you followed to set up your hardware and configure Mu IDE.
    - How you uploaded and executed the blink program.
    - Any troubleshooting steps you performed.
- **Code Exploration:**  
  - Modify the blink program to create an alternative LED pattern (e.g., a “double blink” sequence).
  - Submit your modified code along with your lab report.

### **Next Lab Preview**
In our next session, we will cover:
- **Advanced I/O:**  
  - Reading sensor data using the ADC (Analog-to-Digital Converter).
- **Peripheral Integration:**  
  - Connecting and programming additional components like buttons and displays.
- **Introduction to Interrupts and Timers:**  
  - Utilizing these features for more responsive applications.

---

## **5. Summary**

Today’s lab covered:
- An introduction to the Adafruit Feather RP2040 and its key features.
- Setting up your development environment using the Mu IDE.
- Writing, uploading, and executing a basic blink program in MicroPython.
- Troubleshooting common issues encountered during the process.

Feel free to ask any questions if any part of the lab was unclear or if you ran into any difficulties. Happy coding, and I look forward to reviewing your lab reports and code modifications!
