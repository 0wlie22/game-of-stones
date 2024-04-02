from game_state import GameState


class Minimax:
    def estimate(self, root: GameState) -> None:
        for node in root.post_order_traversal():
            if node.children:
                self._estimate_node(node)
            else:
                self._estimate_leaf(node)

    def _estimate_leaf(self, node: GameState) -> None:
        computer_total = node.computer_stones + node.computer_points
        player_total = node.player_stones + node.player_points

        if computer_total > player_total:
            node.estimation_value = 1
        elif computer_total == player_total:
            node.estimation_value = 0
        else:
            node.estimation_value = -1

    def _estimate_node(self, node: GameState) -> None:
        if node.player_turn == "computer":
            node.estimation_value = max(
                child.estimation_value for child in node.children if child.estimation_value is not None
            )
        else:
            node.estimation_value = min(
                child.estimation_value for child in node.children if child.estimation_value is not None
            )
