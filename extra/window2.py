
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QComboBox


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        #flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        #self.setWindowFlags(flags)
        Dialog.setObjectName("Dialog")
        Dialog.resize(301, 303)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 301, 31))
        self.label.setStyleSheet("QLabel{\n"
" background-color:rgb(75, 83, 104);\n"
" padding-top :8px;\n"
" padding-bottom :8px;\n"
" color: rgba(243,207,72,255);\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 30, 301, 141))
        self.label_2.setStyleSheet("background-color:rgb(111, 118, 134);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(0, 230, 301, 31))
        self.label_9.setStyleSheet("QLabel{\n"
" border : 1px solid;\n"
" border-color:rgb(111, 118, 134);\n"
"background-color:rgb(255, 255, 255);\n"
"border-top-style: none;\n"
"}")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(0, 260, 301, 41))
        self.label_7.setStyleSheet("QLabel{\n"
"border-style:hidden;\n"
"}")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../../../Downloads/New folder (1)/New folder/my_shadow1.png"))
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(10, 40, 281, 31))
        self.comboBox.setStyleSheet("QComboBox {\n"
"background-color:rgb(163, 184, 204);\n"
"}")
        self.comboBox.setObjectName("comboBox")
        #region_selection = ["Select a Region", "Select a Region"]
        #break_selection=["Select Your break Type","Select Your break Type"]
        #self.comboBox.addItems(region_selection) #
        #self.comboBox.addItems(break_selection)
        #self.comboBox.addItem("Select a Region") #
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 80, 281, 31))
        self.comboBox_2.setStyleSheet("QComboBox{\n"
"background-color:rgb(255, 255, 255);\n"
"selection-background-color: rgb(184, 207, 229);\n"
"}")
        self.comboBox_2.setObjectName("comboBox_2")
        #domain_selection = ["Ecommerce","Core PHP","Pc Team","Support","Training","IT Team","Meeting","Email Check","Handover","Activity"]
        #break_type = ["Lunch","Flexi Break"]
        #self.comboBox_2.addItems(domain_selection) # 
        #self.comboBox_2.addItems(break_type)                     
        #self.comboBox_2.addItem("Activity")
        self.pushButton = QtWidgets.QPushButton(Dialog,clicked = lambda: self.on_click())
        self.pushButton.clicked.connect(self.action)#
        self.pushButton.setGeometry(QtCore.QRect(0, 170, 301, 31))
        self.pushButton.setStyleSheet("QPushButton{\n"
"border : 1px solid;\n"
"border-color:rgb(111, 118, 134);\n"
"background-color:rgb(255, 255, 255);\n"
"border-bottom-style: none;\n"
"text-align: left;\n"
"}"
"QPushButton::pressed{\n"
"background-color :rgba(184,207,229,255);"
"}")

        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog,clicked = lambda: self.on_clicked())
        self.pushButton_2.clicked.connect(self.Break)#
        self.pushButton_2.setGeometry(QtCore.QRect(0, 200, 301, 31))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"border : 1px solid;\n"
"border-color:rgb(111, 118, 134);\n"
"background-color:rgb(255, 255, 255);\n"
"border-top-style: none;\n"
"border-bottom-style: none;\n"
"text-align: left;\n"
"}"
"QPushButton::pressed{\n"
"background-color :rgba(184,207,229,255);"
"}")

        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(280, 270, 20, 21))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../../../Downloads/New folder (1)/New folder/refresh.png"))
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(120, 130, 51, 21))
        self.label_8.setStyleSheet("border-bottom-style: none;")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("../../../Downloads/New folder (1)/New folder/done.png"))
        self.label_8.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def action(self):
        # showing the pop up
        region_selection = ["Select a Region", "Select a Region"]
        domain_selection = ["Ecommerce","Core PHP","Pc Team","Support","Training","IT Team","Meeting","Email Check","Handover","Activity"]
        self.comboBox.clear()
        self.comboBox_2.clear()
        self.comboBox.addItems(region_selection)
        self.comboBox_2.addItems(domain_selection)
        self.comboBox_2.showPopup()
        self.comboBox.showPopup()

    def Break(self):
        # showing the pop up        
        break_selection=["Select Your break Type","Select Your break Type"]
        break_type = ["Lunch","Flexi Break"]
        self.comboBox.clear()
        self.comboBox_2.clear()
        self.comboBox.addItems(break_selection)
        self.comboBox_2.addItems(break_type)
        self.comboBox_2.showPopup()
        self.comboBox.showPopup()

    @pyqtSlot()
    def on_click(self):
        self.label.setText('Idle New(IN001)                                                     ')
        self.label.adjustSize()
  
    def on_clicked(self):#
        self.label.setText('Breaks(IN002)                                                         ')
        self.label.adjustSize()
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Idle New(IN001)"))
        self.pushButton_2.setText(_translate("Dialog", "Breaks(IN002)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())