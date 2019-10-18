from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtCore


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Layout Management "
        self.top = 100
        self.left = 100
        self.width = 1200
        self.height = 800

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("play_icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

    def createLayout(self):
        self.groupBox = QGroupBox("What is your Fev Sports?")
        hboxlayout = QHBoxLayout()

        button = QPushButton("Football", self)
        button.setIcon(QtGui.QIcon("play_icon.png"))
        button.setIconSize(QtCore.QSize(40, 40))
        button.setMinimumHeight(40)
        hboxlayout.addWidget(button)

        button1 = QPushButton("Cricket", self)
        button1.setIcon(QtGui.QIcon("play_icon.png"))
        button1.setIconSize(QtCore.QSize(40, 40))
        button1.setMinimumHeight(40)
        hboxlayout.addWidget(button1)

        button3 = QPushButton("Tennis", self)
        button3.setIcon(QtGui.QIcon("play_icon.png"))
        button3.setIconSize(QtCore.QSize(40, 40))
        button3.setMinimumHeight(40)
        hboxlayout.addWidget(button3)

        self.groupBox.setLayout(hboxlayout)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
