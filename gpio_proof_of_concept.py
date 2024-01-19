from machine import Pin, RTC
import time

MAX_ITERATIONS = 65535
MINUTE_INDEX = 5
SECOND_INDEX = 6
MILLISECONDS_PER_SECOND = 1000
SWITCH_DELAY_S = 10

rtc = RTC()

led = Pin(25, Pin.OUT)

blueLed = Pin(0, Pin.OUT)

inputPin = Pin(1, Pin.IN)

toggleRateHz = 2
# timestamp = rtc.datetime()[SECOND_INDEX]
# print(f'Timestamp: {timestamp}')
i = 0
while i < MAX_ITERATIONS:
   # if ((rtc.datetime()[SECOND_INDEX] - timestamp) > SWITCH_DELAY_S):
   if (inputPin.value()):
      blueLed.on()
      toggleRateHz = 10
      print(f'10 Hz')
   else:
      blueLed.off()
      toggleRateHz = 2
      print(f'2 Hz')
   
   led.toggle()
   time.sleep_ms(MILLISECONDS_PER_SECOND // toggleRateHz)

   i += 1
