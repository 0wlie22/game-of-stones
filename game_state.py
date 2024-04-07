import pickle
from collections.abc import Generator
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal, Self
from settings import COMPUTER_PLAYER, HUMAN_PLAYER


@dataclass(slots=True)
class GameState:
    stones_left: int = field(hash=True)
    player_turn: Literal[COMPUTER_PLAYER, HUMAN_PLAYER] = field(hash=True)
    computer_points: int = field(default=0, hash=True)
    player_points: int = field(default=0, hash=True)
    computer_stones: int = field(default=0, hash=True)
    player_stones: int = field(default=0, hash=True)
    computer_stones_taken: int = field(default=0, hash=True)
    _estimation_value: int | None = field(default=None, init=False, hash=False)
    parent: "GameState | None" = field(default=None, init=False, hash=False)
    children: list["GameState"] = field(default_factory=list, init=False, hash=False)

    def generate_next_state(self) -> None:
        """Generate the next possible states based on the number of stones taken."""
        for stones in (2, 3):
            if stones > self.stones_left:
                continue

            add_to_computer, add_to_player, stones_left = self.points_to_add(
                stones, self.player_turn
            )
            if self.player_turn == COMPUTER_PLAYER:
                new_state = GameState(
                    stones_left,
                    HUMAN_PLAYER,
                    self.computer_points + add_to_computer,
                    self.player_points + add_to_player,
                    self.computer_stones + stones,
                    self.player_stones,
                    stones,
                )
            elif self.player_turn == HUMAN_PLAYER:
                new_state = GameState(
                    stones_left,
                    COMPUTER_PLAYER,
                    self.computer_points + add_to_computer,
                    self.player_points + add_to_player,
                    self.computer_stones,
                    self.player_stones + stones,
                    stones,
                )
            self.children.append(new_state)  # type: ignore

        # Set the parent of the children to the current node
        for child in self.children:
            child.parent = self

    def points_to_add(
        self, stones: int, player_turn: Literal[COMPUTER_PLAYER, HUMAN_PLAYER]
    ) -> tuple[int, int, int]:
        """Return the points to add to the computer and player based on the number of stones taken.

        Args:
            stones: The number of stones taken.
            player_turn: The player whose turn it is.

        Returns:
            A tuple containing the points to add to the computer and player and the number of stones left.
        """
        stones_left = self.stones_left - stones
        if stones_left % 2 == 0:
            if player_turn == COMPUTER_PLAYER:
                return 0, 2, stones_left
            else:
                return 2, 0, stones_left
        else:
            if player_turn == COMPUTER_PLAYER:
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

    def leaf_nodes(self) -> list["GameState"]:
        return [node for node in self.traversal() if not node.children]

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

    @classmethod
    def load_dump(
        cls,
        starting_stones: int,
        starting_player: Literal[COMPUTER_PLAYER, HUMAN_PLAYER],
    ) -> "GameState":
        dump_path = Path("dumps") / f"{starting_stones}-{starting_player}-tree.dump"
        with dump_path.open("rb") as fh:
            return pickle.load(fh)  # noqa: S301

    def save_dump(self) -> None:
        dump_path = Path("dumps") / f"{self.stones_left}-{self.player_turn}-tree.dump"
        with dump_path.open("wb") as fh:
            pickle.dump(self, fh)

    def __repr__(self) -> str:
        return (
            f"GameState(stones_left={self.stones_left}, player_turn={self.player_turn}, "
            + f"computer_points={self.computer_points}, player_points={self.player_points}, "
            + f"computer_stones={self.computer_stones}, player_stones={self.player_stones}, "
            + f"estimation_value={self.estimation_value})"
        )
