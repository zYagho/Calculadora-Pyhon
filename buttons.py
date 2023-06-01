from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import MEDIUM_FONT_SIZE
from functions import isEmpty, isNumOrDot

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.styleConfig()

    def styleConfig(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75,75)
        self.setProperty('cssClass', 'Button')



class ButtonsGrid(QGridLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.gridMask = [
            ['C', '<', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['+/-', '0', '.', '='],
        ]

        self.makeGrid()

    def makeGrid(self):
        for rowNumber, row in enumerate(self.gridMask):
            for collumnNumber, buttonText in enumerate(row):
                button = Button(buttonText)

                if not isNumOrDot(buttonText):
                    button.setProperty('cssClass', 'specialButton')

                self.addWidget(button, rowNumber, collumnNumber)
