from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
import sys
from main_window import Window
from variables import WINDOW_ICON_PATH
from display import Display
from info import Info
from styles import setupTheme
from buttons import ButtonsGrid

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    setupTheme()
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    #Info
    info = Info('22+10')
    window.addToVlayout(info)

    #Display
    display = Display()
    window.addToVlayout(display)

    buttonsGrid = ButtonsGrid(display)
    window.v_layout.addLayout(buttonsGrid)


    window.adjustWindowSize()
    window.show()
    sys.exit(app.exec())

