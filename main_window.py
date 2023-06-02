
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox

class Window(QMainWindow):
    def __init__(self):
        super().__init__()


        self.cw = QWidget()
        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)

        self.setCentralWidget(self.cw)


        self.setWindowTitle('Calculadora')

    def addToVlayout(self, widget: QWidget):
        self.v_layout.addWidget(widget)

    def adjustWindowSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def messagebox(self):
        return QMessageBox(self)
