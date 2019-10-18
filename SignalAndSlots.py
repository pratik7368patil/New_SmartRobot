import sys
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Identify_query import Recognize_voice
from s_2_t import ui_path_fun
from quick_book_v1 import exter_book_quick_play
import pyttsx3


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
        self.setStyleSheet("background-color: white;")
        self.setWindowIcon(QtGui.QIcon("play_icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.CreateButton()

        self.show()

    def CreateButton(self):
        button = QPushButton("Add New User", self)
        button.setStyleSheet("QPushButton { font-size: 30px; color: black; border-radius: 5px; border: 4px solid "
                             "black; }")
        button.setGeometry(QRect(25, 25, 230, 100))
        button.clicked.connect(self.add_new_user)

        button = QPushButton("Play Me", self)
        button.setStyleSheet("QPushButton { font-size: 30px; color: black; border-radius: 5px; border: 4px solid "
                             "black;}")
        button.setGeometry((QRect(355, 25, 230, 100)))
        button.clicked.connect(self.ClickMe)

        button = QPushButton("", self)
        button.setStyleSheet("QPushButton { font-size: 30px; color: black; border-radius: 50px; border: 4px solid "
                             "black; }")
        button.setGeometry(QRect(685, 25, 100, 100))
        button.setIcon(QtGui.QIcon("play_icon.png"))
        button.clicked.connect(self.quick_play)

    def ClickMe(self):
        engine = pyttsx3.init()
        engine.say("Hello, What can I do for you?")
        _data = Recognize_voice()

        if _data == "book bus for me" or _data == "book bus" or _data == "bus for me":
            ui_path_fun()
        else:
            engine = pyttsx3.init()
            print("Sorry this is beyond my abilities.")
            engine.say("This is beyond my abilities.")
            engine.runAndWait()

    def quick_play(self):
        alert = QMessageBox()
        alert.setWindowTitle("Quick Play")
        alert.setText('This is Quick play Button!')
        alert.exec_()
        exter_book_quick_play()

    def add_new_user(self):
        print("Hello world")


App = QApplication(sys.argv)
App.setStyle('Fusion')
window = Window()

sys.exit(App.exec())
