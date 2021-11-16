from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal

import sys


class Window_A(QWidget):
    sign_one = pyqtSignal()

    def __init__(self):
        super(Window_A, self).__init__()
        self.init_gui()

    def init_gui(self):
        self.label = QLabel("Window A", self)
        self.label.move(40, 20)

        self.button = QPushButton('Open new Window', self)
        self.button.move(150, 20)
        self.button.clicked.connect(self.click_button)

    def click_button(self):
        self.sign_one.emit()
        self.hide()


class Window_B(QWidget):

    def __init__(self):
        super(Window_B, self).__init__()
        self.init_gui()

    def init_gui(self):
        self.label = QLabel("This is window B", self)
        self.label.move(40, 20)

    def method_handle_sign(self):
        self.show()


app = QApplication(sys.argv)

win_a  = Window_A()
win_b = Window_B()

win_a.sign_one.connect(win_b.method_handle_sign)

win_a.show()

sys.exit(app.exec_())
