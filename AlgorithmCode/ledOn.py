# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
ledOnePin = 16 # Broadcom pin 18 (P1 pin 12)
ledPin = 18 # Broadcom pin 23 (P1 pin 16)

# Pin Setup:
GPIO.setmode(GPIO.BOARD) # Broadcom pin-numbering scheme
GPIO.setup(ledOnePin, GPIO.OUT) # LED pin set as output
GPIO.setup(ledPin, GPIO.OUT) # PWM pin set as output

# Initial state for LEDs:
GPIO.output(ledOnePin, GPIO.LOW)
GPIO.output(ledPin, GPIO.LOW)

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        GPIO.output(ledOnePin, GPIO.HIGH)
        GPIO.output(ledPin, GPIO.HIGH)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.output(ledOnePin, GPIO.LOW)
    GPIO.output(ledPin, GPIO.LOW)
    GPIO.cleanup() # cleanup all GPIO
