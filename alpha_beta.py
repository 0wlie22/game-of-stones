from game_state import GameState


class AlphaBeta:
    def estimate(
        self, root: GameState, alpha: float = -float("inf"), beta: float = float("inf")
    ) -> None:
        for node in root.post_order_traversal():
            if node.children:
                self._estimate_node(node, alpha, beta)
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

    def _estimate_node(self, node: GameState, alpha: float, beta: float) -> None:
        if node.player_turn == "computer":
            max_value = -float("inf")
            for child in node.children:
                if child.estimation_value is not None:
                    max_value = max(max_value, child.estimation_value)
                    alpha = max(alpha, max_value)
                    if beta <= alpha:
                        break
            node.estimation_value = max_value
        else:
            min_value = float("inf")
            for child in node.children:
                if child.estimation_value is not None:
                    min_value = min(min_value, child.estimation_value)
                    beta = min(beta, min_value)
                    if beta <= alpha:
                        break
            node.estimation_value = min_value
