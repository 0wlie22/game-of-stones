import sys

from PySide6 import QtCore
from PySide6.QtCore import Slot
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QComboBox,
    QGridLayout,
    QLabel,
    QPushButton,
    QSpinBox,
    QWidget,
)

from settings import (
    FONT,
    FONT_SIZE_TITLE,
    SETTINGS_SCREEN_SIZE,
    SUBFONT_SIZE,
    TEXT_SIZE,
)


class Screen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Game of Stones")
        self.start_screen()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

    @Slot()
    def start_screen(self):
        self.layout = QGridLayout()

        self.title = QLabel("GAME OF STONES", alignment=QtCore.Qt.AlignCenter)
        self.title.setFont(QFont(FONT, FONT_SIZE_TITLE))

        self.subtitle = QLabel(
            "The game of strategy and wit", alignment=QtCore.Qt.AlignCenter
        )
        self.subtitle.setFont(QFont(FONT, SUBFONT_SIZE))
        self.subtitle.setStyleSheet("color: lightgrey")

        self.new_game_button = QPushButton("New Game", self)
        self.new_game_button.clicked.connect(self.settings_screen)
        self.new_game_button.setFont(QFont(FONT, SUBFONT_SIZE))

        self.layout.addWidget(self.title, 0, 0, 1, 2)
        self.layout.addWidget(self.subtitle, 1, 0, 1, 2)
        self.layout.addWidget(self.new_game_button, 2, 0, 1, 2)

        self.setLayout(self.layout)

    @Slot()
    def settings_screen(self):
        self.clear()

        self.setWindowTitle("Game of Stones - Settings")
        self.resize(*SETTINGS_SCREEN_SIZE)

        self.stone_count_label = QLabel("Stone Count (50 - 70):")
        self.stone_count_label.setFont(QFont(FONT, SUBFONT_SIZE))
        self.stone_count_box = QSpinBox(self)
        self.stone_count_box.setMinimum(50)
        self.stone_count_box.setMaximum(70)
        self.stone_count_box.setFont(QFont(FONT, TEXT_SIZE))

        self.first_player_label = QLabel("First player:")
        self.first_player_label.setFont(QFont(FONT, SUBFONT_SIZE))
        self.first_player_box = QComboBox(self)
        self.first_player_box.addItems(["Player", "Computer"])
        self.first_player_box.setFont(QFont(FONT, TEXT_SIZE))

        self.algorithm_label = QLabel("Computer Algorithm:")
        self.algorithm_label.setFont(QFont(FONT, SUBFONT_SIZE))
        self.algorithm_box = QComboBox(self)
        self.algorithm_box.addItems(["Minimax", "Alpha-Beta"])
        self.algorithm_box.setFont(QFont(FONT, TEXT_SIZE))

        self.start_game_button = QPushButton("Start Game", self)
        self.start_game_button.clicked.connect(self.start_game)
        self.start_game_button.setFont(QFont(FONT, SUBFONT_SIZE))

        self.layout.addWidget(self.stone_count_label, 0, 0)
        self.layout.addWidget(self.stone_count_box, 0, 2)
        self.layout.addWidget(self.first_player_label, 1, 0)
        self.layout.addWidget(self.first_player_box, 1, 2)
        self.layout.addWidget(self.algorithm_label, 2, 0)
        self.layout.addWidget(self.algorithm_box, 2, 2)
        self.layout.addWidget(self.start_game_button, 3, 0, 1, 3)

        self.setLayout(self.layout)

    @Slot()
    def start_game(self):
        print("Game started")
        sys.exit()

    def clear(self):
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
