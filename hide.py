from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit,QLabel,QComboBox
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
from PyQt5 import QtWidgets


import glob
folder_dir = 'Screenshot'
image_list = []

DURATION_INT = 4

#start = datetime.datetime.now()


from threading import Timer


class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()
		#self.window1 = UI2()
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.start = datetime.datetime.now()

		# Load the ui file
		uic.loadUi("trail.ui", self)
		self.label = self.findChild(QLabel, "label_4")
		font = QFont('Arial', 20, QFont.Bold)
		self.label_4.setAlignment(Qt.AlignCenter)
		self.label_4.setFont(font)
		self.timers = QTimer()
		self.timers.timeout.connect(self.Time)
		self.timers.start(1000)
		self.label = self.findChild(QLabel, "label_2")
		# counter
		self.count = 0     #'{:02d}:{:02d}'.format(0,0)
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
		self.buttonmainwin = self.findChild(QPushButton, "pushButton_2")
		self.buttonmainwin.clicked.connect(self.showTime)
		self.buttonmainwin.clicked.connect(self.Start)
		self.buttonmainwin.clicked.connect(self.screenshot)
		self.buttonmainwin.clicked.connect(self.Re_set)
		#->self.button.clicked.connect(self.unhidescreenshot)
		self.button3 = self.findChild(QPushButton, "pushButton_3")
		self.button3.clicked.connect(self.close)
		self.button4 = self.findChild(QPushButton, "pushButton_4")
		self.button4.clicked.connect(self.hideWindow)
		#main window
		#assendingimages = []
		self.label20 = self.findChild(QLabel, "label_5")
		for images in glob.iglob(f'{folder_dir}/*'):
			if (images.endswith(".png")):
				image_list.append(images)
				assendingimages = sorted(image_list)
		#print(image_list)
		#print(self.assendingimages[-1])
		self.label20.setPixmap(QPixmap(assendingimages[-1]))
		self.label20.setScaledContents(True)		


		#self.pixmap = QPixmap('image1.png')
		#self.label20.setPixmap(self.pixmap)
		#self.label20.setScaledContents(True)


		self.label21 = self.findChild(QLabel, "label_4")
		self.label22 = self.findChild(QLabel, "label")
		self.label23 = self.findChild(QLabel, "label_2")
		self.label24 = self.findChild(QLabel, "label_15")
		self.label25 = self.findChild(QLabel, "label_3")
		self.button7 = self.findChild(QPushButton, "pushButton_2")
		self.button8 = self.findChild(QPushButton, "pushButton")
		self.line_edit4 = self.findChild(QLineEdit, "lineEdit_5")
		self.line_edit4.setHidden(True)
		self.label26 = self.findChild(QLabel, "label_6")
		self.label27 = self.findChild(QLabel, "label_7")
		self.button17 = self.findChild(QPushButton, "pushButton_5")
		self.button18 = self.findChild(QPushButton, "pushButton_4")
		self.button19 = self.findChild(QPushButton, "pushButton_3")
		#for projection selection
		self.label0 = self.findChild(QLabel, "label_8")
		self.label0.setHidden(True)
		self.line_edit3 = self.findChild(QLineEdit, "lineEdit_4")
		self.line_edit3.setHidden(True)
		self.label2 = self.findChild(QLabel, "label_10")
		self.label2.setHidden(True)
		self.label3 = self.findChild(QLabel, "label_11")
		self.label3.setHidden(True)
		self.label4 = self.findChild(QLabel, "label_12")
		self.label4.setHidden(True)
		self.label5 = self.findChild(QLabel, "label_13")
		self.label5.setHidden(True)
		self.label6 = self.findChild(QLabel, "label_14")
		self.label6.setHidden(True)
		self.label7 = self.findChild(QLabel, "label_15")
		#self.label7.setHidden(True)
		self.combobox = self.findChild(QComboBox, "comboBox")
		self.combobox.setHidden(True)
		self.combobox1 = self.findChild(QComboBox, "comboBox_2")
		self.combobox1.setHidden(True)
		self.button = self.findChild(QPushButton, "pushButton_6")
		self.button.setHidden(True)
		self.button1 = self.findChild(QPushButton, "pushButton_7")
		self.button1.setHidden(True)
		self.button = self.findChild(QPushButton, "pushButton_7")
		self.button.clicked.connect(self.action)
		self.button.clicked.connect(self.on_click)
		self.button1 = self.findChild(QPushButton, "pushButton_6")
		self.button1.clicked.connect(self.Break)
		self.button1.clicked.connect(self.on_clicked)
		# Click the buttons
		self.button2 = self.findChild(QPushButton, "pushButton")
		self.button2.clicked.connect(self.unhidden)
		self.button5 = self.findChild(QPushButton, "pushButton_5")
		self.button5.clicked.connect(self.unhiddenlogin)
		self.button5.clicked.connect(self.hidemain)
		#->self.button5.clicked.connect(self.hidescreenshot)
        #when done button clicked
		self.button11 = self.findChild(QPushButton, "pushButton_9")
		self.button11.setHidden(True)
		self.button11.clicked.connect(self.hiddenWhenDone)
        #for sign in
		self.label8 = self.findChild(QLabel, "label_25")
		self.label8.setHidden(True)
		self.label9 = self.findChild(QLabel, "label_17")
		self.label9.setHidden(True)
		self.label10 = self.findChild(QLabel, "label_16")
		self.label10.setHidden(True)
		self.label11 = self.findChild(QLabel, "label_26")
		self.label11.setHidden(True)
		self.label12 = self.findChild(QLabel, "label_27")
		self.label12.setHidden(True)
		self.label13 = self.findChild(QLabel, "label_18")
		self.label13.setHidden(True)
		self.label14 = self.findChild(QLabel, "label_20")
		self.label14.setHidden(True)
		self.line_edit = self.findChild(QLineEdit, "lineEdit")
		self.line_edit.setHidden(True)
		self.line_edit1 = self.findChild(QLineEdit, "lineEdit_2")
		self.line_edit1.setHidden(True)
		self.line_edit2 = self.findChild(QLineEdit, "lineEdit_3")
		self.line_edit2.setHidden(True)
		self.label18 = self.findChild(QLabel, "label_24")
		self.label18.setHidden(True)
		self.label19 = self.findChild(QLabel, "label_22")
		self.label19.setHidden(True)
		self.checkbox = self.findChild(QCheckBox, "checkBox")
		self.checkbox.setHidden(True)
		self.checkbox1 = self.findChild(QCheckBox, "checkBox_2")
		self.checkbox1.setHidden(True)
		self.button3 = self.findChild(QPushButton, "pushButton_8")
		self.button3.setHidden(True)
		self.button6 = self.findChild(QPushButton, "pushButton_8")
		self.button6.clicked.connect(self.hideWindowlogin)

        #for continue with project
		self.label30 = self.findChild(QLabel, "label_9")
		self.label30.setHidden(True)
		self.label31 = self.findChild(QLabel, "label_19")
		self.label31.setHidden(True)
		self.label32 = self.findChild(QLabel, "label_21")
		self.label32.setHidden(True)
		self.label33 = self.findChild(QLabel, "label_23")
		self.label33.setHidden(True)
		self.label34 = self.findChild(QLabel, "label_28")
		self.label34.setHidden(True)
		self.button30 = self.findChild(QPushButton, "pushButton_11")
		self.button30.setHidden(True)
		self.button31 = self.findChild(QPushButton, "pushButton_12")
		self.button31.setHidden(True)

		# self.button30.clicked.connect(self.hideconformation)
		# self.button30.clicked.connect(self.showTime)
		# self.button30.clicked.connect(self.Start)

	def action(self):
		# showing the pop up
		region_selection = ["Select a Region", "Select a Region"]
		domain_selection = ["Ecommerce", "Core PHP", "Pc Team", "Support","Training", "IT Team", "Meeting", "Email Check", "Handover", "Activity"]
		self.comboBox.clear()
		self.comboBox_2.clear()
		self.comboBox.addItems(region_selection)
		self.comboBox_2.addItems(domain_selection)
		self.comboBox_2.showPopup()
		self.comboBox.showPopup()

	def Break(self):
		break_selection = ["Select Your break Type", "Select Your break Type"]
		break_type = ["Lunch", "Flexi Break"]
		self.comboBox.clear()
		self.comboBox_2.clear()
		self.comboBox.addItems(break_selection)
		self.comboBox_2.addItems(break_type)
		self.comboBox_2.showPopup()
		self.comboBox.showPopup()

	def on_click(self):
		self.label_14.setText('Idle New (IN001)')
		self.label_15.setText('Idle New (IN001)')
		#self.label_14.adjustSize()

	def on_clicked(self):
		self.label_14.setText('Breaks (IN002)')
		self.label_15.setText('Breaks (IN002)')
		#self.label_14.adjustSize()
            

	def hideWindow(self):
		self.showMinimized()

	def hideWindowlogin(self):
		self.showMinimized()

	def showTime(self):
		if self.flag == True:
			#self.count+= 1
			self.elapsed_seconds = (datetime.datetime.now() - self.start).total_seconds()
			self.hour = int(self.elapsed_seconds // 3600)
			self.min = int(self.elapsed_seconds % 3600 // 60)
			self.seconds = int(self.elapsed_seconds % 60)
			self.count = '{:02d}:{:02d}'.format(self.hour, self.min)
		text = str(self.count)
		self.label_2 .setText(text)
		
	def Start(self):
		self.flag = True
		#self.button2.setDisabled(True)
		#self.button2.setEnabled(False)
		self.button2.setEnabled(False)
		self.buttonmainwin.setIcon(QIcon('image10.png'))

	def Re_set(self):
		self.flag = False
		self.start = datetime.datetime.now()
		self.count = '{:02d}:{:02d}'.format(0,0)
		self.label.setText(str(self.count))
		self.buttonmainwin.setIcon(QIcon('left_black.png'))
		self.sub_window = UI2()
		self.sub_window.location_on_the_screen() 
		self.buttonmainwin.clicked.connect(self.sub_window.show)
		# self.timer = QTimer()
		# self.timer.timeout.connect(self.hideconformation)
		# self.timer.start(9000)
		self.buttonmainwin.clicked.connect(self.unhideconformation)
		self.button2.setEnabled(True)
		# self.label30.setHidden(False)
		# self.label31.setHidden(False)
		# self.label32.setHidden(False)
		# self.label33.setHidden(False)
		# self.label34.setHidden(False)
		# self.button30.setHidden(False)
		# self.button31.setHidden(False)
		#self.buttonmainwin.clicked.connect(self.showTime)
		#self.buttonmainwin.clicked.connect(self.Start)
		self.button30.clicked.connect(self.hideconformation)
		self.button30.clicked.connect(self.showTime)
		self.button30.clicked.connect(self.Start)
		self.button31.clicked.connect(self.hideconformation)
		



	def Time(self):
		# getting current time
		current_time = QTime.currentTime()
		# converting QTime object to string
		label_time = current_time.toString('hh:mm:ss')
		# showing it to the label
		self.label_4.setText(label_time)

	def screenshot(self):
		myScreenshot = pyautogui.screenshot()
		file_name = str(time.asctime())+".png"
		myScreenshot.save(r'/home/spx072/desktopapp/project/pyqt5/Screenshot/'+file_name)
		Timer(120.0, self.screenshot).start()
	#Timer(10.0, screenshot).start()




		#Timer(30.0, screenshot).start()
	#Timer(30.0, screenshot).start()

		








		# if self.flag==True:
		# #for _ in iter(int, 1):
		# 	# generating a random number between 1
		# 	# to 10 which will represent the time
		# 	# delay
		# 	random_time = random.randint(1, 5)
		# 	# create a time delay using the sleep()
		# 	# method
		# 	time.sleep(random_time)
		# 	# Take the screenshot using screenshot()
		# 	# method
		# 	myScreenshot = pyautogui.screenshot()
		# 	# Save the screenshot shot using current
		# 	# time as file name.
		# 	file_name = str(time.time())+".png"
		# 	myScreenshot.save(file_name)



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
		self.setCursor(Qt.PointingHandCursor)#CrossCursor#ArrowCursor

	

	def hidemain(self):
		self.label20.setHidden(True)
		self.label21.setHidden(True)
		self.label22.setHidden(True)
		self.label23.setHidden(True)
		self.label24.setHidden(True)
		self.label25.setHidden(True)
		self.label26.setHidden(True)
		self.label27.setHidden(True)
		self.button7.setHidden(True)
		self.button8.setHidden(True)
		self.line_edit4.setHidden(True)
		self.button17.setHidden(True)
		self.button18.setHidden(True)
		self.button19.setHidden(True)
		
	def unhiddenlogin(self):
		self.label8.setHidden(False)
		self.label9.setHidden(False)
		self.label10.setHidden(False)
		self.label11.setHidden(False)
		self.label12.setHidden(False)
		self.label13.setHidden(False)
		self.label14.setHidden(False)
		self.line_edit.setHidden(False)
		self.line_edit1.setHidden(False)
		self.line_edit2.setHidden(False)
		self.label18.setHidden(False)
		self.label19.setHidden(False)
		self.checkbox.setHidden(False)
		self.checkbox1.setHidden(False)
		self.button3.setHidden(False)
		#self.line_edit4.setHidden(True)

	def unhidden(self):
		self.label0.setHidden(False)
		self.line_edit3.setHidden(False)
		self.label2.setHidden(False)
		self.label3.setHidden(False)
		self.label4.setHidden(False)
		self.label5.setHidden(False)
		self.label6.setHidden(False)
		self.combobox.setHidden(False)
		self.combobox1.setHidden(False)
		self.button.setHidden(False)
		self.button1.setHidden(False)
		self.button11.setHidden(False)
		self.line_edit4.setHidden(True)

	def hiddenWhenDone(self):
		self.label0.setHidden(True)
		self.line_edit3.setHidden(True)
		self.label2.setHidden(True)
		self.label3.setHidden(True)
		self.label4.setHidden(True)
		self.label5.setHidden(True)
		self.label6.setHidden(True)
		self.combobox.setHidden(True)
		self.combobox1.setHidden(True)
		self.button.setHidden(True)
		self.button1.setHidden(True)
		self.button11.setHidden(True)
		self.line_edit4.setHidden(False)


	def hideconformation(self):
		self.label30.setHidden(True)
		self.label31.setHidden(True)
		self.label32.setHidden(True)
		self.label33.setHidden(True)
		self.label34.setHidden(True)
		self.button30.setHidden(True)
		self.button31.setHidden(True)
		# self.timer = QTimer()
		# self.timer.timeout.connect(self.hideconformation)
		# self.timer.start(9000)

	def unhideconformation(self):
		self.label30.setHidden(False)
		self.label31.setHidden(False)
		self.label32.setHidden(False)
		self.label33.setHidden(False)
		self.label34.setHidden(False)
		self.button30.setHidden(False)
		self.button31.setHidden(False)


class UI2(QMainWindow):
	def __init__(self):
		super(UI2, self).__init__()
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

		# Load the ui file
		uic.loadUi("scpopup.ui", self)


		self.time_left_int = DURATION_INT
		self.widget_counter_int = 0
		self.labelseccount = self.findChild(QLabel, "label_22")
		self.labelseccount.setStyleSheet('font-size: 18pt; color: blue;')
		#vbox = QtWidgets.QVBoxLayout()
		#central_widget.setLayout(vbox)
		#self.pages_qsw = QtWidgets.QStackedWidget()
		#vbox.addWidget(self.pages_qsw)
		#self.time_passed_qll = QtWidgets.QLabel()
		#vbox.addWidget(self.time_passed_qll)
		self.timer_start()
		self.update_gui()
        
    

        
		

		#self.labelseccount = self.findChild(QLabel, "label_22")
		

		self.labelsc = self.findChild(QLabel, "label_19")
		for images in glob.iglob(f'{folder_dir}/*'):
			if (images.endswith(".png")):
				image_list.append(images)
				assendingimages = sorted(image_list)
		#print(image_list)
		#print(self.assendingimages[-1])
		self.labelsc.setPixmap(QPixmap(assendingimages[-1]))
		self.labelsc.setScaledContents(True)

		self.buttonCancel = self.findChild(QPushButton, "pushButton_11")
		self.buttonCancel.clicked.connect(self.hideScreenshot)
		#self.buttontimer = self.findChild(QPushButton, "pushButton")
		self.labelseccount = self.findChild(QLabel, "label_22")
		self.show()
		QtCore.QTimer.singleShot(8000, self.close)

	def timer_start(self):
		self.time_left_int = DURATION_INT
		self.my_qtimer = QtCore.QTimer(self)
		self.my_qtimer.timeout.connect(self.timer_timeout)
		self.my_qtimer.start(2000)
		self.update_gui()

	def timer_timeout(self):
		self.time_left_int -= 1
		if self.time_left_int == 0:
			self.widget_counter_int = (self.widget_counter_int + 1) % 4
			#self.labelseccount.setCurrentIndex(self.widget_counter_int)
			self.time_left_int = DURATION_INT
		self.update_gui()

	def update_gui(self):
		self.labelseccount.setText(str(self.time_left_int))


	def hideScreenshot(self):
		self.showMinimized()



	def location_on_the_screen(self):
		ag = QDesktopWidget().availableGeometry()
		sg = QDesktopWidget().screenGeometry()
		widget = self.geometry()
		x = ag.width() - widget.width()
		y = 6 * ag.height() - sg.height() - widget.height()
		self.move(x, y)
    



# # Initialize The App
# app = QApplication(sys.argv)
# UIWindow = UI()
# #self.show()
# #UIWindow.close()
# UIWindow.location_on_the_screen()
# app.exec_()



if __name__ == '__main__':
    app = QApplication([])
    UIWindow = UI()
    #UIWindow2 = UI2()
    #UIWindow2.hide()
    #UIWindow2.location_on_the_screen()
    UIWindow .show()
    sys.exit(app.exec_())	
# # Initialize The App
# app = QApplication(sys.argv)
# UIWindow = UI()
# app.exec_()
