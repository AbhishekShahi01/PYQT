import sys
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QTimer

class MyApp(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('My ProgressBar')
		self.window_width, self.window_height = 1200, 200
		self.setMinimumSize(self.window_width, self.window_height)
		self.increment = 0

		layout = QVBoxLayout()
		self.setLayout(layout)

		self.progressBar = QProgressBar()
		layout.addWidget(self.progressBar)

		self.btn = QPushButton('Start')
		self.btn.clicked.connect(self.pauseResume)
		layout.addWidget(self.btn)

		self.timer = QTimer(self)

	def resumeOperation(self):
		if self.increment >= 100:
			self.timer.stop()
		else:
			self.increment += 1
			self.progressBar.setValue(self.increment)

	def pauseResume(self):
		if self.timer.isActive():
			self.timer.stop()
			self.btn.setText('Resume')
		else:
			self.timer.timeout.connect(self.resumeOperation)
			self.btn.setText('Pause')
			self.timer.start(100)

if __name__ == '__main__':	
	app = QApplication(sys.argv)
	app.setStyleSheet('''
		QWidget {
			font-size: 30px;
		}
	''')
	myApp = MyApp()
	myApp.show()

	try:
		sys.exit(app.exec_())
	except SystemExit:
		print('Closing Window...')
		

