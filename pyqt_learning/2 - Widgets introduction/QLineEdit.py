from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('QLineEdit')
        self.setWindowIcon(QIcon('../images/OIP.jpg'))
        # self.setFixedWidth(700)
        # self.setFixedHeight(400)
        # self.setWindowOpacity(0.5)
        line_edit = QLineEdit(self)
        line_edit.setFont(QFont('Sanserif', 15))
        # line_edit.setText('Default Text')
        # line_edit.setPlaceholderText('Please enter your username')
        line_edit.setEchoMode(QLineEdit.EchoMode.Password)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
