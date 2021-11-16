from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal

import sys


class Window_A(QWidget):
    sign_two = pyqtSignal(str)

    def __init__(self):
        super(Window_A, self).__init__()
        self.resize(300, 200)
        self.init_gui()

    def init_gui(self):
        label = QLabel("Login Page", self)
        label.move(40, 20)

        input_label = QLabel("Enter your name", self)
        input_label.move(20, 50)

        self.input_form = QLineEdit("", self)
        self.input_form.move(20, 80)

        self.button = QPushButton('confirm', self)
        self.button.move(40, 110)
        self.button.clicked.connect(self.click_button)

    def click_button(self):
        name = self.input_form.text()
        self.sign_two.emit(name)
        self.hide()


class Window_B(QWidget):

    def __init__(self):
        super(Window_B, self).__init__()
        self.name = ""
        self.init_gui()

    def init_gui(self):
        label = QLabel("Welcome", self)
        label.move(40, 20)

        self.name_label = QLabel(self.name, self)
        self.name_label.move(40, 50)


    def method_handle_sign2(self, name):
        self.name = name
        self.name_label.setText(self.name)
        self.show()


app = QApplication(sys.argv)

win_a  = Window_A()
win_b = Window_B()

win_a.sign_two.connect(win_b.method_handle_sign2)

win_a.show()

sys.exit(app.exec_())
