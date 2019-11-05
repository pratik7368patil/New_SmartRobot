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
        self.width = 2300
        self.height = 1200

        bar = self.menuBar()
        bar_ = QGraphicsDropShadowEffect(self)
        bar_.setBlurRadius(1000)
        bar.setGraphicsEffect(bar_)

        bar.setStyleSheet("font-size: 35px; color: white; border-bottom: 1px solid black;")
        file = bar.addMenu("File")
        add_new_platform = bar.addMenu("Add New Platform")
        history = bar.addMenu("History")
        hw_to_use = bar.addMenu("How to use?")
        hlp = bar.addMenu("Help")

        # for file
        add_data = file.addAction("Add Data")
        setting = file.addAction("Settings")
        qut = QAction("Quit", self)
        file.addAction(qut)

        # for add_new_platform
        f_bus = add_new_platform.addAction("For Bus")
        f_flight = add_new_platform.addAction("For Flight")
        t_b_product = add_new_platform.addAction("To Buy Product")
        t_o_food = add_new_platform.addAction("To Order Food")

        self.InitWindow()

    def InitWindow(self):
        self.setStyleSheet("background-color: #343434")
        self.setWindowIcon(QtGui.QIcon("play_icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.CreateButton()

        self.show()

    def CreateButton(self):
        button = QPushButton("", self)
        button.setStyleSheet("QPushButton {color: white; border-radius: 50px; border: 4px solid "
                             "#4169E1; }")
        button.setGeometry(QRect(1150, 350, 100, 100))
        button.setIcon(QtGui.QIcon("Bubble_icon.png"))
        button.clicked.connect(self.quick_play)

        button = QPushButton("Play me for Bus Booking", self)
        button.setStyleSheet("QPushButton {color: white; font-size: 30px; border: 4px solid "
                             "#4169E1; }")
        button.setGeometry(QRect(150, 350, 500, 100))

        bus_info = QLabel("", self)
        bus_info.setText("Default Query for bus booking is: book bus for me from Mumbai to Pune bus type ordinary on "
                         "23 next month ")
        bus_info.setGeometry(QRect(500, 200, 1500, 40))
        bus_info.setStyleSheet("QLabel {color: white; font-size: 28px; width: 500px; qproperty-alignment: AlignCenter;}")

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

    def close_window(self):
        sys.exit()


App = QApplication(sys.argv)
App.setStyle('Fusion')
window = Window()

sys.exit(App.exec())
