from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import MEDIUM_FONT_SIZE
from functions import isValid, isNumOrDot, ula
from PySide6.QtCore import Slot
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from display import Display
    from info import Info
    from main_window import Window


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
    def __init__(self, display: 'Display', info: 'Info', window: 'Window', *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.gridMask = [
            ['C', '<', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['||', '0', '.', '='],
        ]

        self.display = display
        self.info = info
        self.window = window
        self._equation = ''
        self.makeGrid()
        self.leftNumber = ''
        self.rightNumber = ''
        self.operation = ''
        self.result = ''
        self.negativeOP = False

    @property
    def equation(self):

        return self._equation

    @equation.setter
    def equation(self, value):

        self._equation = value
        self.info.setText(value)

    def makeGrid(self):

        for rowNumber, row in enumerate(self.gridMask):
            for collumnNumber, buttonText in enumerate(row):
                button = Button(buttonText)

                if not isNumOrDot(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, rowNumber, collumnNumber)
                slot = self.makeSlot(self.addButtonToDisplay, button,)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):

        button.clicked.connect(slot)

    def _configSpecialButton(self, button):

        textButton = button.text()
        if textButton == 'C':
            slot = self.makeSlot(self._clearDisplay)
            self._connectButtonClicked(button, slot)
        elif textButton in '+-/*^':
            self._connectButtonClicked(button, self.makeSlot(self._operation, button))

        elif textButton == '=':
            self._connectButtonClicked(button, self.makeSlot(self._equalOp))

        elif textButton == '<':
            self._connectButtonClicked(button, self.display.backspace)

    def makeSlot(self, func, *args, **kwargs):

        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    def addButtonToDisplay(self, button):

        button_text = button.text()

        if isValid(self.display.text() + button_text):
            self.display.insert(button_text)

    def _clearDisplay(self, flag=False):

        if flag is False:
            self.setInfo()
            self.leftNumber = ''
            self.rightNumber = ''
            self.operation = ''
            self.result = ''
            self.display.clear()

        else:
            self.leftNumber = ''
            self.rightNumber = ''
            self.operation = ''
            self.result = ''
            self.display.clear()
            self.setInfo()


    def _operation(self, button):

        self.operation = button.text()
        if self.operation != '' and len(self.display.text()) == 0:
            if self.operation == '-':
                self.negativeOP = True
            else:
                self.showMsgError(2)
                return

        elif self.leftNumber == '':
            if self.negativeOP == True:
                self.leftNumber = (float)(self.display.text()) * (-1)
                self.negativeOP = False
            else:
                self.leftNumber = (float)(self.display.text())
            self.display.clear()

        self.setInfo()

    def _equalOp(self):

        if not isValid(self.display.text()):
            return
        if self.operation != '' and self.leftNumber != '':
            if self.negativeOP:
                self.rightNumber = (float)(self.display.text()) + -1
                self.negativeOP = False
            else:
                self.rightNumber = (float)(self.display.text())

            if self.operation == '/' and self.rightNumber == 0:
                self.showMsgError(1)
                self._clearDisplay(flag=True)
            else:
                self.setResult()
                self._clearDisplay()


    def setInfo(self):

        if self.result != '':
            self.equation = f'{self.leftNumber} {self.operation} {self.rightNumber} = {self.result}'
        else:
            self.equation = f'{self.leftNumber} {self.operation} {self.rightNumber}'


    def setResult(self):
        self.result = ula(self.operation, self.leftNumber, self.rightNumber)
        self.setInfo()

    def showMsgError(self, error):
        if error == 1:
            msg = self.window.messagebox()
            msg.setText('ERROR: Division by zero')
            msg.setIcon(msg.Icon.Critical)
            msg.exec()
        elif error == 2:
            msg = self.window.messagebox()
            msg.setText('ERROR: Nothing informed')
            msg.setIcon(msg.Icon.Warning)
            msg.exec()
