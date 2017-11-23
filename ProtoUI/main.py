# From https://www.baldengineer.com/raspberry-pi-gui-tutorial.html 
# by James Lewis (@baldengineer)
# Minimal python code to start PyQt5 GUI
#

# always seem to need this
import sys

# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *

# This is our window from QtCreator
import mainwindow_auto

# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
    # access variables inside of the UI's file

    ### functions for the buttons to call
    def pressedNormalBtn(self):
        ecoMode = 0;
        print(ecoMode)

    def pressedEcoBtn(self):
        ecoMode = 1;
        print(ecoMode)

    def pressedHeatBtn(self):
        heatingOn = 1;
        print(heatingOn)

    def pressedCoolBtn(self):
        coolingOn = 1;
        print(coolingOn)

    def pressedUpTempBtn(self):
        self.setTemp = self.setTemp + 1
        setTempString = str(self.setTemp)
        self.set_temp_lbl.setText(setTempString)
        print(self.setTemp)

    def pressedDownTempBtn(self):
        self.setTemp = self.setTemp - 1
        setTempString = str(self.setTemp)
        self.set_temp_lbl.setText(setTempString)
        print(self.setTemp)

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        self.setTemp = 70
        setTempString = str(self.setTemp)
        self.set_temp_lbl.setText(setTempString)

        ### Hooks to for buttons
        self.normal_btn.clicked.connect(lambda: self.pressedNormalBtn())
        self.eco_btn.clicked.connect(lambda: self.pressedEcoBtn())
        self.heat_btn.clicked.connect(lambda: self.pressedHeatBtn())
        self.cool_btn.clicked.connect(lambda: self.pressedCoolBtn())
        self.up_temp_btn.clicked.connect(lambda: self.pressedUpTempBtn())
        self.down_temp_btn.clicked.connect(lambda: self.pressedDownTempBtn())

# I feel better having one of these
def main():
    # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())

# python bit to figure how who started This
if __name__ == "__main__":
    main()
