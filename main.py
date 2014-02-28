# Test that pins can light an LED. Turns out they can! Note this assumes pin 26 is driving the LED.
import RPi.GPIO as GPIO
import time
import re
from get_text import get_text

# P1 header scheme numbering
GPIO.setmode(GPIO.BOARD)

# Create GPIO output channel on 26
pin = 26
GPIO.setup(pin, GPIO.OUT)


# Set up dot, dash and gap times
dot_time        = 0.1 # 0.1 seconds
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
        morse_dict = {  'a' : '.-' ,
                        'b' : '-...',
                        'c' : '-.-.',
                        'd' : '-..',
                        'e' : '.',
                        'f' : '..-.',
                        'g' : '--.',
                        'h' : '....',
                        'i' : '..',
                        'j' : '.---',
                        'k' : '-.-',
                        'l' : '.-..',
                        'm' : '--',
                        'n' : '-.',
                        'o' : '---',
                        'p' : '.--.',
                        'q' : '--.-',
                        'r' : '.-.',
                        's' : '...',
                        't' : '-',
                        'u' : '..-',
                        'v' : '...-',
                        'w' : '.--',
                        'x' : '-..-',
                        'y' : '-.--',
                        'z' : '--..',

                        '1' : '.----',
                        '2' : '..---',
                        '3' : '...--',
                        '4' : '....-',
                        '5' : '.....',
                        '6' : '-....',
                        '7' : '--...',
                        '8' : '---..',
                        '9' : '----.',
                        '0' : '-----',
                     }

        if (char in morse_dict):
                return morse_dict[char]
        else:
                return '!'

def blink_morse(text):
        # Convert text to array of lower-case chars, then translate this to Morse
        char_array = list(text.lower())

        regex_char = re.compile('[a-z,A-Z,0-9]') # Regex used to check a char is in Morse code 
        regex_endl = re.compile('\n') # Regex used to check a char is followed by endline

        morsified = ''

        for i in range(1, len(char_array)):
                if   (regex_char.match(char_array[i-1]) and regex_char.match(char_array[i])): # Morse-compatible character followed by Morse-compatible character
                        morsified += (morsify(char_array[i-1]) + '\\')              # Backslash for char gap  

                elif (regex_char.match(char_array[i-1]) and char_array[i] == ' '):       # Morse-compatible character followed by space
                        morsified += (morsify(char_array[i-1]) + ' ')               # Space for word-space gap

                if (i==len(char_array)-1): # Last character on the line
                        morsified += (morsify(char_array[i]) + ' ')

        #print(morsified)

        for char in morsified:
                if   (char == '.'):
                        dot()
                        intra_char_gap()

                elif (char == '-'):
                        dash()
                        intra_char_gap()

                elif (char == ' '):
                        medium_gap()

                elif (char == '\\'):
                        short_gap()
                        
                        
#text = "SO"

while True:
        text = get_text("IRC")
        #print(text)
        blink_morse(text)

GPIO.cleanup()
