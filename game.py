import logging
import time
from dataclasses import dataclass
from typing import Literal

from algorithm import HeuristicAlgorithm
from game_state import GameState


@dataclass
class Game:
    starting_stones: int
    starting_player: Literal["computer", "player"]
    heuristic_estimation_algorithm: HeuristicAlgorithm
    time_spent_per_move: float = 0
    computer_nodes_visited: int = 0

    def __post_init__(self) -> None:
        time_start = time.time()
        self.root_state = GameState(
            self.starting_stones, self.starting_player
        ).generate_state_tree()
        time_end = time.time()
        self.generation_time = time_end - time_start
        logging.debug("Generating the state tree took %f seconds", self.generation_time)

        self.current_state = self.root_state

        # Run the heuristic algorithm to estimate the value of each node
        time_start = time.time()
        self.heuristic_estimation_algorithm.estimate(self.root_state)
        time_end = time.time()
        self.estimation_time = time_end - time_start
        logging.debug(
            "Estimating the value of each node took %f seconds", self.estimation_time
        )

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
        self.computer_nodes_visited += 1

        start_time = time.time()
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

        end_time = time.time()

        time_spent = end_time - start_time
        self.time_spent_per_move += time_spent
        logging.debug("Computer move took %f seconds", time_spent)

    def can_take(self, stones: int) -> bool:
        return self.current_state.stones_left >= stones
