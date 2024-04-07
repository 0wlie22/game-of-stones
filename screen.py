# pyright: basic

import logging

from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QBoxLayout,
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
    MINI_TITLE_SIZE,
    SCREEN_SIZE,
    SETTINGS_SCREEN_SIZE,
    SUBFONT,
    SUBFONT_SIZE,
    TEXT_SIZE,
)


class Screen(QWidget):
    game_state_changed = QtCore.Signal()

    def __init__(self) -> None:
        super().__init__()
        self.init_ui()
        self.game_state_changed.connect(self.update_score)

    def init_ui(self) -> None:
        self.setWindowTitle("Game of Stones")
        self.start_screen()
        self.show()

    def key_press_event(self, event) -> None:  # noqa: ANN001
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

    def start_screen(self) -> None:
        self.layout = QGridLayout()

        self.resize(*SCREEN_SIZE)

        self.title = QLabel("GAME OF STONES", alignment=QtCore.Qt.AlignCenter)
        self.title.setFont(QFont(FONT, FONT_SIZE_TITLE))

        self.subtitle = QLabel(
            "The game of strategy and wit", alignment=QtCore.Qt.AlignCenter
        )
        self.subtitle.setFont(QFont(SUBFONT, SUBFONT_SIZE))
        self.subtitle.setStyleSheet("color: lightgrey")

        self.new_game_button = QPushButton("New Game", self)
        self.new_game_button.clicked.connect(self.settings_screen)
        self.new_game_button.setFont(QFont(SUBFONT, SUBFONT_SIZE))

        self.layout.addWidget(self.title, 0, 0, 1, 2)
        self.layout.addWidget(self.subtitle, 1, 0, 1, 2)
        self.layout.addWidget(self.new_game_button, 2, 0, 1, 2)

        self.setLayout(self.layout)

    def settings_screen(self) -> None:
        self.clear_layout(self.layout)

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

    def clear_layout(self, layout) -> None:
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
            elif child.layout():
                self.clear_layout(child.layout())

    def start_game(self) -> None:
        logging.info("Starting game")

        if self.algorithm_box.currentText() == ALGORITHM_MINIMAX:
            algorithm = Minimax()
        elif self.algorithm_box.currentText() == ALGORITHM_ALPHA_BETA:
            raise NotImplementedError("Alpha-Beta algorithm not implemented")
        else:
            # Should never reach here
            raise ValueError("Invalid algorithm")

        # Create a new game and enter the game screen
        self.game = Game(
            self.stone_count_box.value(),
            self.first_player_box.currentText().lower(),
            algorithm,
        )  # type: ignore
        self.game_screen()

    def game_screen(self) -> None:
        self.clear_layout(self.layout)
        self.resize(*SCREEN_SIZE)
        self.setWindowTitle("Game of Stones")

        block_width = SETTINGS_SCREEN_SIZE[0] // 10
        block_height = SETTINGS_SCREEN_SIZE[1] // 12

        # Buttons
        self.take_two_button = QPushButton("TAKE 2 STONES", self)
        self.take_two_button.setFixedSize(block_width * 3, block_height * 2)
        self.take_two_button.clicked.connect(self.take_two_stones)
        self.take_three_button = QPushButton("TAKE 3 STONES", self)
        self.take_three_button.setFixedSize(block_width * 3, block_height * 2)
        self.take_three_button.clicked.connect(self.take_three_stones)

        # Player info
        self.player_score_label = QLabel(
            f"Player: {self.game.current_state.player_points}",
            alignment=QtCore.Qt.AlignCenter,
        )
        self.player_score_label.setFont(QFont(FONT, SUBFONT_SIZE))

        self.player_info = QBoxLayout(QBoxLayout.TopToBottom)
        self.player_label = QLabel("Player")
        self.player_label.setFont(QFont(FONT, MINI_TITLE_SIZE))
        self.player_stones_label = QLabel(
            f"Stones: {self.game.current_state.player_points}"
        )
        self.player_stones_label.setStyleSheet("color: lightgrey")
        self.player_stones_label.setFont(QFont(SUBFONT, SUBFONT_SIZE))
        self.player_info.addWidget(self.player_label)
        self.player_info.addWidget(self.player_stones_label)

        # Computer info
        self.computer_score_label = QLabel(
            f"Computer: {self.game.current_state.computer_points}",
            alignment=QtCore.Qt.AlignCenter,
        )
        self.computer_score_label.setFont(QFont(FONT, SUBFONT_SIZE))
        self.computer_info = QBoxLayout(QBoxLayout.TopToBottom)
        self.computer_label = QLabel("Computer", alignment=QtCore.Qt.AlignRight)
        self.computer_label.setFont(QFont(FONT, MINI_TITLE_SIZE))
        self.computer_stones_label = QLabel(
            f"Stones: {self.game.current_state.computer_points}",
            alignment=QtCore.Qt.AlignRight,
        )
        self.computer_stones_label.setStyleSheet("color: lightgrey")
        self.computer_stones_label.setFont(QFont(SUBFONT, SUBFONT_SIZE))
        self.computer_info.addWidget(self.computer_label)
        self.computer_info.addWidget(self.computer_stones_label)

        # Score
        self.score_label = QLabel("0:0", alignment=QtCore.Qt.AlignCenter)
        self.score_label.setFont(QFont(FONT, FONT_SIZE_TITLE))

        self.computer_info.addStretch(0)
        self.player_info.addStretch(0)

        self.stone_count_label = QLabel(
            f"Stones left:\n{self.game.current_state.stones_left}",
            alignment=QtCore.Qt.AlignCenter,
        )
        self.stone_count_label.setFont(QFont(FONT, MINI_TITLE_SIZE))

        self.layout.setContentsMargins(
            block_width / 2, block_height / 2, block_width / 2, block_height / 2
        )

        self.layout.addWidget(self.score_label, 0, 3, 1, 2)
        self.layout.addLayout(self.player_info, 0, 0, 2, 3)
        self.layout.addLayout(self.computer_info, 0, 5, 2, 3)
        self.layout.addWidget(self.stone_count_label, 2, 2, 1, 4)
        self.layout.addWidget(self.take_two_button, 5, 0, 1, 3)
        self.layout.addWidget(self.take_three_button, 5, 5, 1, 3)

        # Make the first move
        if self.game.current_state.player_turn == "computer":
            self.game.make_computer_move()
            self.update_score()

    def take_two_stones(self) -> None:
        if self.game.can_take(2):
            self.game.take_two_stones()

        if self.game.can_take(2):
            self.game.make_computer_move()

        self.update_score()

    def take_three_stones(self) -> None:
        if self.game.can_take(3):
            self.game.take_three_stones()

        if self.game.can_take(3):
            self.game.make_computer_move()

        self.update_score()

    def update_score(self) -> None:
        self.player_stones_label.setText(
            f"Stones: {self.game.current_state.player_stones}"
        )
        self.computer_stones_label.setText(
            f"Stones: {self.game.current_state.computer_stones}"
        )
        self.stone_count_label.setText(
            f"Stones left:\n{self.game.current_state.stones_left}"
        )
        self.score_label.setText(
            f"{self.game.current_state.player_points}:{self.game.current_state.computer_points}"
        )

        QCoreApplication.processEvents()

        if (
            self.game.current_state.stones_left <= 1
            and not self.game.can_take(2)
            and not self.game.can_take(3)
        ):
            self.game_over_screen()

    def game_over_screen(self) -> None:
        # Final score calculations
        player_final_score = (
            self.game.current_state.player_points
            + self.game.current_state.player_stones
        )
        computer_final_score = (
            self.game.current_state.computer_points
            + self.game.current_state.computer_stones
        )

        winner = "Player" if player_final_score > computer_final_score else "Computer"

        self.clear_layout(self.layout)

        self.player_stones_label.setText(f"Score: {player_final_score}")
        self.computer_stones_label.setText(f"Score: {computer_final_score}")

        if winner == "Player":
            result_message = "YOU WON!"
        else:
            result_message = "GAME OVER!"

        result_message_label = QLabel(result_message, alignment=QtCore.Qt.AlignCenter)
        result_message_label.setFont(QFont(FONT, FONT_SIZE_TITLE))

        self.layout.addWidget(result_message_label, 0, 2, 1, 4)
