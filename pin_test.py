# Test that pins can light an LED. Turns out they can! Note this assumes pin 26 is driving the LED.
import RPi.GPIO as GPIO
import time

# P1 header scheme numbering
GPIO.setmode(GPIO.BOARD)

# Create GPIO output channel on 26
GPIO.setup(26, GPIO.OUT)

# Output high on 26 
GPIO.output(26, GPIO.HIGH)

# Wait a second
time.sleep(1) 

# Output low on 26
GPIO.output(26, GPIO.LOW)

# Wait a second... again
time.sleep(1) 

GPIO.cleanup()
