# pyright: basic


from PySide6 import QtCore
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QComboBox,
    QGridLayout,
    QLabel,
    QPushButton,
    QSpinBox,
    QWidget,
)

from game import Game
from minimax import Minimax
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

    def start_screen(self) -> None:
        self.layout = QGridLayout()

        self.resize(*SCREEN_SIZE)

        self.title = QLabel("GAME OF STONES", alignment=QtCore.Qt.AlignCenter)
        self.title.setFont(QFont(FONT, FONT_SIZE_TITLE))

        self.subtitle = QLabel("The game of strategy and wit", alignment=QtCore.Qt.AlignCenter)
        self.subtitle.setFont(QFont(FONT, SUBFONT_SIZE))
        self.subtitle.setStyleSheet("color: lightgrey")

        self.new_game_button = QPushButton("New Game", self)
        self.new_game_button.clicked.connect(self.settings_screen)
        self.new_game_button.setFont(QFont(FONT, SUBFONT_SIZE))

        self.layout.addWidget(self.title, 0, 0, 1, 2)
        self.layout.addWidget(self.subtitle, 1, 0, 1, 2)
        self.layout.addWidget(self.new_game_button, 2, 0, 1, 2)

        self.setLayout(self.layout)

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
        self.start_game_button.setFont(QFont(FONT, SUBFONT_SIZE))

        self.layout.addWidget(self.stone_count_label, 0, 0)
        self.layout.addWidget(self.stone_count_box, 0, 2)
        self.layout.addWidget(self.first_player_label, 1, 0)
        self.layout.addWidget(self.first_player_box, 1, 2)
        self.layout.addWidget(self.algorithm_label, 2, 0)
        self.layout.addWidget(self.algorithm_box, 2, 2)
        self.layout.addWidget(self.start_game_button, 3, 0, 1, 3)

        self.start_game_button.clicked.connect(self.start_game)

    def clear(self) -> None:
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def start_game(self) -> None:
        print("Game started")
        if self.algorithm_box.currentText() == ALGORITHM_MINIMAX:
            algorithm = Minimax()
        elif self.algorithm_box.currentText() == ALGORITHM_ALPHA_BETA:
            raise NotImplementedError("Alpha-Beta algorithm not implemented")
        else:
            # Should never reach here
            raise ValueError("Invalid algorithm")

        # Create a new game and enter the game screen
        self.game = Game(self.stone_count_box.value(), self.first_player_box.currentText().lower(), algorithm)  # type: ignore
        self.game_screen()

    def game_screen(self) -> None:
        self.clear()
        self.resize(*SCREEN_SIZE)
        self.setWindowTitle("Game of Stones")

        self.player_score_label = QLabel(
            f"Player: {self.game.current_state.player_points}", alignment=QtCore.Qt.AlignCenter
        )
        self.player_score_label.setFont(QFont(FONT, SUBFONT_SIZE))

        self.computer_score_label = QLabel(
            f"Computer: {self.game.current_state.computer_points}", alignment=QtCore.Qt.AlignCenter
        )
        self.computer_score_label.setFont(QFont(FONT, SUBFONT_SIZE))

        self.take_two_button = QPushButton("TAKE 2 STONES", self)
        self.take_three_button = QPushButton("TAKE 3 STONES", self)

        self.stone_count_label = QLabel(
            f"Stones left: {self.game.current_state.stones_left}", alignment=QtCore.Qt.AlignCenter
        )
        self.stone_count_label.setFont(QFont(FONT, SUBFONT_SIZE))

        self.layout.addWidget(self.player_score_label, 0, 0)
        self.layout.addWidget(self.computer_score_label, 0, 3)
        self.layout.addWidget(self.stone_count_label, 1, 2)
        self.layout.addWidget(self.take_two_button, 3, 0)
        self.layout.addWidget(self.take_three_button, 3, 3)

        if self.game.current_state.player_turn == "computer":
            self.game.make_computer_move()
            self.update_score()

        self.take_two_button.clicked.connect(self.take_two_stones)
        self.take_three_button.clicked.connect(self.take_three_stones)

    def take_two_stones(self) -> None:
        if self.game.can_take(2):
            self.game.take_two_stones()
            self.update_score()
        if self.game.can_take(2):
            self.game.make_computer_move()
            self.update_score()

    def take_three_stones(self) -> None:
        if self.game.can_take(3):
            self.game.take_three_stones()
            self.update_score()
        if self.game.can_take(3):
            self.game.make_computer_move()
            self.update_score()

    def update_score(self) -> None:
        self.player_score_label.setText(f"Player: {self.game.current_state.player_points}")
        self.computer_score_label.setText(f"Computer: {self.game.current_state.computer_points}")
        self.stone_count_label.setText(f"Stones: {self.game.current_state.stones_left}")
