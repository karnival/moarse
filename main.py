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

        if (char in morse_dict):
                return morse_dict[char]
        else:
                return '!'

def blink_morse(text)
        # Convert text to array of chars, then translate this to dots, dashes, spaces and exclamation marks. The latter are for incompatible characters.
        char_array = list(text)

        morsified = ''

        for (i, char) in char_array:
                if (char_array[i] == '[a-z,A-Z,0-9]' && char_array[i+1] == '[a-z,A-Z,0-9]'):
                        morsified += (morsify(char) + '\') # Backslash for char gap  
                elif (char_array[i] == '[a-z,A-Z,0-9]' && char_array[i+1] == ' '):
                        morsified += (morsify(char) + '#') # Hash for word-space gap
                elif (char_array[i] == '[a-z,A-Z,0-9]' && char_array[i+1] == '$'):
                        morsified += (morsify(char_array[i+1])) # Hash for word-space gap

        print(morsified)

        for char in morsified:
                if char == '.'
                        

GPIO.cleanup()
