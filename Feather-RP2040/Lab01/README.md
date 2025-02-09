<P align="center"> - <A HREF="https://www.qrz.com/db/WA9ONY">WA9ONY</A> - <A HREF="https://www.youtube.com/user/DavidAHaworth">YouTube</A> - <A HREF="http://www.stargazing.net/david/index.html">Website</A> -<BR>
- <A HREF="https://github.com/WA9ONY">GitHub WA9ONY</A>: 
<A HREF="https://github.com/WA9ONY/Adafruit-Feather/tree/main">Adafruit Feather</A><BR> 
 <BR>
<A HREF="https://github.com/WA9ONY/Adafruit-Feather/tree/main/Feather-RP2040"> Adafruit Feather RP2040 Index</A>
</P>

The [OpenAI](https://en.wikipedia.org/wiki/OpenAI) icon appears next to information in this web page that was created by OpenAI ChatGPT4 o3-mini-high in a conversation with David Haworth, WA9ONY.

<img align=right width="49" height="48" src="/Images/OpenAI_Icon.png">

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

## circup

Raspberry Pi  P500 termainal

59  source circup-env/bin/activate
   60  pip install circup
   61  clear
   62  circup list
   63  clear
   64  circup update
   65  clear
   66  circup diff
   67  circup --help
   68  deactivate
   69  history
   70  source circup-env/bin/activate
   71  circup list
   72  pip3 install --upgrade thonny
   73  source circup-env/bin/activate
   74  pip3 install --upgrade thonny
   75  deactivate
   76  history
   77  source circup-env/bin/activate
   78  deactivate
   79  ls /dev/ttyACM*
   80  dmesg | grep tty
   81  sudo usermod -a -G dialout $USER
   82  history
david@rpi500:~ $ !73
source circup-env/bin/activate
(circup-env) david@rpi500:~ $ !62
circup list
Found device adafruit_feather_rp2040 at /media/david/CIRCUITPY, running CircuitPython 9.2.4.
Downloading latest bundles for adafruit/Adafruit_CircuitPython_Bundle (20250208).
py:
Extracting:  [####################################]  100%          
8.x-mpy:
Extracting:  [####################################]  100%          
9.x-mpy:
Extracting:  [####################################]  100%          

OK

All modules found on the device are up to date.
(circup-env) david@rpi500:~ $ circup list
Found device adafruit_feather_rp2040 at /media/david/CIRCUITPY, running CircuitPython 9.2.4.
All modules found on the device are up to date.
(circup-env) david@rpi500:~ $ help circup
bash: help: no help topics match `circup'.  Try `help help' or `man -k circup' or `info circup'.
(circup-env) david@rpi500:~ $ circup --version
Circup, A CircuitPython module updater. Version 2.1.1
(circup-env) david@rpi500:~ $ circup help
Usage: circup [OPTIONS] COMMAND [ARGS]...
Try 'circup --help' for help.

Error: No such command 'help'.
(circup-env) david@rpi500:~ $ circup -help
Usage: circup [OPTIONS] COMMAND [ARGS]...
Try 'circup --help' for help.

Error: No such option: -h
(circup-env) david@rpi500:~ $ circup --help
Usage: circup [OPTIONS] COMMAND [ARGS]...

  A tool to manage and update libraries on a CircuitPython device.

Options:
  --verbose           Comprehensive logging is sent to stdout.
  --path DIRECTORY    Path to CircuitPython directory. Overrides automatic
                      path detection.
  --host TEXT         Hostname or IP address of a device. Overrides automatic
                      path detection.
  --port INTEGER      Port to contact. Overrides automatic path detection.
  --password TEXT     Password to use for authentication when --host is used.
                      You can optionally set an environment variable
                      CIRCUP_WEBWORKFLOW_PASSWORD instead of passing this
                      argument. If both exist the CLI arg takes precedent.
  --timeout INTEGER   Specify the timeout in seconds for any network
                      operations.
  --board-id TEXT     Manual Board ID of the CircuitPython device. If provided
                      in combination with --cpy-version, it overrides the
                      detected board ID.
  --cpy-version TEXT  Manual CircuitPython version. If provided in combination
                      with --board-id, it overrides the detected CPy version.
  --version           Show the version and exit.
  --help              Show this message and exit.

Commands:
  bundle-add     Add bundles to the local bundles list, by "user/repo"...
  bundle-remove  Remove one or more bundles from the local bundles list.
  bundle-show    Show the list of bundles, default and local, with URL,...
  example        Copy named example(s) from a bundle onto the device.
  freeze         Output details of all the modules found on the connected...
  install        Install a named module(s) onto the device.
  list           Lists all out of date modules found on the connected...
  show           Show a list of available modules in the bundle.
  uninstall      Uninstall a named module(s) from the connected device.
  update         Update modules on the device. Use --all to automatically
                 update all modules without Major Version warnings.
(circup-env) david@rpi500:~ $ circup -a
Usage: circup [OPTIONS] COMMAND [ARGS]...
Try 'circup --help' for help.

Error: No such option: -a
(circup-env) david@rpi500:~ $ circup --auto
Usage: circup [OPTIONS] COMMAND [ARGS]...
Try 'circup --help' for help.

Error: No such option: --auto Did you mean --path?
(circup-env) david@rpi500:~ $ ^C
(circup-env) david@rpi500:~ $ circup insatll -a
Usage: circup [OPTIONS] COMMAND [ARGS]...
Try 'circup --help' for help.

Error: No such command 'insatll'.
(circup-env) david@rpi500:~ $ circup install -a
Found device adafruit_feather_rp2040 at /media/david/CIRCUITPY, running CircuitPython 9.2.4.
Auto file: code.py
Auto file path: code.py
Auto file path: /media/david/CIRCUITPY/code.py
Searching for dependencies for: ['adafruit_display_text', 'adafruit_displayio_sh1107']
Ready to install: ['adafruit_bitmap_font', 'adafruit_display_text', 'adafruit_displayio_sh1107', 'adafruit_ticks']

Installed 'adafruit_bitmap_font'.
Installed 'adafruit_display_text'.
Installed 'adafruit_displayio_sh1107'.
Installed 'adafruit_ticks'.
(circup-env) david@rpi500:~ $ ^C
(circup-env) david@rpi500:~ $ 

ource circup-env/bin/activate
circup list
help circup
circup --version
circup --help
circup install -a
deactivate

