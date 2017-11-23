# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Nov 16 22:41:38 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setStyleSheet("#MainWindow{\n"
"background: white;\n"
"}\n"
"QPushButton {\n"
"background-color: transparent;\n"
"border-width: 2px;\n"
"border-radius: 9px;\n"
"border-color: #99e600;\n"
"border-style: solid;\n"
"}\n"
"\n"
"QFrame#frame{\n"
"background-color: #d1d1e0;\n"
"border-color: #d1d1e0;\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"}\n"
"QFrame#frame_2{\n"
"background-color: #d1d1e0;\n"
"border-color: #d1d1e0;\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"}\n"
"QFrame#frame_3{\n"
"background-color: #d1d1e0;\n"
"border-color: #d1d1e0;\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"}\n"
"")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setStyleSheet("#centralWidget{\n"
"background: transparent\n"
"}")
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 240, 211, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.normal_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.normal_btn.setObjectName("normal_btn")
        self.verticalLayout_2.addWidget(self.normal_btn)
        self.eco_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.eco_btn.setObjectName("eco_btn")
        self.verticalLayout_2.addWidget(self.eco_btn)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(550, 240, 211, 121))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.heat_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.heat_btn.setObjectName("heat_btn")
        self.verticalLayout_4.addWidget(self.heat_btn)
        self.cool_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.cool_btn.setObjectName("cool_btn")
        self.verticalLayout_4.addWidget(self.cool_btn)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(290, 40, 211, 72))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.title_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.title_lbl.setFont(font)
        self.title_lbl.setObjectName("title_lbl")
        self.gridLayout_2.addWidget(self.title_lbl, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(290, 240, 211, 121))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.current_tmp_lbl = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.current_tmp_lbl.setFont(font)
        self.current_tmp_lbl.setObjectName("current_tmp_lbl")
        self.gridLayout.addWidget(self.current_tmp_lbl, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.up_temp_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.up_temp_btn.setFont(font)
        self.up_temp_btn.setObjectName("up_temp_btn")
        self.verticalLayout.addWidget(self.up_temp_btn)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.set_temp_lbl = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.set_temp_lbl.setFont(font)
        self.set_temp_lbl.setObjectName("set_temp_lbl")
        self.gridLayout_6.addWidget(self.set_temp_lbl, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.gridLayout_6)
        self.down_temp_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.down_temp_btn.setFont(font)
        self.down_temp_btn.setObjectName("down_temp_btn")
        self.verticalLayout.addWidget(self.down_temp_btn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(30, 170, 211, 5))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralWidget)
        self.frame_2.setGeometry(QtCore.QRect(290, 170, 211, 5))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.centralWidget)
        self.frame_3.setGeometry(QtCore.QRect(550, 170, 211, 5))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 180, 211, 51))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.mode_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.mode_lbl.setFont(font)
        self.mode_lbl.setObjectName("mode_lbl")
        self.gridLayout_3.addWidget(self.mode_lbl, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(290, 180, 211, 51))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.temp_lbl = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.temp_lbl.setFont(font)
        self.temp_lbl.setObjectName("temp_lbl")
        self.gridLayout_4.addWidget(self.temp_lbl, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(550, 180, 211, 51))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.heat_cool_lbl = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.heat_cool_lbl.setFont(font)
        self.heat_cool_lbl.setObjectName("heat_cool_lbl")
        self.gridLayout_5.addWidget(self.heat_cool_lbl, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.normal_btn.setText(_translate("MainWindow", "Normal"))
        self.eco_btn.setText(_translate("MainWindow", "Eco"))
        self.heat_btn.setText(_translate("MainWindow", "Heat"))
        self.cool_btn.setText(_translate("MainWindow", "Cool"))
        self.title_lbl.setText(_translate("MainWindow", "EcoHub"))
        self.current_tmp_lbl.setText(_translate("MainWindow", "70"))
        self.up_temp_btn.setText(_translate("MainWindow", "+"))
        self.set_temp_lbl.setText(_translate("MainWindow", "70"))
        self.down_temp_btn.setText(_translate("MainWindow", "-"))
        self.mode_lbl.setText(_translate("MainWindow", "Mode"))
        self.temp_lbl.setText(_translate("MainWindow", "Temperature"))
        self.heat_cool_lbl.setText(_translate("MainWindow", "Heating + Cooling"))

