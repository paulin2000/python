import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt
import random


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt Drawing")
        self.setGeometry(100, 100, 500, 400)

        # Création d'un widget de canevas
        self.canvas = Canvas(self)
        self.setCentralWidget(self.canvas)

        # Création de boutons
        self.quit_button = QPushButton("Quitter", self)
        self.quit_button.clicked.connect(self.close)
        self.line_button = QPushButton("Tracer une ligne", self)
        self.line_button.clicked.connect(lambda: self.draw('line'))
        self.rect_button = QPushButton("Tracer un rectangle", self)
        self.rect_button.clicked.connect(lambda: self.draw('rectangle'))
        self.arc_button = QPushButton("Tracer un arc", self)
        self.arc_button.clicked.connect(lambda: self.draw('arc'))
        # self.oval_button = QPushButton("Tracer un oval", self)
        # self.oval_button.clicked.connect(self.canvas.draw('oval'))
        # self.poly_button = QPushButton("Tracer un polygon", self)
        # self.poly_button.clicked.connect(self.canvas.draw('polygon'))
        # self.color_button = QPushButton("Autre couleur", self)
        # self.color_button.clicked.connect(self.canvas.change_color)
        # self.target_button = QPushButton("Viseur", self)
        # self.target_button.clicked.connect(self.canvas.draw('viseur'))

        # Ajout des boutons dans un layout horizontal
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.quit_button)
        button_layout.addWidget(self.line_button)
        button_layout.addWidget(self.rect_button)
        button_layout.addWidget(self.arc_button)
        # button_layout.addWidget(self.oval_button)
        # button_layout.addWidget(self.poly_button)
        # button_layout.addWidget(self.color_button)
        # button_layout.addWidget(self.target_button)

        # Ajout du layout des boutons dans un layout vertical
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.canvas)
        main_layout.addLayout(button_layout)

        # Définition du layout principal de la fenêtre
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def draw(self, arg):
        self.canvas.set_draw_type(arg)
        self.canvas.update()


class Canvas(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setMinimumSize(500, 400)
        self.setAutoFillBackground(True)
        self.palette().setColor(self.backgroundRole(), Qt.darkGray)
        self.pen_color = Qt.white
        self.draw_type = ''

    def paintEvent(self, event):
        qp = QPainter()
        print(self.pen_color)
        qp.setPen(QPen(self.pen_color, 2, Qt.SolidLine))
        qp.begin(self)
        self.draw_canvas(qp)
        qp.end()

    def set_pen_color(self, arg):
        self.pen_color = arg

    def set_draw_type(self, arg):
        self.draw_type = arg

    def draw_canvas(self, qp):
        # print('salut les naz')
        qp.drawLine(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # self.update()
        # print(qp, self.target_pen,qp.drawLine(10, 190, 190, 9), "qb")

        switcher: dict = {
            "line": lambda: qp.drawLine(10, 190, 190, 9),
            "rectangle": lambda: qp.drawRect(50, 50, 200, 100),
            "arc": lambda: qp.drawArc(250, 50, 200, 100, 0, 180 * 16),
            # "oval":,
            # "polygon":,
            # "viseur":
        }
        func = switcher.get(self.draw_type)
        self.change_color()
        if func:
            func()

    def change_color(self):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        tmp = QColor(red, green, blue)
        print(tmp)
        self.set_pen_color(Qt.white)

    # def draw_lines(self, qp):
    #     pen = QPen(self.pen_color, 1, Qt.SolidLine)
    #     qp.setPen(pen)
    #
    #     # Tracer une ligne
    #     qp.drawLine(10, 190, 190, 9)
    #
    #     # Tracer un rectangle
    #     qp.drawRect(50, 50, 200, 100)
    #
    #     # Tracer un arc
    #     qp.drawArc(250, 50, 200, 100, 0, 180 * 16)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
