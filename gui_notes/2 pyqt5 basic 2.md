## pyqt5笔记 初级
### 4 使用类Class
当写的代码一多起来，
使用类Class的继承重写等等，来编写组织代码会更好。
这个更进一步，就是面向对象编程的思想。


比如使用类Class的写法,
重新写下基础部分第三节的总代码

```python
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

import sys

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.resize(300, 200)
        self.init_gui()

        self.button.clicked.connect(self.click_button)

        self.show()

    def init_gui(self):
        self.label = QLabel("Label Text", self)
        self.label.move(40, 20)

        self.button = QPushButton('Button', self)
        self.button.move(150, 20)

        self.img_label = QLabel(self)
        pixmap = QPixmap('my_logo.png')
        self.img_label.setPixmap(pixmap)
        self.img_label.move(20, 50)

    def click_button(self):
        self.label.setText("Clicked")

app = QApplication(sys.argv)

mywindow = MyWindow()

sys.exit(app.exec_())
```

### 5 键盘点击事件
要写键盘点击事件
需要继承窗口类，并重写自己的`keyPressEvent`方法。

```python
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

import sys

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.resize(300, 200)

        self.add_widgets()
        self.show()

    def add_widgets(self):
        self.label = QLabel("Label Text", self)
        self.label.move(40, 20)

        self.button = QPushButton('Button', self)
        self.button.move(150, 20)

        self.img_label = QLabel(self)
        pixmap = QPixmap('my_logo.png')
        self.img_label.setPixmap(pixmap)
        self.img_label.move(20, 50)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_K:
            self.label.setText("Press K")

app = QApplication(sys.argv)
mywindow = MyWindow()

sys.exit(app.exec_())
```
此时按键盘上的`K`键， `label`标签会展示`Press K`。
