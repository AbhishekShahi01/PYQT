import sys

from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 300)

    def location_on_the_screen(self):
        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()

        widget = self.geometry()
        x = ag.width() - widget.width()
        y = 2 * ag.height() - sg.height() - widget.height()
        self.move(x, y)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.location_on_the_screen()
    widget.show()
    app.exec_()
