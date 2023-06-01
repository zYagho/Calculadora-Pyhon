from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import MEDIUM_FONT_SIZE
from functions import isValid, isNumOrDot
from display import Display
from PySide6.QtCore import Slot

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
    def __init__(self, display: Display, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.gridMask = [
            ['C', '<', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['||', '0', '.', '='],
        ]

        self.display = display
        self.makeGrid()

    def makeGrid(self):
        for rowNumber, row in enumerate(self.gridMask):
            for collumnNumber, buttonText in enumerate(row):
                button = Button(buttonText)

                if not isNumOrDot(buttonText):
                    button.setProperty('cssClass', 'specialButton')

                self.addWidget(button, rowNumber, collumnNumber)
                buttonSlot = self.buttonDisplaySlot(self.addButtonToDisplay, button,)
                button.clicked.connect(buttonSlot)

    def buttonDisplaySlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    def addButtonToDisplay(self, button):
        button_text = button.text()

        if isValid(self.display.text() + button_text):
            self.display.insert(button_text)
