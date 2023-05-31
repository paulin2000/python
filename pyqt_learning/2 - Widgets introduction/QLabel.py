from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('Python GUI Development')
        self.setWindowIcon(QIcon('../images/OIP.jpg'))

        '''
        label = QLabel("Python gui label", self)
        label.setText('New text')
        label.move(100, 100)
        label.setFont(QFont("Sanserif", 15))
        label.setStyleSheet('color:red')
        # '''
        #label.setText(str(12))
        #label.setNum(15)
        #label.clear()
        '''
        label = QLabel(self)
        pixmap = QPixmap('../images/OIP.jpg')
        label.setPixmap(pixmap)
        '''
        label = QLabel(self)
        movie = QMovie('../videos/sky.gif')
        movie.setSpeed(500)
        label.setMovie(movie)
        movie.start()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
