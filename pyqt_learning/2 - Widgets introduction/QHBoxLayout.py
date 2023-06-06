from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('QHBoxLayout')
        self.setWindowIcon(QIcon('../images/OIP.jpg'))
        # self.setFixedWidth(700)
        # self.setFixedHeight(400)
        # self.setWindowOpacity(0.5)


        hbox = QHBoxLayout()


        btn1 = QPushButton('Click one')
        btn2 = QPushButton('Click two')
        btn3 = QPushButton('Click three')
        btn4 = QPushButton('Click four')

        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addWidget(btn4)
        hbox.addSpacing(100)

        # hbox.addStretch(0)

        self.setLayout(hbox)





app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
