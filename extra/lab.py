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


class UI2(QMainWindow):
	def __init__(self):
		super(UI2, self).__init__()

		# Load the ui file
		uic.loadUi("window2.ui", self)
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

		self.button = self.findChild(QPushButton, "pushButton")
		self.button.clicked.connect(self.action)
		self.button.clicked.connect(self.on_click)

		self.button1 = self.findChild(QPushButton, "pushButton_2")
		self.button1.clicked.connect(self.Break)
		self.button1.clicked.connect(self.on_clicked)

    	

		
		self.show()


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
		break_selection=["Select Your break Type","Select Your break Type"]
		break_type = ["Lunch","Flexi Break"]
		self.comboBox.clear()
		self.comboBox_2.clear()
		self.comboBox.addItems(break_selection)
		self.comboBox_2.addItems(break_type)
		self.comboBox_2.showPopup()
		self.comboBox.showPopup()


  
	def on_click(self):
		self.label.setText('Idle New(IN001)                                                     ')
		self.label.adjustSize()

	def on_clicked(self):
		self.label.setText('Breaks(IN002)                                                         ')
		self.label.adjustSize()




         
	    


    




	


	
# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI2()
app.exec_()
