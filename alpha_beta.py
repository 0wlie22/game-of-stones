from game_state import GameState


class AlphaBeta:
    def estimate(self, root: GameState) -> None:
        self.alpha_beta(root, float('-inf'), float('inf'), True)

    def alpha_beta(self, node: GameState, alpha: float, beta: float, maximizing_player: bool) -> float:
        if not node.children:
            self._estimate_leaf(node)
            return node.estimation_value

        if maximizing_player:
            value = float('-inf')
            for child in node.children:
                eval_child = self.alpha_beta(child, alpha, beta, False)
                value = max(value, eval_child)
                alpha = max(alpha, value)
                if beta <= alpha:
                    break
            return value
        else:
            value = float('inf')
            for child in node.children:
                eval_child = self.alpha_beta(child, alpha, beta, True)
                value = min(value, eval_child)
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return value

    def _estimate_leaf(self, node: GameState) -> None:
        computer_total = node.computer_stones + node.computer_points
        player_total = node.player_stones + node.player_points

        if computer_total > player_total:
            node.estimation_value = 1
        elif computer_total == player_total:
            node.estimation_value = 0
        else:
            node.estimation_value = -1
        

class AlphaBeta:
    def estimate(self, root: GameState) -> None:
        self.alpha_beta(root, float('-inf'), float('inf'), True)

    def alpha_beta(self, node: GameState, alpha: float, beta: float, maximizing_player: bool) -> float:
        if not node.children:
            self._estimate_leaf(node)
            return node.estimation_value

        if maximizing_player:
            value = float('-inf')
            for child in node.children:
                eval_child = self.alpha_beta(child, alpha, beta, False)
                value = max(value, eval_child)
                alpha = max(alpha, value)
                if beta <= alpha:
                    break
            return value
        else:
            value = float('inf')
            for child in node.children:
                eval_child = self.alpha_beta(child, alpha, beta, True)
                value = min(value, eval_child)
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return value

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
