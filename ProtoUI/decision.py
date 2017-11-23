# External module imports
#import RPi.GPIO as GPIO
import time

#########################################################################################
class DecisionAlgorithm(object):

#***************************************************************************************#
    # constructs the DecisionAlgorithm object
    def __init__(self):
        # Pin Definitons:
        HEATPIN = 16 
        COOLPIN = 18 

        # Pin Setup:
        # GPIO.setmode(GPIO.BOARD) # Boardpin-numbering scheme
        # GPIO.setup(HEATPIN, GPIO.OUT) # LED pin set as output
        # GPIO.setup(COOLPIN, GPIO.OUT) # LED pin set as output

        # Initial state for LEDs:
        # GPIO.output(HEATPIN, GPIO.LOW)
        # GPIO.output(COOLPIN, GPIO.LOW)

        # Variables Setup:
        self.ambientLight = 0 #?
        self.setLight = 0 #?

        self.outTemp = 0 # outside temperature, given by the weather channel
        self.setTemp = 0 # current temperature setting
        self.ambientTemp = 0 # current temperature read by a temperature sensor, in a room

        self.human = False # true if motion is detected

        self.light = False # light turns on if true
        self.blinds = False # blinds extend if true
        self.window = False # window opens if true

        self.airCond = False # can delete later, replaced by GPIO
        self.heater = False # can delete later, replaced by GPIO
        self.coolingOn = False # true if thermostat set to cool
        self.heatingOn = False # true if thermostat set to heat
        self.ecoMode = False # true if eco-mode is enabled

        print("Here we go! Press CTRL+C to exit")

#***************************************************************************************#
    # Controls whether the blinds are up or down.
    def controlBlinds(self):
        if (self.human == True):
            if (self.blinds == True):
                self.blinds = True
            else:
                if (self.ambientLight >= self.setLight):
                    self.blinds = False
                else:
                    self.blinds = True
        else:
            if (self.blinds == True):
                if (self.outTemp > self.setTemp):
                    self.blinds = False
                else:
                    self.blinds = True
            else:
                self.blinds = False

    #***********************************************************************************#
    # Controls whether the lights are on or off.
    def controlLights(self):
        if (self.human == True):
            if (self.ambientLight < self.setLight):
                self.light = True
        else:
            self.light = False

    #***********************************************************************************#
    # Controls the HVAC for heating and cooling and whether the windows are open or shut.
    def controlTemp(self):
        # Cooling
        if (self.coolingOn == True):
            if (self.ambientTemp > self.setTemp):
                if (self.outTemp > self.ambientTemp):
                    if (self.ecoMode == False):
                        self.window = False
                        # GPIO.output(coolPin, GPIO.HIGH) # cooling = True
                    else:
                        self.window = False
                        # GPIO.output(coolPin, GPIO.HIGH) # cooling = True
                else: # outTemp < ambientTemp
                    if (self.outTemp < self.setTemp):
                        if (self.ecoMode == False):
                            self.window = True
                            # GPIO.output(coolPin, GPIO.LOW) # cooling = False
                        else:
                            self.window = True
                            # GPIO.output(coolPin, GPIO.LOW) # cooling = False
                    else: # outTemp > setTemp
                        if (self.ecoMode == False):
                            self.window = True
                            # GPIO.output(coolPin, GPIO.HIGH) # cooling = True
                        else:
                            self.window = True
                            # GPIO.output(coolPin, GPIO.LOW) # cooling = False
            else: # ambientTemp < setTemp
                self.window = False
                # GPIO.output(coolPin, GPIO.LOW) # heater = False

        # Heating
        elif (self.heatingOn == True):
            if (self.ambientTemp < self.setTemp):
                if (self.outTemp < self.ambientTemp):
                    if (self.ecoMode == False):
                        self.window = False
                        # GPIO.output(heatPin, GPIO.HIGH) # heater = True
                    else:
                        self.window = False
                        # GPIO.output(heatPin, GPIO.HIGH) # heater = True
                else: # outTemp > ambientTemp
                    if (self.outTemp > self.setTemp):
                        if (self.ecoMode == False):
                            self.window = True
                            # GPIO.output(heatPin, GPIO.LOW) # heater = False
                        else:
                            self.window = True
                            # GPIO.output(heatPin, GPIO.LOW) # heater = False
                    else: # outTemp < setTemp
                        if (self.ecoMode == False):
                            self.window = True
                            # GPIO.output(heatPin, GPIO.HIGH) # heater = True
                        else:
                            self.window = True
                            # GPIO.output(heatPin, GPIO.LOW) # heater = False
            else: # ambientTemp > setTemp
                self.window = False
                # GPIO.output(heatPin, GPIO.LOW) # heater = False

    #***********************************************************************************#
    # Cleanup GPIO if Ctrl+C is pressed.
    def cleanupGPIO(self):
        GPIO.output(heatPin, GPIO.LOW)
        GPIO.output(coolPin, GPIO.LOW)
        GPIO.cleanup() # cleanup all GPIO
