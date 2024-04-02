import sys

from PySide6.QtWidgets import QApplication

from screen import Screen
from settings import FONT, SCREEN_SIZE

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setFont(FONT)

    screen = Screen()
    screen.resize(*SCREEN_SIZE)
    screen.show()

    sys.exit(app.exec())
