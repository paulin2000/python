from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('QGridLayout')
        self.setWindowIcon(QIcon('../images/OIP.jpg'))


        grid = QGridLayout()
        btn1 = QPushButton('Click one')
        btn2 = QPushButton('Click two')
        btn3 = QPushButton('Click three')
        btn4 = QPushButton('Click four')
        btn5 = QPushButton('Click four')
        btn6 = QPushButton('Click four')
        btn7 = QPushButton('Click four')
        btn8 = QPushButton('Click four')

        grid.addWidget(btn1, 0, 1)
        grid.addWidget(btn2, 0, 2)
        grid.addWidget(btn3, 0, 3)
        grid.addWidget(btn4, 0, 4)
        grid.addWidget(btn5, 1, 1)
        grid.addWidget(btn6, 1, 2)
        grid.addWidget(btn7, 1, 3)
        grid.addWidget(btn8, 1, 4)

        self.setLayout(grid)

        # hbox.addStretch(0)






app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
