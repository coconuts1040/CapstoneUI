# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
heatPin = 16 
coolPin = 18 

# Pin Setup:
GPIO.setmode(GPIO.BOARD) # Boardpin-numbering scheme
GPIO.setup(heatPin, GPIO.OUT) # LED pin set as output
GPIO.setup(coolPin, GPIO.OUT) # LED pin set as output

# Initial state for LEDs:
GPIO.output(heatPin, GPIO.LOW)
GPIO.output(coolPin, GPIO.LOW)

# Variables Setup:
human = False

light = False
ambientLight = 0
setLight = 0

blinds = False
outTemp = 0
setTemp = 0

window = False
airCond = False # can delete later, replaced by GPIO
heater = False # can delete later, replaced by GPIO
coolingOn = False
heatingOn = False
ecoMode = False
ambientTemp = 0

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        #*******************************************************#
        # Blinds
        if (human == True):
            if (blinds == True):
                blinds = True
            else:
                if (ambientLight >= setLight):
                    blinds = False
                else:
                    blinds = True
        else:
            if (blinds == True):
                if (outTemp > setTemp):
                    blinds = False
                else:
                    blinds = True
            else:
                blinds = False
        #*******************************************************#
        # Lights
        if (human == True):
            if (ambientLight < setLight):
                light = True
        else:
            light = False
        #*******************************************************#
        # HVAC
        # Cooling
        if (coolingOn == True):
            if (ambientTemp > setTemp):
                if (outTemp > ambientTemp):
                    if (ecoMode == False):
                        window = False
                        GPIO.output(coolPin, GPIO.HIGH) # cooling = True
                    else:
                        window = False
                        GPIO.output(coolPin, GPIO.HIGH) # cooling = True
                else: # outTemp < ambientTemp
                    if (outTemp < setTemp):
                        if (ecoMode == False):
                            window = True
                            GPIO.output(coolPin, GPIO.LOW) # cooling = False
                        else:
                            window = True
                            GPIO.output(coolPin, GPIO.LOW) # cooling = False
                    else: # outTemp > setTemp
                        if (ecoMode == False):
                            window = True
                            GPIO.output(coolPin, GPIO.HIGH) # cooling = True
                        else:
                            window = True
                            GPIO.output(coolPin, GPIO.LOW) # cooling = False
            else: # ambientTemp < setTemp
                window = False
                GPIO.output(coolPin, GPIO.LOW) # heater = False
        #*******************************************************#   
        # Heating
        if (heatingOn == True):
            if (ambientTemp < setTemp):
                if (outTemp < ambientTemp):
                    if (ecoMode == False):
                        window = False
                        GPIO.output(heatPin, GPIO.HIGH) # heater = True
                    else:
                        window = False
                        GPIO.output(heatPin, GPIO.HIGH) # heater = True
                else: # outTemp > ambientTemp
                    if (outTemp > setTemp):
                        if (ecoMode == False):
                            window = True
                            GPIO.output(heatPin, GPIO.LOW) # heater = False
                        else:
                            window = True
                            GPIO.output(heatPin, GPIO.LOW) # heater = False
                    else: # outTemp < setTemp
                        if (ecoMode == False):
                            window = True
                            GPIO.output(heatPin, GPIO.HIGH) # heater = True
                        else:
                            window = True
                            GPIO.output(heatPin, GPIO.LOW) # heater = False
            else: # ambientTemp > setTemp
                window = False
                GPIO.output(heatPin, GPIO.LOW) # heater = False
        #*******************************************************#
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.output(heatPin, GPIO.LOW)
    GPIO.output(coolPin, GPIO.LOW)
    GPIO.cleanup() # cleanup all GPIO
