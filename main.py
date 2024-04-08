import sys

from PySide6.QtWidgets import QApplication

from screen import Screen
from settings import FONT

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setFont(FONT)

    screen = Screen()
    screen.show()

    sys.exit(app.exec())
