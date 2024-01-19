from machine import Pin, RTC
import time
from TimeOfDay import TimeOfDay

# 7 AM
OPEN_TIME = TimeOfDay(7, 0, 0)
# 6 PM
CLOSE_TIME = TimeOfDay(18, 0, 0)

SPIN_DURATION_MS = 2400
WAIT_TIME_MS = 900

# RTC.datetime constants
HOUR_INDEX = 4
MINUTE_INDEX = 5
SECOND_INDEX = 6
MILLISECONDS_PER_SECOND = 1000

# Initialize pins
led = Pin(25, Pin.OUT)
clockwisePin = Pin(0, Pin.OUT)
counterClockwisePin = Pin(1, Pin.OUT)
motorEnablePin = Pin(2, Pin.OUT)
inputPin = Pin(3, Pin.OUT)

# Initialize RTC
rtc = RTC()

# Initialize global variables
currentTime = rtc.datetime()
currentTimeOfDay = TimeOfDay(currentTime[HOUR_INDEX], currentTime[MINUTE_INDEX], currentTime[SECOND_INDEX])
if currentTimeOfDay < OPEN_TIME or currentTimeOfDay > CLOSE_TIME:
    shadesOpen = False
else:
    shadesOpen = True
    
def openShades():
    global shadesOpen
    
    print('Shades opening')
    if (shadesOpen == True):
        print('Shades already open')
        return
    
    # SPIN_DURATION_MS ms clockwise rotation
    motorEnablePin.on()
    clockwisePin.on()
    counterClockwisePin.off()
    time.sleep_ms(SPIN_DURATION_MS)
    clockwisePin.off()
    
    shadesOpen = True
    
def closeShades():
    global shadesOpen
    
    print('Shades closing')
    if (shadesOpen == False):
        print('Shades already closed')
        return
    
    # SPIN_DURATION_MS ms counter-clockwise rotation
    motorEnablePin.on()
    clockwisePin.off()
    counterClockwisePin.on()
    time.sleep_ms(SPIN_DURATION_MS)
    counterClockwisePin.off()
    shadesOpen = False
    
def toggleShades():
    print(f'toggleShades, shadesOpen = {shadesOpen}')
    if (shadesOpen == True):
        closeShades()
    else:
        openShades()

while True:
    currentTime = rtc.datetime()
    currentTimeOfDay = TimeOfDay(currentTime[HOUR_INDEX], currentTime[MINUTE_INDEX], currentTime[SECOND_INDEX])
    
    if (currentTimeOfDay == OPEN_TIME):
        openShades()
        
    if (currentTimeOfDay == CLOSE_TIME):
        closeShades()
    
    if (inputPin.value()):
        print('toggling')
        toggleShades()
    
    if (shadesOpen):
        led.on()
    else:
        led.off()
    
    time.sleep_ms(WAIT_TIME_MS)
