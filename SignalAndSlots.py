import sys
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Identify_query import Recognize_voice
from s_2_t import ui_path_fun
from quick_book_v1 import exter_book_quick_play


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Event and Signal "
        self.top = 100
        self.left = 100
        self.width = 1200
        self.height = 800

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("play_icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.CreateButton()

        self.show()

    def CreateButton(self):
        button = QPushButton("Add New User", self)
        button.setGeometry(QRect(25, 25, 200, 50))
        button.clicked.connect(self.add_new_user)

        button = QPushButton("Play Me", self)
        button.setGeometry(QRect(25, 250, 200, 50))
        button.setIcon(QtGui.QIcon("play_icon.png"))
        button.clicked.connect(self.ClickMe)

        button = QPushButton("Quick Book", self)
        button.setGeometry((QRect(25, 500, 200, 50)))
        button.clicked.connect(self.quick_play)

    def ClickMe(self):
        _data = Recognize_voice()

        if _data == "book bus for me" or _data == "book bus" or _data == "bus for me":
            ui_path_fun()
        else:
            print("Hello")

    def quick_play(self):
        alert = QMessageBox()
        alert.setText('This is Quick play Button!')
        alert.exec_()
        exter_book_quick_play()

    def add_new_user(self):
        print("Hello world")


App = QApplication(sys.argv)
App.setStyle('Fusion')
window = Window()

sys.exit(App.exec())
