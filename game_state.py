from collections.abc import Generator
from dataclasses import dataclass
from typing import Literal, Self


@dataclass
class GameState:
    stones_left: int
    player_turn: Literal["computer", "player"]
    computer_points: int = 0
    player_points: int = 0
    computer_stones: int = 0
    player_stones: int = 0

    def __post_init__(self) -> None:
        self._estimation_value = None
        self.parent = None
        self.children: list[GameState] = []

    def generate_next_state(self) -> None:
        """Generate the next possible states based on the number of stones taken."""
        for stones in (2, 3):
            if stones > self.stones_left:
                continue

            add_to_computer, add_to_player, stones_left = self.points_to_add(stones, self.player_turn)
            if self.player_turn == "computer":
                self.children.append(
                    GameState(
                        stones_left,
                        "player",
                        self.computer_points + add_to_computer,
                        self.player_points + add_to_player,
                        self.computer_stones + stones,
                        self.player_stones,
                    )
                )
            elif self.player_turn == "player":
                self.children.append(
                    GameState(
                        stones_left,
                        "computer",
                        self.computer_points + add_to_computer,
                        self.player_points + add_to_player,
                        self.computer_stones,
                        self.player_stones + stones,
                    )
                )

        # Set the parent of the children to the current node
        for child in self.children:
            child.parent = self

    def points_to_add(self, stones: int, player_turn: Literal["computer", "player"]) -> tuple[int, int, int]:
        """Return the points to add to the computer and player based on the number of stones taken.

        Args:
            stones: The number of stones taken.
            player_turn: The player whose turn it is.

        Returns:
            A tuple containing the points to add to the computer and player and the number of stones left.
        """
        stones_left = self.stones_left - stones
        if stones_left % 2 == 0:
            if player_turn == "computer":
                return 0, 2, stones_left
            else:
                return 2, 0, stones_left
        else:
            if player_turn == "computer":
                return 2, 0, stones_left
            else:
                return 0, 2, stones_left

    def generate_state_tree(self) -> Self:
        self.generate_next_state()
        for child in self.children:
            child.generate_state_tree()

        return self

    def traversal(self) -> Generator["GameState", None, None]:
        queue: list[GameState] = [self]
        while queue:
            node = queue.pop()
            yield node
            queue.extend(node.children)

    def post_order_traversal(self) -> Generator["GameState", None, None]:
        for child in self.children:
            yield from child.post_order_traversal()
        yield self

    def left_child(self) -> "GameState":
        return self.children[0]

    def right_child(self) -> "GameState":
        return self.children[1]

    @property
    def estimation_value(self) -> int | None:
        return self._estimation_value

    @estimation_value.setter
    def estimation_value(self, value: int) -> None:
        if value not in (-1, 0, 1):
            raise ValueError("Estimation value must be either -1, 0 or 1.")
        self._estimation_value = value

    def __hash__(self) -> int:
        return hash(
            (
                self.stones_left,
                self.player_turn,
                self.computer_points,
                self.player_points,
                self.computer_stones,
                self.player_stones,
            )
        )

    def __repr__(self) -> str:
        return (
            f"GameState(stones_left={self.stones_left}, player_turn={self.player_turn}, "
            + f"computer_points={self.computer_points}, player_points={self.player_points}, "
            + f"computer_stones={self.computer_stones}, player_stones={self.player_stones}, "
            + f"estimation_value={self.estimation_value})"
        )
