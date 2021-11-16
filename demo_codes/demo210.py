from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *

import sys

imgpath = "./gui_notes/imgs/my_logo.png"

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.resize(300, 200)
        self.init_gui()

        self.item = None
        self.show()

    def init_gui(self):
        box = QVBoxLayout()
        label = QLabel("Label Text", self)

        self.view = QGraphicsView()
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        box.addWidget(label)
        box.addWidget(self.view)

        self.set_view()
        self.setLayout(box)

    def set_view(self):
        self.item = QGraphicsPixmapItem()  # 新建QGraphicsPixmapItem对象用于显示图片
        self.item.setPixmap(QPixmap(imgpath))  # 设置位图
        self.item.setPos(100, 100)  # 设置图片位置
        self.scene.addItem(self.item)  # 添加图片到scene中

        self.view.setFixedSize(300, 300)  # 设置view为固定尺寸 300x300
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) # 关闭水平方向滚动条
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 关闭竖直方向滚动条

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_D:
            print("d")
            if self.item:
                self.scene.removeItem(self.item)
                self.item.hide()

        # self.scene.update()
        # self.view.update()


app = QApplication(sys.argv)
win = MyWindow()
sys.exit(app.exec_())
