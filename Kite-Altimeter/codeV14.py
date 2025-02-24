# Kite Altimeter
# Version:
VERSION = 1.14
# Date: 2025-02-23
# Author: David Haworth, WA9ONY
# Website: https://www.qrz.com/db/WA9ONY
# GitHub https://github.com/WA9ONY/Adafruit-Feather/tree/main

# ----------------------------------------------------
# Kite Altimeter Hardware
# ----------------------------------------------------
# - Adafruit Feather RP2040 https://www.adafruit.com/product/4884
# - Adafruit DPS310 Precision Barometric Pressure / Altitude Sensor  https://www.adafruit.com/product/4494
# - STEMMA QT / Qwiic JST SH 4-Pin Cable - 50mm Long https://www.adafruit.com/product/4399
# - Adafruit FeatherWing OLED - 128x64 https://www.adafruit.com/product/4650
# - Adalogger FeatherWing - RTC pcf8523 + SD  https://www.adafruit.com/product/2922 
# - FeatherWing Tripler https://www.adafruit.com/product/3417
# - Adafruit LiPo Battery TBD

# ----------------------------------------------------
# Development Tools
# ----------------------------------------------------
# - Raspberry Pi 500 Rev 1.0 computer
# - OS: Debian GNU/Linux 12 (bookworm) aarch64 
# - Thonny IDE Version 4.1.4 Comes with Raspberry OS install. https://thonny.org/
# - Circup (for managing CircuitPython libraries) https://github.com/adafruit/circup
# - Circup is a Terminal CLI tool

# ----------------------------------------------------
# CircuitPython and Libraries
# ----------------------------------------------------
# - CircuitPython 9.2.4 https://circuitpython.org/board/adafruit_feather_rp2040/
# - CircuitPython 9.X Libraries https://circuitpython.org/libraries

# ----------------------------------------------------
# Modules and Libraries
# ----------------------------------------------------
import os
import gc
import sys
import math
import time
import alarm
import board
import busio
import storage
import analogio
import neopixel
import digitalio
import displayio
import microcontroller
import adafruit_displayio_sh1107
from i2cdisplaybus import I2CDisplayBus
from adafruit_dps310.basic import DPS310
from adafruit_pcf8523.pcf8523 import PCF8523

# ----------------------------------------------------
# Global Variables and Constants
# ----------------------------------------------------
TIME_ONLY = 1
DATE_ONLY = 2
DAY = 3
DATE_TIME = 4
DATE_DAY_TIME = 5
HI_NOW_LO_TIME = 6
TIME_ONLY_WITHOUT_NEWLINE = 7


TIME_FT = 1
TIME_INCHES = 2
SEQ_FT_IN = 3
HPA_FT = 4
FT_MAX_MIN = 5

operating_mode = HI_NOW_LO_TIME
sequence_num = 0
SEA_LEVEL_PRESSURE = 1013.25  # Standard sea-level pressure in hPa
altitude_offset = 0  # Offset for zeroing altitude

max_feet = 0
min_feet = 0
Hi_time_str = ""
Lo_time_str = ""

pause_time = 1

# Built-in LED setup
led_status = True
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led_blink_time = 50 # milliseconds

# Built-in NeoPixel setup
nexopixel_status = False
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)  # One NeoPixel
pixel.brightness = 0.5  # Adjust brightness (0.0 to 1.0)
neopixel_blink_time = 1

# Lookup table for names of days (nicer printing).
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


# ----------------------------------------------------
# Create Objects
# ----------------------------------------------------

# Initialize sensors
dps310 = DPS310(board.STEMMA_I2C())

# uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
rtc = PCF8523(board.I2C())

# Initialize OLED
# SH1107 is vertically oriented 64x128
displayio.release_displays()
display_bus = I2CDisplayBus(board.I2C(), device_address=0x3C)
display = adafruit_displayio_sh1107.SH1107(display_bus, width=128, height=64)

# Set up the ADC on A2 (Battery Voltage Monitor)
vbat_adc = analogio.AnalogIn(board.A0)


# ----------------------------------------------------
# Functions
# ----------------------------------------------------


def log_data(sequence: int, pressure: float, altitude: float, filename="data.csv"):
    """
    Logs data to a CSV file. Creates the file with headers if it does not exist.

    Parameters:
        sequence (int): Sequence number.
        pressure (float): Pressure value.
        altitude (float): Altitude value.
        filename (str): Name of the CSV file. Default is "data.csv".
    """
    # Get current date and time
    now = time.localtime()
    date_str = f"{now.tm_year}-{now.tm_mon:02d}-{now.tm_mday:02d}"
    time_str = f"{now.tm_hour:02d}:{now.tm_min:02d}:{now.tm_sec:02d}"
    
    # Prepare data entry
    data_entry = f"{sequence},{date_str},{time_str},{pressure:.2f},{altitude:.2f}\n"
    
    # Check if file exists
    file_exists = filename in os.listdir("/")
    
    # Open file in append mode
    with open(filename, "a") as file:
        if not file_exists:
            # Write header if file is newly created
            file.write("Sequence,Date,Time,Pressure,Altitude\n")
        # Write the data entry
        file.write(data_entry)

    print(f"Logged: {data_entry.strip()}")


def NeoPixel_Blink(millsec, color=(255, 0, 0)):
    """Blink the built-in NeoPixel for the given duration in milliseconds.
    
    Parameters:
        millsec (int): Duration of blink in milliseconds.
        color (tuple): RGB color for the NeoPixel.
    """
    if nexopixel_status: 
        pixel.fill((0, 0, 0))  # Ensure NeoPixel is off
        time.sleep(0.01)  # Small delay for visibility
        pixel.fill(color)  # Turn NeoPixel on with specified color
        time.sleep(millsec / 1000)  # Convert milliseconds to seconds
        pixel.fill((0, 0, 0))  # Turn NeoPixel off


def LED_Blink(millsec):
    """Blink the built-in LED for the given duration in milliseconds."""
    if led_status: 
        led.value = False  # Ensure LED is off
        time.sleep(0.05)  # Small delay to ensure it's seen as an intentional blink
        led.value = True  # Turn LED on
        time.sleep(millsec / 1000)  # Convert milliseconds to seconds
        led.value = False  # Turn LED off

def hpa_to_feet(pressure_hpa):
    """
    Convert atmospheric pressure (in hPa) to altitude (in feet)
    using the International Standard Atmosphere (ISA) model.

    Parameters:
        pressure_hpa (float): Pressure in hectopascals (hPa).

    Returns:
        float: Altitude in feet.
    """
    # Standard sea-level pressure in hPa
    sea_level_pressure = 1013.25

    # The exponent derived from the ISA barometric formula
    exponent = 0.1903

    # Conversion factor:
    # (T0 / L) in meters is approximately 44330.8 m, and 1 m = 3.28084 ft.
    # Thus, 44330.8 m * 3.28084 ft/m ≈ 145442 ft.
    conversion_factor = 145442

    # Calculate altitude in feet using the rearranged barometric formula
    altitude_feet = conversion_factor * (1 - (pressure_hpa / sea_level_pressure) ** exponent)

    return altitude_feet

def pressure_average(measurements: int = 64) -> float:
    """
    Reads a specified number of pressure measurements from the DPS310 sensor,
    calculates statistics on the measurements (average, minimum, maximum, range in hPa,
    altitude range in inches, and standard deviation), prints each statistic on a line 
    limited to ~21 characters with a 3-second delay between lines, pauses for 10 seconds,
    and returns the average pressure value.

    Parameters:
        measurements (int): The number of pressure measurements to take. Default is 64.

    Returns:
        float: The average pressure value in hPa.
    """
    print("Base hPa cal", measurements,"rdg")
    readings = []
    for i in range(measurements):
        print(".", end="")
        # Read the pressure measurement from the DPS310 sensor
        pressure_value = dps310.pressure
        readings.append(pressure_value)
        # Small delay between measurements for sensor stability
        time.sleep(0.1) # Delay for DPS310
    print(" ")
    # Calculate pressure statistics
    avg_pressure = sum(readings) / measurements
    min_pressure = min(readings)
    max_pressure = max(readings)
    pressure_range = max_pressure - min_pressure  # in hPa
    
    # Calculate the variance and standard deviation
    variance = sum((x - avg_pressure) ** 2 for x in readings) / measurements
    std_dev = math.sqrt(variance)
    
    # Calculate altitude for the extreme pressure values using hpa_to_feet.
    altitude_at_min_pressure = hpa_to_feet(min_pressure)  # higher altitude (ft)
    altitude_at_max_pressure = hpa_to_feet(max_pressure)  # lower altitude (ft)
    altitude_range_feet = altitude_at_min_pressure - altitude_at_max_pressure
    altitude_range_inches = altitude_range_feet * 12

    # Print the statistics with each line limited to ~21 characters and a 3-second delay between each
    print(f"Num: {measurements} Measurements")
    time.sleep(pause_time)
    print(f"Av: {avg_pressure:6.3f} hPa")
    time.sleep(pause_time)
    print(f"Min: {min_pressure:6.3f} hPa")
    time.sleep(pause_time)
    print(f"Max: {max_pressure:6.3f} hPa")
    time.sleep(pause_time)
    print(f"Std:{std_dev:6.3f} hPa")
    time.sleep(pause_time)
    print(f"Rng:{pressure_range:6.3f} hPa")
    time.sleep(pause_time)
    print(f"Rng:{altitude_range_inches:6.3f} inches")
    time.sleep(pause_time*5)

#    print("---------------------")
#    time.sleep(pause_time)
    return avg_pressure


def print_date_time(date_mode: int = 1):
    """
    Prints the current date/time information based on the selected mode.

    date_mode definitions:
        1: Print only time (HH:MM:SS).
        2: Print only date (YYYY-MM-DD).
        3: Print only day of the week.
        4: Print date and time.
        5: Print date, day of week, and time.
        6: Print only time (HH:MM:SS) without a newline at the end.
    
    Uses the RTC (PCF8523) to retrieve the current time.
    """
    # Retrieve current date and time from RTC.
    t = rtc.datetime

    # Create formatted strings.
    date_str = "{:04d}-{:02d}-{:02d}".format(t.tm_year, t.tm_mon, t.tm_mday)
    time_str = "{:02d}:{:02d}:{:02d}".format(t.tm_hour, t.tm_min, t.tm_sec)
    day_str = days[t.tm_wday]  # days is the global tuple defined earlier

    if date_mode == 1:
        print(time_str)
    elif date_mode == 2:
        print(date_str)
    elif date_mode == 3:
        print(day_str)
    elif date_mode == 4:
        print("{} {}".format(date_str, time_str))
    elif date_mode == 5:
        print("{} {} {}".format(date_str, day_str, time_str))
    elif date_mode == 6:
        print(time_str, end='')
    elif date_mode == 7:
        print(time_str, end='')
    else:
        print("Invalid date", date_mode)

def button_status():
    # If deep sleep is supported, use the alarm method.
    if hasattr(alarm, "exit_and_deep_sleep"):
        if alarm.wake_alarm:
            time.sleep(0.05)  # debounce delay
            if isinstance(alarm.wake_alarm, alarm.pin.PinAlarm):
                if alarm.wake_alarm.pin == board.D9:
                    return 9
                elif alarm.wake_alarm.pin == board.D6:
                    return 6
                elif alarm.wake_alarm.pin == board.D5:
                    return 5
            elif isinstance(alarm.wake_alarm, alarm.time.TimeAlarm):
                return 0

        # Deinitialize any existing digitalio button objects so alarms can use the pins.
        try:
            button9.deinit()
        except Exception:
            pass
        try:
            button6.deinit()
        except Exception:
            pass
        try:
            button5.deinit()
        except Exception:
            pass

        # Create PinAlarms for each button (active low with pull-ups) and a TimeAlarm.
        button9_alarm = alarm.pin.PinAlarm(pin=board.D9, value=False, pull=True)
        button6_alarm = alarm.pin.PinAlarm(pin=board.D6, value=False, pull=True)
        button5_alarm = alarm.pin.PinAlarm(pin=board.D5, value=False, pull=True)
        time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 1)

        # Enter deep sleep until one of the alarms triggers.
        alarm.exit_and_deep_sleep((button9_alarm, button6_alarm, button5_alarm, time_alarm))
    else:
        # Fallback polling method for boards that do not support deep sleep (e.g. RP2040).
        debounce_delay = 0.05  # 50 ms debounce delay

        # Create local digitalio button objects
        button9 = digitalio.DigitalInOut(board.D9)
        button9.direction = digitalio.Direction.INPUT
        button9.pull = digitalio.Pull.UP

        button6 = digitalio.DigitalInOut(board.D6)
        button6.direction = digitalio.Direction.INPUT
        button6.pull = digitalio.Pull.UP

        button5 = digitalio.DigitalInOut(board.D5)
        button5.direction = digitalio.Direction.INPUT
        button5.pull = digitalio.Pull.UP

        start = time.monotonic()
        while time.monotonic() - start < 1:
            # Check button on D9 pressed (active low)
            if not button9.value:
                time.sleep(debounce_delay)
                if not button9.value:
                    while not button9.value:
                        time.sleep(0.01)
                    # Deinitialize local buttons before returning
                    button9.deinit()
                    button6.deinit()
                    button5.deinit()
                    return 9
            # Check button on D6 pressed
            if not button6.value:
                time.sleep(debounce_delay)
                if not button6.value:
                    while not button6.value:
                        time.sleep(0.01)
                    button9.deinit()
                    button6.deinit()
                    button5.deinit()
                    return 6
            # Check button on D5 pressed
            if not button5.value:
                time.sleep(debounce_delay)
                if not button5.value:
                    while not button5.value:
                        time.sleep(0.01)
                    button9.deinit()
                    button6.deinit()
                    button5.deinit()
                    return 5
            time.sleep(0.01)
        # Deinitialize before returning if no button was pressed.
        button9.deinit()
        button6.deinit()
        button5.deinit()
        return 0


def print_chip_temperature():
    """Reads and prints the RP2040 chip temperature in Fahrenheit."""
    temperature_c = microcontroller.cpu.temperature  # Read temperature in Celsius
    temperature_f = (temperature_c * 9 / 5) + 32  # Convert to Fahrenheit
    print(f"Chip: {temperature_f:.2f} °F")


def print_memory_usage():
    """Prints the amount of free and used memory in bytes."""
    gc.collect()  # Run garbage collection to get an accurate reading
    free_mem = gc.mem_free()  # Get free memory
    allocated_mem = gc.mem_alloc()  # Get allocated memory
    total_mem = free_mem + allocated_mem  # Total memory available
    print("Memory Usage:\n\n")
    time.sleep(pause_time*3)    
    print(f"{allocated_mem} bytes used")
    print(f"{free_mem} bytes free")
    print(f"{total_mem} bytes total")
    time.sleep(pause_time*4)

def print_cpu_info():
    """Prints CPU information including clock speed, unique ID, and CircuitPython version."""
    cpu_freq = microcontroller.cpu.frequency  # Get CPU frequency in Hz
    cpu_temp = microcontroller.cpu.temperature  # Get CPU temperature in Celsius
    unique_id = microcontroller.cpu.uid  # Get the unique ID of the chip
    python_version = sys.version  # Get CircuitPython version
    board_name = os.uname().machine  # Get board name
    os_version = os.uname().version  # Get CircuitPython OS version

    # Format the unique ID separately before printing
    unique_id_str = " ".join(["{:02X}".format(x) for x in unique_id])

    print(f"{board_name}\n")
    time.sleep(pause_time*4)    
    print(f"CPU Freq: {cpu_freq / 1_000_000:.2f} MHz")
    print(f"CPU Temp: {cpu_temp:.1f}°C {(cpu_temp * 9/5) + 32:.1f}°F")
    time.sleep(pause_time*3)
    print(f"ID: {unique_id_str}\n")
    time.sleep(pause_time*3)
    print(f"CPy V: {python_version}")
    time.sleep(pause_time*4)
    print(f"OS V: {os_version}")
    time.sleep(pause_time*4)


def get_battery_voltage():
    """Reads the battery voltage from A0 and converts it to real voltage."""
    # ADC reference voltage (RP2040 uses a 3.3V reference)
    ADC_REF_VOLTAGE = 3.3
    # RP2040 ADC resolution is 16-bit, but only 12 bits are used (0-65535 range)
    ADC_RESOLUTION = 65535
    # Voltage divider ratio (from Feather RP2040's built-in circuit)
    VOLTAGE_DIVIDER_RATIO = 2.0  # The circuit divides by 2, so we multiply back
    CAL = 4.095/3.94
    raw_value = vbat_adc.value  # Read ADC value (0-65535)
    measured_voltage = (raw_value / ADC_RESOLUTION) * ADC_REF_VOLTAGE
    battery_voltage = measured_voltage * VOLTAGE_DIVIDER_RATIO * CAL  # Compensate for voltage divider
    return battery_voltage



# ----------------------------------------------------
# Initialization Code
# ----------------------------------------------------

print("Initializing\nKite hPa Altimeter")
print("Version", VERSION)
print("Close Alt Case 4 Cal")  # Time to put the case lid on

while True:
    print(get_battery_voltage())
    time.sleep(pause_time) 

time.sleep(pause_time*3)
print_date_time(3)
print_date_time(2)
print_date_time(1)
time.sleep(pause_time*3) 
print_memory_usage()
time.sleep(pause_time*3)
print_cpu_info()

measurements_num = 8 
pressure_base = pressure_average(measurements_num)
time.sleep(pause_time)

# Blink LED to indicate startup
LED_Blink(led_blink_time)

"""
#Test print_date_time function
print_date_time(TIME_ONLY)
time.sleep(pause_time)
print_date_time(DATE_ONLY)
time.sleep(pause_time)
print_date_time(DAY)
time.sleep(pause_time)
print_date_time(DATE_TIME)
time.sleep(pause_time)
print_date_time(DATE_DAY_TIME)
time.sleep(pause_time*2)
"""

# Set time
#rtc.datetime = time.struct_time((2025, 2,   16,    18,    24,   0,   6,  -1,   -1))


# ----------------------------------------------------
# Operating Mode Selection
# ----------------------------------------------------
# Set operating_mode for the altimeter.
# Change this variable to select the desired mode (1 through 20).

print("Operating Mode", operating_mode)
time.sleep(pause_time)


# ----------------------------------------------------
# Program Loop
# ----------------------------------------------------
while True:


# When the board wakes from deep sleep, this code runs again.
    result = button_status()
    if result != 0:
#        print("Button status:", result)
        if result == 9:
            operating_mode = operating_mode + 1
            if operating_mode == 7:
               operating_mode = 6
        if result == 6:
            operating_mode = 6
        if result == 5:
            operating_mode = operating_mode - 1
            if operating_mode == 0:
               operating_mode = 1
        print("Mode:", operating_mode)
        time.sleep(pause_time * 2)

    sequence_num = sequence_num + 1
    LED_Blink(led_blink_time)
    NeoPixel_Blink(neopixel_blink_time, (0, 255, 0))  # Green Blink
    pressure = dps310.pressure
    altitude = hpa_to_feet(pressure)
    altitude_above_gnd = hpa_to_feet(pressure) - hpa_to_feet(pressure_base)
    altitude_above_gnd_inches = altitude_above_gnd * 12.0

    current_feet = hpa_to_feet(pressure) - hpa_to_feet(pressure_base)
    t = rtc.datetime
    Now_time_str = "{:02d}:{:02d}:{:02d}".format(t.tm_hour, t.tm_min, t.tm_sec)

# Update maximum and minimum values
    if current_feet > max_feet:
        max_feet = current_feet
        t = rtc.datetime
        Hi_time_str = "{:02d}:{:02d}:{:02d}".format(t.tm_hour, t.tm_min, t.tm_sec)
    if current_feet < min_feet:
        min_feet = current_feet
        t = rtc.datetime
        Lo_time_str = "{:02d}:{:02d}:{:02d}".format(t.tm_hour, t.tm_min, t.tm_sec)


    if operating_mode == TIME_FT:
        # Operating Mode 1: Original functionality
        print_date_time(TIME_ONLY_WITHOUT_NEWLINE)
        print(" %.1f""'" % altitude_above_gnd)  # Print altitude in feet
        time.sleep(pause_time)
    elif operating_mode == TIME_INCHES:
        # Operating mode 2.
        print_date_time(TIME_ONLY_WITHOUT_NEWLINE)
        print(" %.1f"'"' %  altitude_above_gnd_inches) # Print altitude in inches
        time.sleep(pause_time)
    elif operating_mode == SEQ_FT_IN:
        #Operating mode 3.
        print("#" + str(sequence_num), "%.1f""'" %  altitude_above_gnd, "%.1f"'"' %  altitude_above_gnd_inches)
        time.sleep(pause_time)
    elif operating_mode == HPA_FT:
        # Operating mode 4.
        print("%.3f hPa" % pressure, "%.1f""'" %  altitude)    
        time.sleep(pause_time)
    elif operating_mode == FT_MAX_MIN:
        # Operating Mode 5: Print current altitude (feet), maximum and minimum of all measurements.

        # Print the current, maximum, and minimum altitude measurements
        print("%.1f'" % current_feet, "%.1f'" % max_feet, "%.1f'" % min_feet)
        time.sleep(pause_time)
    elif operating_mode == HI_NOW_LO_TIME:
        # Operating mode 6.
        print("Hi ", Hi_time_str, "%.1f'" % max_feet)
        print("Now", Now_time_str,"%.1f'" % current_feet)
        print("Lo ", Lo_time_str, "%.1f'" % min_feet)
        time.sleep(pause_time)
    elif operating_mode == 7:
        # Placeholder for future code for operating mode 7.
        time.sleep(pause_time)
    elif operating_mode == 8:
        # Placeholder for future code for operating mode 8.
        time.sleep(pause_time)
    elif operating_mode == 9:
        # Placeholder for future code for operating mode 9.
        time.sleep(pause_time)
    elif operating_mode == 10:
        # Placeholder for future code for operating mode 10.
        time.sleep(pause_time)
    elif operating_mode == 11:
        # Placeholder for future code for operating mode 11.
        time.sleep(pause_time)
    elif operating_mode == 12:
        # Placeholder for future code for operating mode 12.
        time.sleep(pause_time)
    elif operating_mode == 13:
        # Placeholder for future code for operating mode 13.
        time.sleep(pause_time)
    elif operating_mode == 14:
        # Placeholder for future code for operating mode 14.
        time.sleep(pause_time)
    elif operating_mode == 15:
        # Placeholder for future code for operating mode 15.
        time.sleep(pause_time)
    elif operating_mode == 16:
        # Placeholder for future code for operating mode 16.
        time.sleep(pause_time)
    elif operating_mode == 17:
        # Placeholder for future code for operating mode 17.
        time.sleep(pause_time)
    elif operating_mode == 18:
        # Placeholder for future code for operating mode 18.
        time.sleep(pause_time)
    elif operating_mode == 19:
        # Placeholder for future code for operating mode 19.
        time.sleep(pause_time)
    elif operating_mode == 20:
        # Placeholder for future code for operating mode 20.
        time.sleep(pause_time)
    else:
        print("Invalid", operating_mode)
        time.sleep(pause_time)



"""
    pressed = push_button_status()
    if pressed:
        print("Button pressed on pin:", pressed)
    time.sleep(0.01)
    

def push_button_status():
    debounce_delay = 0.05  # 50 milliseconds debounce time
    
    # Check button on D9
    if not button9.value:  # Active low: False means pressed
        time.sleep(debounce_delay)
        if not button9.value:
            # Wait for button release to avoid multiple detections
            while not button9.value:
                time.sleep(0.01)
            return 9

    # Check button on D6
    if not button6.value:
        time.sleep(debounce_delay)
        if not button6.value:
            while not button6.value:
                time.sleep(0.01)
            return 6

    # Check button on D5
    if not button5.value:
        time.sleep(debounce_delay)
        if not button5.value:
            while not button5.value:
                time.sleep(0.01)
            return 5

    return 0  # Return 0 if no button is pressed
    
    
"""


"""
SD_CS = board.D10
spi = board.SPI()

try:
    import sdcardio

    sd_card = sdcardio.SDCard(spi, SD_CS)
except ImportError:
    import adafruit_sdcard
    import digitalio

    cs = digitalio.DigitalInOut(SD_CS)
    sd_card = adafruit_sdcard.SDCard(spi, cs)

vfs = storage.VfsFat(sd_card)
storage.mount(vfs, "/sd_card")

print("Start Logging num to log file")
doOnce = True
while doOnce:
    try:
        with open("/sd_card/log.txt", "a") as sdc:
            data = 900.123           
            sdc.write(
                "{}, {}, {}, {:.2f}\n".format(
                    data, data, data, data
                )
            )
        time.sleep(3)
    except OSError:
        pass
    except RuntimeError:
        pass
    doOnce = False

print("End Logging num to log file")
"""
