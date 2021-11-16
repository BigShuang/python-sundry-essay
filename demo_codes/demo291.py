from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal

import sys


class Window_B(QWidget):
    sign_three = pyqtSignal(dict)

    def __init__(self):
        super(Window_B, self).__init__()

        self.name = "BigShuang"
        self.level = 1
        self.score = 0

        self.setWindowTitle("Game")
        self.resize(300, 200)
        self.init_gui()

    def init_gui(self):
        label1 = QLabel("Welcome", self)
        label1.move(40, 20)

        self.name_label = QLabel(self.name, self)
        self.name_label.move(40, 50)

        label2 = QLabel("Choose one button", self)
        label2.move(40, 80)

        button_1 = QPushButton("1", self)
        button_1.move(20, 110)

        button_2 = QPushButton("2", self)
        button_2.move(150, 110)

        button_1.clicked.connect(self.ending_1)
        button_2.clicked.connect(self.ending_2)

    def ending_1(self):
        self.score += 10
        self.send_info()

    def ending_2(self):
        self.score += 20
        self.send_info()

    def send_info(self):
        info = {
            "name": self.name,
            "level": self.level,
            "score": self.score
        }
        self.hide()
        self.sign_three.emit(info)

    def next_level(self):
        self.level += 1
        self.show()


class Window_C(QWidget):
    sign_four = pyqtSignal()

    def __init__(self):
        super(Window_C, self).__init__()

        self.resize(300, 200)
        self.setWindowTitle("Result")
        self.init_gui()

    def init_gui(self):
        label1 = QLabel("Name: ", self)
        label2 = QLabel("Level: ", self)
        label3 = QLabel("score: ", self)
        self.name_label = QLabel("", self)
        self.level_label = QLabel("", self)
        self.score_label = QLabel("", self)

        button = QPushButton("Next Level", self)

        label1.move(20, 20)
        label2.move(20, 50)
        label3.move(20, 80)

        self.name_label.move(100, 20)
        self.level_label.move(100, 50)
        self.score_label.move(100, 80)

        button.move(60, 110)
        button.clicked.connect(self.click_button)

    def show_result(self, info):
        self.name_label.setText(info["name"])
        self.level_label.setText(str(info["level"]))
        self.score_label.setText(str(info["score"]))

        self.show()

    def click_button(self):
        self.sign_four.emit()

app = QApplication(sys.argv)

win_b = Window_B()
win_c = Window_C()

win_b.sign_three.connect(win_c.show_result)
win_c.sign_four.connect(win_b.next_level)
win_c.sign_four.connect(win_c.hide)

win_b.show()

sys.exit(app.exec_())
