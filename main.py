# Test that pins can light an LED. Turns out they can! Note this assumes pin 26 is driving the LED.
import RPi.GPIO as GPIO
import time

# P1 header scheme numbering
GPIO.setmode(GPIO.BOARD)

# Create GPIO output channel on 26
pin = 26
GPIO.setup(pin, GPIO.OUT)

text = "hello world"

# Set up dot, dash and gap times
dot_time        = 0.2 # 0.2 seconds
dash_time       = 3 * dot_time
intra_char_time = dot_time
short_gap_time  = 3 * dot_time
medium_gap_time = 7 * dot_time

# Set up pin writing functions for dash, dot, etc
def dash():
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(dash_time)
        GPIO.output(pin, GPIO.LOW)
        return

def dot():
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(dot_time)
        GPIO.output(pin, GPIO.LOW)
        return

def intra_char_gap():
        GPIO.output(pin, GPIO.LOW)
        time.sleep(intra_char_time)
        return

def short_gap():
        GPIO.output(pin, GPIO.LOW)
        time.sleep(short_gap_time)
        return

def medium_gap():
        GPIO.output(pin, GPIO.LOW)
        time.sleep(medium_gap_time)
        return


def morsify(char):
        morse_dict = { 'h' : '....',
                       ' ' : ' ',
                     }
        return morse_dict[char]

char_array = list(text)
for char in char_array:
        print(morsify(char))



GPIO.cleanup()
