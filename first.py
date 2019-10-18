from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "SmartRobot"
        self.top = 100
        self.left = 100
        self.width = 1200
        self.height = 800

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("play_icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()


App = QApplication(sys.argv)
window = Window()

sys.exit(App.exec())
