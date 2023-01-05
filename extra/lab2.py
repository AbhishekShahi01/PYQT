from PyQt5.QtWidgets import QMainWindow, QApplication, QLCDNumber
from PyQt5 import uic
import sys
from PyQt5.QtCore import QTime, QTimer
from datetime import datetime
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
import datetime
import time
import pyautogui
import random


start = datetime.datetime.now()
class UI(QMainWindow):

    def __init__(self):
    	super(UI, self).__init__()
    	self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    	self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    	uic.loadUi("window1.ui", self)
    	self.label = self.findChild(QLabel, "label_4")
    	font = QFont('Arial', 20, QFont.Bold)
    	self.label_4.setAlignment(Qt.AlignCenter)
    	self.label_4.setFont(font)
    	self.timers = QTimer()
    	self.timers.timeout.connect(self.Time)
    	self.timers.start(1000)
    	self.label = self.findChild(QLabel, "label_2")
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
    	self.button = self.findChild(QPushButton, "pushButton_2")
    	self.button.clicked.connect(self.showTime)
    	self.button.clicked.connect(self.Start)
    	self.show()

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


    def Time(self):
  
        # getting current time
        current_time = QTime.currentTime()
        
        
        # converting QTime object to string
        label_time = current_time.toString('hh:mm:ss')
  
        # showing it to the label
        self.label_4.setText(label_time)

    def mousePressEvent(self, event):
      if event.button() == Qt.LeftButton:
        self.moveFlag = True
        self.movePosition = event.globalPos() - self.pos()
        self.setCursor(QCursor(Qt.OpenHandCursor))
        event.accept()

    def mouseMoveEvent(self, event):
      if Qt.LeftButton and self.moveFlag:
        self.move(event.globalPos() - self.movePosition)
        event.accept()

    def mouseReleaseEvent(self, event):
        self.moveFlag = False
        self.setCursor(Qt.CrossCursor)

	
# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()

