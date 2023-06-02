import re


NUM_OR_DOT_REGEX =  re.compile(r'^[0-9.]$')


def isNumOrDot(string: str):
    return bool(NUM_OR_DOT_REGEX.search(string))

def isValid(string:str):

    try:
        (float)(string)
        return True
    except ValueError:
        return False


def ula(operation, leftNumber, rigthNumber):

    if operation == '+':
        return float(leftNumber + rigthNumber)
    elif operation == '-':
        return float(leftNumber - rigthNumber)
    elif operation == '*':
        return float(leftNumber * rigthNumber)
    elif operation == '/':
        return float(leftNumber / rigthNumber)
    elif operation == '^':
        return float(leftNumber ** rigthNumber)
