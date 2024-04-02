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
        self.game = GameState(self.starting_stones, self.starting_player)
        self.root_state = self.game.generate_state_tree()

        # Run the heuristic algorithm to estimate the value of each node
        self.heuristic_estimation_algorithm.estimate(self.root_state)
