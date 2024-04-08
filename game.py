import logging
from dataclasses import dataclass
from typing import Literal

from algorithm import HeuristicAlgorithm
from game_state import GameState


@dataclass
class Game:
    starting_stones: int
    starting_player: Literal["computer", "player"]
    heuristic_estimation_algorithm: HeuristicAlgorithm

    def __post_init__(self) -> None:
        try:
            self.root_state = GameState.load_dump(
                self.starting_stones, self.starting_player
            )
        except FileNotFoundError:
            self.root_state = GameState(
                self.starting_stones, self.starting_player
            ).generate_state_tree()
            self.root_state.save_dump()

        self.current_state = self.root_state

        # Run the heuristic algorithm to estimate the value of each node
        self.heuristic_estimation_algorithm.estimate(self.root_state)

    def _make_player_move(self, stones: int) -> None:
        if stones not in (2, 3):
            raise ValueError("You can only take 2 or 3 stones.")

        if stones == 2:
            self.current_state = self.current_state.left_child()
        else:
            self.current_state = self.current_state.right_child()

    def take_two_stones(self) -> None:
        self._make_player_move(2)

    def take_three_stones(self) -> None:
        self._make_player_move(3)

    def make_computer_move(self) -> None:
        """Make the computer move.

        The next state is chosen using Hill Climbing algorithm. It chooses the child with the highest estimated value.
        """
        if len(self.current_state.children) == 0:
            raise ValueError("The game is already over.")

        # Choose the child with the highest estimated value
        self.current_state = max(
            self.current_state.children, key=lambda x: x.estimation_value
        )

        stones_taken = (
            self.current_state.parent.stones_left - self.current_state.stones_left
        )
        logging.info("Computer takes %d stones", stones_taken)

    def can_take(self, stones: int) -> bool:
        return self.current_state.stones_left >= stones
