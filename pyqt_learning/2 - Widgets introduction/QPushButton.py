from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMenu
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('Pyqt6 QPushButton')
        self.setWindowIcon(QIcon('../images/OIP.jpg'))
        self.create_button()

    def create_button(self):
        btn = QPushButton('Click', self)
        btn.setGeometry(100, 100, 130, 130)
        btn.setFont(QFont('Times', 14, QFont.Weight.ExtraBold))
        btn.setIcon(QIcon('../images/OIP.jpg'))
        btn.setIconSize(QSize(100 ,50))

        #popup menu
        menu = QMenu()
        menu.setFont(QFont('Times', 14, QFont.Weight.ExtraBold))
        menu.setStyleSheet('background-color:gray')
        menu.addAction("Copy")
        menu.addAction("Cut")
        menu.addAction("Paste")
        btn.setMenu(menu)




app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
