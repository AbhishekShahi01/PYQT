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

class UI4(QMainWindow):
	def __init__(self):
		super(UI4, self).__init__()
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

		# Load the ui file
		uic.loadUi("signin.ui", self)

		
		# Show The App
		self.show()



	

	
# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI4()
app.exec_()


