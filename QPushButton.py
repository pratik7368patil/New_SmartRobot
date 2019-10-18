from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtGui


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "Push Button"
        left = 500
        top = 200
        width = 1200
        height = 800
        iconName = "play_icon.png"

        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(left, top, width, height)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        button = QPushButton("", self)
        button.setGeometry(50, 50, 200, 50)
        button.setIcon(QtGui.QIcon("play_icon.png"))
        button.setToolTip("<h2>Play Me</h2>")


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
