"""
Kite Altimeter
Version: 07
Date: 2025-02-16
Author: David Haworth, WA9ONY
Website: https://www.qrz.com/db/WA9ONY
GitHub https://github.com/WA9ONY/Adafruit-Feather/tree/main
"""

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
import math
import time
import board
import busio
import neopixel
import digitalio
import displayio
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
TIME_ONLY_WITHOUT_NEWLINE = 6

sequence_num = 0
SEA_LEVEL_PRESSURE = 1013.25  # Standard sea-level pressure in hPa
altitude_offset = 0  # Offset for zeroing altitude

pause_time = 1

# Built-in LED setup
led_status = False
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
    print("Taking base pressure readings")
    readings = []
    for i in range(measurements):
        print(".", end="")
        # Read the pressure measurement from the DPS310 sensor
        pressure_value = dps310.pressure
        readings.append(pressure_value)
        # Small delay between measurements for sensor stability
        time.sleep(0.1)
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
    print(f"Avg: {avg_pressure:6.3f} hPa")
    time.sleep(pause_time)
    print(f"Min: {min_pressure:6.3f} hPa")
    time.sleep(pause_time)
    print(f"Max: {max_pressure:6.3f} hPa")
    time.sleep(pause_time)
    print(f"Std:{std_dev:6.3f} hPa")
    time.sleep(pause_time)
    print(f"Rng:{pressure_range:6.3f} hPa")
    time.sleep(pause_time)
    print(f"Rng:{altitude_range_inches:6.3f} in")
    time.sleep(pause_time)
    print("---------------------")
    time.sleep(pause_time)
    return avg_pressure


def print_date_time(mode: int = 1):
    """
    Prints the current date/time information based on the selected mode.

    Mode definitions:
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

    if mode == 1:
        print(time_str)
    elif mode == 2:
        print(date_str)
    elif mode == 3:
        print(day_str)
    elif mode == 4:
        print("{} {}".format(date_str, time_str))
    elif mode == 5:
        print("{} {} {}".format(date_str, day_str, time_str))
    elif mode == 6:
        print(time_str, end='')
    else:
        print("Invalid mode. Please use a mode from 1 to 6.")


# ----------------------------------------------------
# Initialization Code
# ----------------------------------------------------

print("Initializing\nKite Altimeter")
time.sleep(pause_time)

pressure_base = pressure_average(32)
print("Pressure calc",  pressure_base)
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
time.sleep(pause_time)
"""

# Set time
#rtc.datetime = time.struct_time((2025, 2,   16,    18,    24,   0,   6,  -1,   -1))
   
# ----------------------------------------------------
# Program Loop
# ----------------------------------------------------
while True:
    sequence_num = sequence_num + 1

    LED_Blink(led_blink_time)
    NeoPixel_Blink(neopixel_blink_time, (0, 255, 0))  # Green Blink

    pressure = dps310.pressure
    altitude = hpa_to_feet(pressure)
    altitude_above_gnd = hpa_to_feet(pressure) - hpa_to_feet(pressure_base)
    altitude_above_gnd_inches = altitude_above_gnd * 12.0
    
    print_date_time(TIME_ONLY_WITHOUT_NEWLINE)
#    print(" %.1f""'" %  altitude_above_gnd) # Print altitude in feet
    print(" %.1f"'"' %  altitude_above_gnd_inches) # Print altitude in inches
#    print(" %.1f""'" %  altitude_above_gnd, "%.1f"'"' %  altitude_above_gnd_inches)

    time.sleep(pause_time)

# Test code
#    print(sequence_num, "%.2f ft" %  altitude_above_gnd, "%.2f in" %  altitude_above_gnd_inches)
#    print("%.3f hPa" % pressure, "%.1f ft" %  altitude)
#    log_data(sequence_num, pressure, altitude)    


    

