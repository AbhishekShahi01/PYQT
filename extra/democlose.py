from PyQt5 import QtCore, QtWidgets
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Should close")
        QtCore.QTimer.singleShot(0, self.show)


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.close()
app.exec_()
