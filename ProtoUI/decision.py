# External module imports
import RPi.GPIO as GPIO
import time
import socket
import select

#########################################################################################
class DecisionAlgorithm(object):

#***************************************************************************************#
    # constructs the DecisionAlgorithm object
    def __init__(self):
        # Pin Definitons:
        HEATPIN = 16 
        COOLPIN = 18

        # Wifi Setup
        HOST = '192.168.1.126'    # The remote host
        PORT = 80              # The same port as used by the server
        self.socketS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketS.connect((HOST, PORT))

        # Pin Setup:
        GPIO.setmode(GPIO.BOARD) # Boardpin-numbering scheme
        GPIO.setup(HEATPIN, GPIO.OUT) # LED pin set as output
        GPIO.setup(COOLPIN, GPIO.OUT) # LED pin set as output

        # Initial state for LEDs:
        GPIO.output(HEATPIN, GPIO.LOW)
        GPIO.output(COOLPIN, GPIO.LOW)

        # Variables Setup:
        self.ambientLight = 0 # current light sensor value out of 1024
        self.setLight = 256 # light threshold
        self.humanTimer = 0 # number of cycles since there was no motion

        self.outTemp = 0 # outside temperature (in Celsius), given by the weather channel
        self.setTemp = 0 # current temperature setting (in Celsius)
        self.ambientTemp = 0 # current temperature (in Celsius) read by a temperature sensor, in a room
        self.tempThreshold = 1 # the degrees (in Celsius) of leeway given to setting the temperature
        
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
        if self.human and not self.blinds:
                if (self.ambientLight >= self.setLight):
                    self.blinds = False
                else:
                    self.blinds = True
        elif not self.human:
            if self.blinds:
                if (self.outTemp > self.setTemp):
                    self.blinds = False
                else:
                    self.blinds = True
            else:
                self.blinds = False

    #***********************************************************************************#
    # Controls whether the lights are on or off.
    def controlLights(self):
        if (self.ambientLight < self.setLight) and
            (self.human or (self.light and (self.humanTimer < 60))):
                self.light = True
        else:
            self.light = False

    #***********************************************************************************#
    # Controls the HVAC for heating and cooling and whether the windows are open or shut.
    def controlTemp(self):
        # Cooling
        if self.coolingOn:
            if (self.ambientTemp > self.setTemp + self.tempThreshold):
                if (self.outTemp > self.ambientTemp):
                    self.window = False
                    GPIO.output(coolPin, GPIO.HIGH) # cooling = True
                else: # outTemp < ambientTemp
                    if (self.outTemp < self.setTemp - self.tempThreshold):
                        self.window = True
                        GPIO.output(coolPin, GPIO.LOW) # cooling = False
                    else: # outTemp > setTemp
                        if not self.ecoMode:
                            self.window = True
                            GPIO.output(coolPin, GPIO.HIGH) # cooling = True
                        else:
                            self.window = True
                            GPIO.output(coolPin, GPIO.LOW) # cooling = False
            else: # ambientTemp <= setTemp
                self.window = False
                GPIO.output(coolPin, GPIO.LOW) # heater = False

        # Heating
        elif self.heatingOn:
            if (self.ambientTemp < self.setTemp - self.tempThreshold):
                if (self.outTemp < self.ambientTemp):
                    self.window = False
                    GPIO.output(heatPin, GPIO.HIGH) # heater = True
                else: # outTemp > ambientTemp
                    if (self.outTemp > self.setTemp + self.tempThreshold):
                        self.window = True
                        GPIO.output(heatPin, GPIO.LOW) # heater = False
                    else: # outTemp < setTemp
                        if not self.ecoMode:
                            self.window = True
                            GPIO.output(heatPin, GPIO.HIGH) # heater = True
                        else:
                            self.window = True
                            GPIO.output(heatPin, GPIO.LOW) # heater = False
            else: # ambientTemp > setTemp
                self.window = False
                GPIO.output(heatPin, GPIO.LOW) # heater = False

    #***********************************************************************************#
    # Receive data from the socket.
    def getSensorData(self):
        input = [self.socketS]

        # Empty socket
        while True:
            inputready, o, e = select.select(input, [], [], 0.0)
            if len(inputready) == 0:
                break
            for s in inputready:
                s.recv(1)
                
        # Get most recent socket data
        data = self.socketS.recv(1024)
        print('Received', repr(data))

        # Parse data read
        values = data.decode('UTF-8').split('\n')
        self.ambientTemp = int(bin(int(values[0], 16))[5:], 2) / 16
        self.ambientLight = int(values[1], 16)

        if int(values[2], 16) == 0:
            self.human = False
            self.humanTimer += 1
        else:
            self.human = True
            self.humanTimer = 0

        print(self.light)
        
    #***********************************************************************************#
    # Convert ambient temperature to Fahrenheit.
    def toFahrenheit(self):
        return int((self.ambientTemp*1.8) + 32)
    
    #***********************************************************************************#
    # Cleanup GPIO if Ctrl+C is pressed.
    def cleanupGPIO(self):
        GPIO.output(heatPin, GPIO.LOW)
        GPIO.output(coolPin, GPIO.LOW)
        GPIO.cleanup() # cleanup all GPIO
