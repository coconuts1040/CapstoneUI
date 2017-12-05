# External module imports
import RPi.GPIO as GPIO
import time
import socket
import select
import urllib.request
import json
import csv
from datetime import datetime

#########################################################################################
class DecisionAlgorithm(object):

#***************************************************************************************#
    # constructs the DecisionAlgorithm object
    def __init__(self):
        # Pin Definitons:
        self.heatPin = 16
        self.coolPin = 18

        # Wifi Setup
        HOST = '192.168.1.119'    # The remote host
        PORT = 80              # The same port as used by the server
        self.socketS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketS.connect((HOST, PORT))

        # Pin Setup:
        GPIO.setmode(GPIO.BOARD) # Boardpin-numbering scheme
        GPIO.setup(self.heatPin, GPIO.OUT) # LED pin set as output
        GPIO.setup(self.coolPin, GPIO.OUT) # LED pin set as output

        # Initial state for LEDs:
        GPIO.output(self.heatPin, GPIO.LOW)
        GPIO.output(self.coolPin, GPIO.LOW)

        # Variables Setup:
        self.ambientLight = 0 # current light sensor value out of 1024
        self.setLight = 256 # light threshold
        self.humanTimer = 0 # number of cycles since there was no motion

        self.outTemp = 0 # outside temperature (in Fahrenheit), given by the weather channel
        self.setTemp = 0 # current temperature setting (in Fahrenheit)
        self.ambientTemp = 0 # current temperature (in Fahrenheit) read by a temperature sensor, in a room
        self.tempThreshold = 2 # the degrees (in Fahrenheit) of leeway given to setting the temperature
        
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
        if (self.ambientLight < self.setLight) and (self.human or (self.light and (self.humanTimer < 60))):
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
                    self.airCond = True
                    GPIO.output(self.coolPin, GPIO.HIGH) # cooling = True
                else: # outTemp < ambientTemp
                    if (self.outTemp < self.setTemp - self.tempThreshold):
                        self.window = True
                        self.airCond = False
                        GPIO.output(self.coolPin, GPIO.LOW) # cooling = False
                    else: # outTemp > setTemp
                        if not self.ecoMode:
                            self.window = True
                            self.airCond = True
                            GPIO.output(self.coolPin, GPIO.HIGH) # cooling = True
                        else:
                            self.window = True
                            self.airCond = False
                            GPIO.output(self.coolPin, GPIO.LOW) # cooling = False
            else: # ambientTemp <= setTemp
                self.window = False
                self.airCond = False
                GPIO.output(self.coolPin, GPIO.LOW) # cooling = False

        # Heating
        if self.heatingOn:
            if (self.ambientTemp < self.setTemp - self.tempThreshold):
                if (self.outTemp < self.ambientTemp):
                    self.window = False
                    self.heater = True
                    GPIO.output(self.heatPin, GPIO.HIGH) # heater = True
                    print('HEAT 1')
                else: # outTemp > ambientTemp
                    if (self.outTemp > self.setTemp + self.tempThreshold):
                        self.window = True
                        self.heater = False
                        GPIO.output(self.heatPin, GPIO.LOW) # heater = False
                        print('HEAT OFF 1')
                    else: # outTemp < setTemp
                        if not self.ecoMode:
                            self.window = True
                            self.heater = True
                            GPIO.output(self.heatPin, GPIO.HIGH) # heater = True
                            print('HEAT 2')
                        else:
                            self.window = True
                            self.heater = False
                            GPIO.output(self.heatPin, GPIO.LOW) # heater = False
                            print('HEAT OFF 2')
            else: # ambientTemp > setTemp
                self.window = False
                self.heater = False
                GPIO.output(self.heatPin, GPIO.LOW) # heater = False
                print('HEAT OFF 3')

    #***********************************************************************************#
    # Get current weather data.
    def getWeatherData(self):
        f = urllib.request.urlopen('http://api.wunderground.com/api/b60a60cef2a36764/geolookup/conditions/q/MA/Boston.json')
        json_string = f.read()
        parsed_json = json.loads(json_string.decode('utf-8'))
        location = parsed_json['location']['city']
        temp_f = parsed_json['current_observation']['temp_f']
        print("Current temperature in %s is: %s" % (location, temp_f))
        self.outTemp = temp_f
        f.close()
    
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
        #print('Received', repr(data))

        # Parse data read
        values = data.decode('UTF-8').split('\n')
        self.ambientTemp = int(((int(bin(int(values[0], 16))[5:], 2) / 16) * 1.8) + 32)
        self.ambientLight = int(values[1], 16)

        if int(values[2], 16) == 0:
            self.human = False
            self.humanTimer += 1
        else:
            self.human = True
            self.humanTimer = 0

        #print(self.light)      

        # Write to csv file
        sttime = datetime.now().strftime('%Y%m%d_%H:%M:%S')
        readableTemp = self.ambientTemp*1.8 + 32
        with open('test.csv', 'a') as fp:
            writer = csv.writer(fp, delimiter=',') 
            writer.writerow([readableTemp, self.setTemp, self.outTemp, self.ambientLight, self.human, self.heater, self.airCond, sttime])
        print('Ambient', self.ambientTemp, 'Set', self.setTemp, 'Outside', self.outTemp, 'Heating', self.heatingOn, 'HEATER', self.heater)

    #***********************************************************************************#
    # Decrement setTemp.
    def decrementSetTempF(self):
        self.setTemp = self.setTemp - 1
        
    #***********************************************************************************#
    # Increment setTemp.
    def incrementSetTempF(self):
        self.setTemp = self.setTemp + 1

    #***********************************************************************************#
    # Turn off heating.
    def heatOff(self):
        GPIO.output(self.heatPin, GPIO.LOW)

    #***********************************************************************************#
    # Turn off cooling.
    def coolOff(self):
        GPIO.output(self.coolPin, GPIO.LOW)
    
    #***********************************************************************************#
    # Cleanup GPIO if Ctrl+C is pressed.
    def cleanupGPIO(self):
        GPIO.output(self.heatPin, GPIO.LOW)
        GPIO.output(self.coolPin, GPIO.LOW)
        GPIO.cleanup() # cleanup all GPIO
