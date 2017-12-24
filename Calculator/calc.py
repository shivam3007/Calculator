# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(742, 764)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        MainWindow.setDocumentMode(True)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 671, 51))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("font: 75 italic 18pt \"Gill Sans MT\";")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.Button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_1.setGeometry(QtCore.QRect(50, 140, 81, 81))
        self.Button_1.setStyleSheet("font: 75 italic 14pt \"MS Shell Dlg 2\";")
        self.Button_1.setObjectName("Button_1")
        self.Button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_2.setGeometry(QtCore.QRect(240, 140, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.Button_2.setFont(font)
        self.Button_2.setObjectName("Button_2")
        self.Button_10 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_10.setGeometry(QtCore.QRect(580, 140, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Button_10.setFont(font)
        self.Button_10.setObjectName("Button_10")
        self.Button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_3.setGeometry(QtCore.QRect(410, 140, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.Button_3.setFont(font)
        self.Button_3.setObjectName("Button_3")
        self.Button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_4.setGeometry(QtCore.QRect(50, 290, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.Button_4.setFont(font)
        self.Button_4.setObjectName("Button_4")
        self.Button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_5.setGeometry(QtCore.QRect(240, 290, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.Button_5.setFont(font)
        self.Button_5.setObjectName("Button_5")
        self.Button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_6.setGeometry(QtCore.QRect(410, 290, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.Button_6.setFont(font)
        self.Button_6.setObjectName("Button_6")
        self.Button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_7.setGeometry(QtCore.QRect(60, 450, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.Button_7.setFont(font)
        self.Button_7.setObjectName("Button_7")
        self.Button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_8.setGeometry(QtCore.QRect(240, 450, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.Button_8.setFont(font)
        self.Button_8.setObjectName("Button_8")
        self.Button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_9.setGeometry(QtCore.QRect(410, 450, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.Button_9.setFont(font)
        self.Button_9.setObjectName("Button_9")
        self.Button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_0.setGeometry(QtCore.QRect(250, 600, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.Button_0.setFont(font)
        self.Button_0.setObjectName("Button_0")
        self.Button_11 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_11.setGeometry(QtCore.QRect(580, 360, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Button_11.setFont(font)
        self.Button_11.setObjectName("Button_11")
        self.Button_12 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_12.setGeometry(QtCore.QRect(580, 490, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Button_12.setFont(font)
        self.Button_12.setObjectName("Button_12")
        self.Button_13 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_13.setGeometry(QtCore.QRect(580, 250, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Button_13.setFont(font)
        self.Button_13.setObjectName("Button_13")
        self.Button_14 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_14.setGeometry(QtCore.QRect(580, 610, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Button_14.setFont(font)
        self.Button_14.setObjectName("Button_14")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 742, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.Button_1.setText(_translate("MainWindow", "1"))
        self.Button_2.setText(_translate("MainWindow", "2"))
        self.Button_10.setText(_translate("MainWindow", "+"))
        self.Button_3.setText(_translate("MainWindow", "3"))
        self.Button_4.setText(_translate("MainWindow", "4"))
        self.Button_5.setText(_translate("MainWindow", "5"))
        self.Button_6.setText(_translate("MainWindow", "6"))
        self.Button_7.setText(_translate("MainWindow", "7"))
        self.Button_8.setText(_translate("MainWindow", "8"))
        self.Button_9.setText(_translate("MainWindow", "9"))
        self.Button_0.setText(_translate("MainWindow", "0"))
        self.Button_11.setText(_translate("MainWindow", "-"))
        self.Button_12.setText(_translate("MainWindow", "*"))
        self.Button_13.setText(_translate("MainWindow", "÷"))
        self.Button_14.setText(_translate("MainWindow", "="))

        #self.lineEdit.setReadOnly(True)
        self.Button_0.clicked.connect(self.add_0)
        self.Button_1.clicked.connect(self.add_1)
        self.Button_2.clicked.connect(self.add_2)
        self.Button_3.clicked.connect(self.add_3)
        self.Button_4.clicked.connect(self.add_4)
        self.Button_5.clicked.connect(self.add_5)
        self.Button_6.clicked.connect(self.add_6)
        self.Button_7.clicked.connect(self.add_7)
        self.Button_8.clicked.connect(self.add_8)
        self.Button_9.clicked.connect(self.add_9)
        self.Button_10.clicked.connect(self.add_p)
        self.Button_11.clicked.connect(self.add_s)
        self.Button_12.clicked.connect(self.add_m)
        self.Button_13.clicked.connect(self.add_d)
        self.Button_14.clicked.connect(self.add_e)

    def add_0(self):
        res = self.lineEdit.text() + str(0)
        self.lineEdit.setText(str(res))

    def add_1(self):
        res = self.lineEdit.text() + str(1)
        self.lineEdit.setText(str(res))

    def add_2(self):
        res = self.lineEdit.text() + str(2)
        self.lineEdit.setText(str(res))

    def add_3(self):
        res = self.lineEdit.text() + str(3)
        self.lineEdit.setText(str(res))

    def add_4(self):
        res = self.lineEdit.text() + str(4)
        self.lineEdit.setText(str(res))

    def add_5(self):
        res = self.lineEdit.text() + str(5)
        self.lineEdit.setText(str(res))

    def add_6(self):
        res = self.lineEdit.text() + str(6)
        self.lineEdit.setText(str(res))

    def add_7(self):
        res = self.lineEdit.text() + str(7)
        self.lineEdit.setText(str(res))

    def add_8(self):
        res = self.lineEdit.text() + str(8)
        self.lineEdit.setText(str(res))

    def add_9(self):
        res = self.lineEdit.text() + str(9)
        self.lineEdit.setText(str(res))

    def add_p(self):
         res = self.lineEdit.text() + '+'
         self.lineEdit.setText(str(res))

    def add_s(self):
        res = self.lineEdit.text() + '-'
        self.lineEdit.setText(str(res))

    def add_m(self):
        res = self.lineEdit.text() + '*'
        self.lineEdit.setText(str(res))

    def add_d(self):
        res = self.lineEdit.text() + '/'
        self.lineEdit.setText(str(res))

    def add_e(self):
      #  res = eval('self.lineEdit.text()')
        self.lineEdit.setText(str(eval(self.lineEdit.text())))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

