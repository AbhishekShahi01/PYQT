from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
  
  
class Window(QMainWindow):
  
    def __init__(self):
        super().__init__()
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # setting title
        self.setWindowTitle("Python ")
  
        # setting geometry
        self.setGeometry(100, 100, 600, 400)
  
        # calling method
        self.UiComponents()
  
        # showing all the widgets
        self.show()
        
  
    # method for widgets
    def UiComponents(self):
  
        # creating a combo box widget
        #self.combo_box = QComboBox(self)
        #self.combo_box1 = QComboBox(self)
        
        # setting geometry of combo box
        #self.combo_box.setGeometry(200, 150, 120, 30)
        #self.combo_box1.setGeometry(300, 200, 250, 50)
        # geek list
        #geek_list = ["Geek", "Geeky Geek", "Legend Geek", "Ultra Legend Geek"]
  
        #lunch_list=["fexible break","lunch"]
        
        # adding list of items to combo box
        #self.combo_box.addItems(geek_list)
        #self.combo_box1.addItems(lunch_list)
        
        # by default label will display at top left corner
        self.label = QLabel('This is label', self)
        
        # creating push button
        #button = QPushButton("idle !", self)
        button1 = QPushButton("break!", self)
      
        # adding action to the button
        #button.pressed.connect(self.action)
        #button1.pressed.connect(self.action)

  
# create pyqt5 app
App = QApplication(sys.argv)
# create the instance of our Window
window = Window()
  
# start the app
sys.exit(App.exec())







