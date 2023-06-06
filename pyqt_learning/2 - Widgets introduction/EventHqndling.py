from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('EventHandling')
        self.setWindowIcon(QIcon('../images/OIP.jpg'))
        self.create_widget()

    def create_widget(self):
        hbox = QHBoxLayout()
        btn = QPushButton('Change Text')
        btn.clicked.connect(self.clicked_btn)
        self.label = QLabel('Defaut Text')

        hbox.addWidget(btn)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

    def clicked_btn(self):
        self.label.setText('Another TExt')
        self.label.setFont(QFont('Times', 15))
        self.label.setStyleSheet('color:red')




app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
