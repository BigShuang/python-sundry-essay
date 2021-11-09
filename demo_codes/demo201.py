from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.show()

sys.exit(app.exec_())
