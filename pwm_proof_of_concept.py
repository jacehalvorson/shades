from machine import Pin, PWM

servoPin = Pin(2, Pin.OUT)
servoPwm = PWM(servoPin, freq=50, duty_ns=1500000)