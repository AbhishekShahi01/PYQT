

from PyQt5 import QtCore, QtGui, QtWidgets
from window2 import Ui_Dialog
#from pop import Ui_WizardPage
from PyQt5.QtWidgets import QMainWindow, QApplication, QLCDNumber
from PyQt5 import uic
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtCore import QTime, QTimer
#from datetime import datetime
import pyautogui
import random
import time
import datetime
import sys

start = datetime.datetime.now() 

class Ui_mainWindow(QMainWindow):
    def openWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWizard(self):
        self.wizard = QtWidgets.QWizardPage()
        self.ui = Ui_WizardPage()
        self.ui.setupUi(self.wizard)
        self.wizard.show()

    
    # def __init__(self):

    #     super().__init__()
    #     #self.ui = uic.loadUi('window1.ui')
    #def setupUi(self, mainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(422, 390)
        #self.setWindowFlag(Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 40, 311, 41))
        self.label.setStyleSheet("QLabel{\n"
" border : 1px solid;\n"
" border-color:rgb(215, 184, 0);\n"
"}")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../Downloads/New folder (1)/New folder/image14.png"))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 0, 311, 41))
        self.label_3.setStyleSheet("QLabel{\n"
" border : 1px solid;\n"
" border-color:rgb(215, 184, 0);\n"
"}")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../../Downloads/New folder (1)/New folder/image7.png"))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 111, 81))
        self.label_5.setStyleSheet("QLabel{\n"
" border : 1px solid;\n"
" border-color:rgb(215, 184, 0);\n"
"}")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.openWindow())
        self.pushButton.setGeometry(QtCore.QRect(330, 10, 21, 21))
        self.pushButton.setStyleSheet("QPushButton{\n"
"border-style:hidden;\n"
"background-color:rgb(254, 222, 5);\n"
"}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Downloads/New folder (1)/New folder/image4.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.openWizard())
        # adding action to a button
        self.pushButton_2.clicked.connect(self.showTime)
        self.pushButton_2.clicked.connect(self.Start)
        self.pushButton_2.clicked.connect(self.screenshot)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 0, 41, 41))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
" border : 1px solid;\n"
" border-color:rgb(215, 184, 0);\n"
"border-bottom-style: none;\n"
"border-top-style: none;\n"
"border-left-style: none;\n"
"}")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../Downloads/New folder (1)/New folder/image10.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 0, 61, 41))
        self.label_2.setStyleSheet("QLabel{\n"
" border : 1px solid;\n"
" border-color:rgb(215, 184, 0);\n"
"border-bottom-style: none;\n"
"border-top-style: none;\n"
"border-right-style: none;\n"
"padding-left :8px;\n"
"}")    
        # counter
        self.count = 0
        # creating flag
        self.flag = False
        self.label_2.setText(str(self.count))
        # creating a timer object
        self.label_2.setFont(QFont('sans-serif', 10))
        self.timer = QTimer()
        # adding action to timer
        self.timer.timeout.connect(self.showTime)
        # update the timer every tenth second
        self.timer.start(1000)
        #self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 40, 161, 41))
        self.label_4.setStyleSheet("QLabel{\n"
"border-style:hidden;\n"
"font-weight: bold;\n"
"}")    
        # creating font object
        font = QFont('Arial', 20, QFont.Bold)
  
        # setting centre alignment to the label
        self.label_4.setAlignment(Qt.AlignCenter)
  
        # setting font to the label
        self.label_4.setFont(font)
  
        # creating a timer object
        self.timers = QTimer()
  
        # adding action to timer
        self.timers.timeout.connect(self.Time)
  
        # update the timer every second
        self.timers.start(1000)

        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 20))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def showTime(self):#
        # checking if flag is true
        if self.flag:
            # incrementing the counter
            #self.count+= 1
            self.elapsed_seconds = (datetime.datetime.now() - start).total_seconds()
            self.hour = int(self.elapsed_seconds // 3600)
            self.min = int(self.elapsed_seconds % 3600 // 60)
            self.seconds = int(self.elapsed_seconds % 60)
            self.count ='{:02d}:{:02d}'.format(self.hour, self.min)
            #self.lcd.display(timer)
            # getting text from count
        text = str(self.count)
  
        # showing text
        self.label_2 .setText(text)

    def Start(self):
  
        # making flag to true
        self.flag = True



    # method called by timer
    def Time(self):
  
        # getting current time
        current_time = QTime.currentTime()
        
        
        # converting QTime object to string
        label_time = current_time.toString('hh:mm:ss')
  
        # showing it to the label
        self.label_4.setText(label_time)

    def screenshot(self):
        if self.flag==True:
                # generating a random number between 1 
                # to 10 which will represent the time 
                # delay
                random_time = random.randint(1, 5)
  
                # create a time delay using the sleep()
                # method
                time.sleep(random_time)
  
                # Take the screenshot using screenshot()
                # method
                myScreenshot = pyautogui.screenshot()
  
                # Save the screenshot shot using current
                # time as file name.
                file_name = str(time.time())+".png"
                myScreenshot.save(file_name)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    #ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
#https://www.pythonguis.com/tutorials/creating-multiple-windows/#:~:text=This%20means%2C%20to%20show%20a,QMainWindow%20instances%20you%20can%20have.
#https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/