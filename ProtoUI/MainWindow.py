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

    def pressedEcoBtn(self):
        if not self.model.ecoMode:
            self.model.ecoMode = True
            print("Eco Mode: ON")

    def pressedHeatBtn(self):
        if not self.model.heatingOn:
            self.model.coolingOn = False
            self.model.heatingOn = True
            print("Heat ON")

    def pressedCoolBtn(self):
        if not self.model.coolingOn:
            self.model.heatingOn = False
            self.model.coolingOn = True
            print("Cool ON")

    def pressedUpTempBtn(self):
        self.model.setTemp += 1
        setTempString = str(self.model.setTemp)
        self.set_temp_lbl.setText(setTempString)
        print(self.model.setTemp)

    def pressedDownTempBtn(self):
        self.model.setTemp -= 1
        setTempString = str(self.model.setTemp)
        self.set_temp_lbl.setText(setTempString)
        print(self.model.setTemp)

    def __init__(self, model):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        self.model = model
        setTempString = str(self.model.setTemp)
        self.set_temp_lbl.setText(setTempString)
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
