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
        self.root_state = GameState(self.starting_stones, self.starting_player).generate_state_tree()
        self.current_state = self.root_state

        # Run the heuristic algorithm to estimate the value of each node
        self.heuristic_estimation_algorithm.estimate(self.root_state)

    def make_player_move(self, stones: int) -> None:
        if stones not in (2, 3):
            raise ValueError("You can only take 2 or 3 stones.")

        if stones == 2:
            self.current_state = self.current_state.left_child()
        else:
            self.current_state = self.current_state.right_child()

    def make_computer_move(self) -> None:
        if self.current_state.left_child().estimation_value == self.root_state.estimation_value:
            self.current_state = self.current_state.left_child()
        else:
            self.current_state = self.current_state.right_child()

    def can_take(self, stones: int) -> bool:
        return self.current_state.stones_left >= stones
