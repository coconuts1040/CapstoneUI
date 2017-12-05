# From https://www.baldengineer.com/raspberry-pi-gui-tutorial.html 
# by James Lewis (@baldengineer)
# Minimal python code to start PyQt5 GUI
#
# This program represents the controller that takes in a model and a view from the main() function 
# and handles their interaction.

# always seem to need this
import sys

# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *

# This is our window from QtCreator
import mainwindow_auto

# decision algorithm model
from decision import DecisionAlgorithm

# threading for polling sensor module
import threading

# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
    # access variables inside of the UI's file

    ### functions for the buttons to call
    def pressedNormalBtn(self):
        if self.model.ecoMode:
            self.model.ecoMode = False
            print("Eco Mode: OFF")
            self.eco_btn.setStyleSheet('QPushButton {background-color: transparent;}')
            self.normal_btn.setStyleSheet('QPushButton {background-color: #d9d9f2;}')

    def pressedEcoBtn(self):
        if not self.model.ecoMode:
            self.model.ecoMode = True
            print("Eco Mode: ON")
            self.normal_btn.setStyleSheet('QPushButton {background-color: transparent;}')
            self.eco_btn.setStyleSheet('QPushButton {background-color: #e6ffe6;}')

    def pressedHeatBtn(self):
        self.model.heatingOn = not self.model.heatingOn
        if self.model.heatingOn:
            print("Heat ON")
            self.heat_btn.setStyleSheet('QPushButton {background-color: #ffe6e6;}')
        else:
            print("Heat OFF")
            self.model.heatOff()
            self.heat_btn.setStyleSheet('QPushButton {background-color: transparent;}')

    def pressedCoolBtn(self):
        self.model.coolingOn = not self.model.coolingOn
        if self.model.coolingOn:
            print("Cool ON")
            self.cool_btn.setStyleSheet('QPushButton {background-color: #e6ffff;}')
        else:
            print("Cool Off")
            self.model.coolOff()
            self.cool_btn.setStyleSheet('QPushButton {background-color: transparent}')

    def pressedUpTempBtn(self):
        self.model.incrementSetTempF()
        setTempString = str(self.model.setTemp)
        self.set_temp_lbl.setText(setTempString)
        print(self.model.setTemp)

    def pressedDownTempBtn(self):
        self.model.decrementSetTempF()
        setTempString = str(self.model.setTemp)
        self.set_temp_lbl.setText(setTempString)
        print(self.model.setTemp)

    def __init__(self, model):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        self.model = model
        self.model.getSensorData()
        self.model.getWeatherData()
        self.model.setTemp = self.model.ambientTemp

        setTempString = str(self.model.setTemp)
        curTempString = str(self.model.ambientTemp)

        self.set_temp_lbl.setText(setTempString)
        self.current_tmp_lbl.setText(curTempString)
        self.normal_btn.setStyleSheet('QPushButton {background-color: #d9d9f2;}')
        self.runSystem()

        ### Hooks to for buttons
        self.normal_btn.clicked.connect(lambda: self.pressedNormalBtn())
        self.eco_btn.clicked.connect(lambda: self.pressedEcoBtn())
        self.heat_btn.clicked.connect(lambda: self.pressedHeatBtn())
        self.cool_btn.clicked.connect(lambda: self.pressedCoolBtn())
        self.up_temp_btn.clicked.connect(lambda: self.pressedUpTempBtn())
        self.down_temp_btn.clicked.connect(lambda: self.pressedDownTempBtn())

    # Runs the decision algorithm constantly
    def runSystem(self):
        threading.Timer(1.0, self.runSystem).start()
        try:
            self.model.getSensorData()
            curTempString = str(self.model.ambientTemp)
            self.current_tmp_lbl.setText(curTempString)
            
            self.model.controlBlinds()
            self.model.controlLights()
            self.model.controlTemp()

        except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
            self.model.cleanupGPIO()

# passes the model to the MainWindow controller, will be moved to its own file
def main():
    # a new app instance
    app = QApplication(sys.argv)
    model = DecisionAlgorithm()
    form = MainWindow(model)
    form.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())

# python bit to figure how who started This
if __name__ == "__main__":
   main()
