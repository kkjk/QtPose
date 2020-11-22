import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QLineEdit, QHBoxLayout, QSplitter


class MyMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Splitter"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        hbox = QHBoxLayout()
        self.widg_1 = QFrame()
        self.widg_1.setFrameShape(QFrame.StyledPanel)
        self.my_splitter = QSplitter(Qt.Horizontal)
        self.widg_2 = QLineEdit()
        self.my_splitter.addWidget(self.widg_1)
        self.my_splitter.addWidget(self.widg_2)
        self.my_splitter.setSizes([200, 200])
        hbox.addWidget(self.my_splitter)
        # Note: splitter handle 0 is always hidden and handle 1 is between the widgets 1 & 2
        self.my_splitter_handle = self.my_splitter.handle(1)
        self.my_splitter.setStyleSheet("QSplitter::handle {background: 3px blue};")
        self.setLayout(hbox)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()


App = QApplication(sys.argv)
window = MyMainWindow()
sys.exit(App.exec())