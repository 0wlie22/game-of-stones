from typing import Protocol

from game_state import GameState


class HeuristicAlgorithm(Protocol):
    def estimate(self, root: GameState) -> None:
        """Create an estimation value for each node in the tree."""
