import qdarktheme


from variables import (DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR,
                       PRIMARY_COLOR, BUTTON_COLOR_MEDIUM, BUTTON_COLOR_HIGH, BUTTON_COLOR_LOW)

qss = f"""
    QPushButton[cssClass="Button"] {{
        color: #fff;
        background: {BUTTON_COLOR_HIGH};
    }}
    QPushButton[cssClass="Button"]:hover {{
        color: #fff;
        background: {BUTTON_COLOR_MEDIUM};
    }}
    QPushButton[cssClass="Button"]:pressed {{
        color: #fff;
        background: {BUTTON_COLOR_LOW};
    }}
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""


def setupTheme():
    qdarktheme.setup_theme(
        theme='dark',
        corner_shape='rounded',
        custom_colors={
            "[dark]": {
                "primary": f"{PRIMARY_COLOR}",
            },
            "[light]": {
                "primary": f"{PRIMARY_COLOR}",
            },
        },
        additional_qss=qss
    )
