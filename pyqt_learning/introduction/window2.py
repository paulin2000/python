from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.statusBar().showMessage("salut les nas")
window.menuBar().addMenu("new File   ")


window.show()

sys.exit(app.exec())
