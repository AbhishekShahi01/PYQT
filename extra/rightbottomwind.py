
from PyQt5.QtWidgets import QMainWindow, QApplication, QLCDNumber,QWidget, QDesktopWidget, QLabel
from PyQt5 import uic
import sys
from PyQt5.QtCore import QTime, QTimer
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

		# Load the ui file
		uic.loadUi("screenshot.ui", self)
		self.show()
		QtCore.QTimer.singleShot(4000, self.close)

		# self.label0 = self.findChild(QLabel, "label_2")
		# self.label1 = self.findChild(QLabel, "label")
		# self.label2 = self.findChild(QLabel, "label_3")

		



		# self.show()

		# waiting for 2 second
		#time.sleep(2)

		# closing the window
		#self.close()


	def location_on_the_screen(self):
		ag = QDesktopWidget().availableGeometry()
		sg = QDesktopWidget().screenGeometry()
		widget = self.geometry()
		x = ag.width() - widget.width()
		y = 7 * ag.height() - sg.height() - widget.height()
		self.move(x, y)
	
# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
#self.show()
#UIWindow.close()
UIWindow.location_on_the_screen()
app.exec_()

