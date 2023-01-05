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
from PyQt5 import QtWidgets

start = datetime.datetime.now()


class UI(QMainWindow):

    def __init__(self):
        super(UI, self).__init__()
        self.window1 = UI2()
        #self.window1 = UI2()
        #self.window2 = AnotherWindow()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        uic.loadUi("window1.ui", self)
        self.label = self.findChild(QLabel, "label_3")
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
        self.button.clicked.connect(self.screenshot)
        #self.button.clicked.connect(self.Re_set)
        self.button1 = self.findChild(QPushButton, "pushButton")
        self.sub_window = UI2()
        self.button1.clicked.connect(self.sub_window.show)
        self.button2 = self.findChild(QPushButton, "pushButton_5")
        self.sub_window2 = UI4()
        self.button2.clicked.connect(self.sub_window2.show)
        self.button3 = self.findChild(QPushButton, "pushButton_3")
        self.button3.clicked.connect(self.close)
        self.button4 = self.findChild(QPushButton, "pushButton_4")
        self.button4.clicked.connect(self.hideWindow)
        # self.UI2.show()
        #self.show()
    def hideWindow(self):
        self.showMinimized()

    def gotowin2(self):
        secwin = UI2()
        widget.addWidget(secwin)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def showTime(self):
        # checking if flag is true
        if self.flag:
            # incrementing the counter
            #self.count+= 1
            self.elapsed_seconds = (datetime.datetime.now() - start).total_seconds()
            self.hour = int(self.elapsed_seconds // 3600)
            self.min = int(self.elapsed_seconds % 3600 // 60)
            self.seconds = int(self.elapsed_seconds % 60)
            self.count = '{:02d}:{:02d}'.format(self.hour, self.min)
            # self.lcd.display(timer)
            # getting text from count
        text = str(self.count)

        # showing text
        self.label_2 .setText(text)

    def Start(self):

        # making flag to true
        self.flag = True

    # def Re_set(self):
    #     # making flag to false
    #     self.flag = False
    #     # reseeting the count
    #     self.count = '{:02d}:{:02d}'.format(0,0,0)
    #     # setting text to label
    #     self.label.setText(str(self.count))

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
        self.setCursor(Qt.PointingHandCursor)#CrossCursor#ArrowCursor




class UI2(QMainWindow):
    def __init__(self):
        super(UI2, self).__init__()
        #self.windows = UI()
        # Load the ui file
        uic.loadUi("window2.ui", self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.action)
        self.button.clicked.connect(self.on_click)
        #self.button.clicked.connect(self.passingInformation)

        self.button1 = self.findChild(QPushButton, "pushButton_2")
        self.button1.clicked.connect(self.Break)
        self.button1.clicked.connect(self.on_clicked)
        #self.button1.clicked.connect(self.passingInformation2)

        # self.show()

    def action(self):
        # showing the pop up
        region_selection = ["Select a Region", "Select a Region"]
        domain_selection = ["Ecommerce", "Core PHP", "Pc Team", "Support",
                            "Training", "IT Team", "Meeting", "Email Check", "Handover", "Activity"]
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
        self.label.setText(
            'Idle New(IN001)                                                     ')
        self.label.adjustSize()

    def on_clicked(self):
        self.label.setText(
            'Breaks(IN002)                                                         ')
        self.label.adjustSize()

    

    # def passingInformation(self):
    #     self.secndwindow.label_3.setText('Idle New(IN001)')
    # def passingInformation2(self):
    #     self.secndwindow.label_3.setText('Breaks(IN002)')

class UI4(QMainWindow):
    def __init__(self):
        super(UI4, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Load the ui file
        uic.loadUi("signin.ui", self)




if __name__ == '__main__':
     app = QApplication([])
     window = UI()
     window.show()
     sys.exit(app.exec_())
# Initialize The App
#app = QApplication(sys.argv)
#UIWindow = UI()
#app.exec_()
#mainwin = UI()
# widget = QtWidgets.QStackedWidget()
# widget.addWidget(mainwin)
# widget.setFixedHeight(800)
# widget.setFixedWidth(1200)
# widget.setVisible(False)
# widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
# widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
# widget.show()
# try:
#     sys.exit(app.exec_())
# except:
#     print("Exiting")

