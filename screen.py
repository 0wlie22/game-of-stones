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
    ALGORITHM_ALPHA_BETA,
    ALGORITHM_MINIMAX,
    FONT,
    FONT_SIZE_TITLE,
    SCREEN_SIZE,
    SETTINGS_SCREEN_SIZE,
    SUBFONT_SIZE,
    TEXT_SIZE,
)


class Screen(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.init_ui()

    def init_ui(self) -> None:
        self.setWindowTitle("Game of Stones")
        self.start_screen()

    def key_press_event(self, event) -> None:  # noqa: ANN001
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

    @Slot()
    def start_screen(self) -> None:
        self.layout = QGridLayout()

        self.resize(*SCREEN_SIZE)

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
    def settings_screen(self) -> None:
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
        self.algorithm_box.addItems([ALGORITHM_MINIMAX, ALGORITHM_ALPHA_BETA])
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

    def clear(self) -> None:
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    @Slot()
    def start_game(self) -> None:
        print("Game started")
        self.game_screen()
        # TODO: Implement minimax and alpha-beta algorithms
        if self.algorithm_box.currentText() == ALGORITHM_MINIMAX:
            raise NotImplementedError("Minimax algorithm not implemented")
        elif self.algorithm_box.currentText() == ALGORITHM_ALPHA_BETA:
            raise NotImplementedError("Alpha-Beta algorithm not implemented")
        else:
            raise ValueError("Invalid algorithm")

    @Slot()
    def game_screen(self) -> None:
        self.clear()
        self.resize(*SCREEN_SIZE)
        self.setWindowTitle("Game of Stones")

        stone_count = self.stone_count_box.value()
        computer_score = 0
        player_score = 0

        self.player_score_label = QLabel(
            "Player: " + str(player_score), alignment=QtCore.Qt.AlignCenter
        )
        self.player_score_label.setFont(QFont(FONT, SUBFONT_SIZE))

        self.computer_score_label = QLabel(
            "Computer: " + str(computer_score), alignment=QtCore.Qt.AlignCenter
        )
        self.computer_score_label.setFont(QFont(FONT, SUBFONT_SIZE))

        self.take_two_button = QPushButton("TAKE 2", self)
        self.take_three_button = QPushButton("TAKE 3", self)

        self.stone_count_label = QLabel(
            "Stones: " + str(stone_count), alignment=QtCore.Qt.AlignCenter
        )
        self.stone_count_label.setFont(QFont(FONT, SUBFONT_SIZE))

        self.layout.addWidget(self.player_score_label, 0, 0)
        self.layout.addWidget(self.computer_score_label, 0, 3)
        self.layout.addWidget(self.stone_count_label, 1, 2)
        self.layout.addWidget(self.take_two_button, 3, 0)
        self.layout.addWidget(self.take_three_button, 3, 3)
