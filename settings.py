# Windows sizes
SCREEN_SIZE = (800, 600)
SETTINGS_SCREEN_SIZE = (500, 400)

# Text
FONT = "Georgia"
FONT_SIZE_TITLE = 70
SUBFONT_SIZE = 20
TEXT_SIZE = 15

# Algorithms
ALGORITHM_MINIMAX = "Minimax"
ALGORITHM_ALPHA_BETA = "Alpha-Beta"

def ALGORITHM_ALPHA_BETA(state, depth, alpha, beta, maximizing_player):
    if depth == 0 or state == 0:
        return evaluate(state), None
    
    if maximizing_player:
        max_eval = float('-inf')
        best_move = None
        for move in [2, 3]:
            if state - move >= 0:
                eval, _ = ALGORITHM_ALPHA_BETA(state - move, depth - 1, alpha, beta, False)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in [2, 3]:
            if state - move >= 0:
                eval, _ = ALGORITHM_ALPHA_BETA(state - move, depth - 1, alpha, beta, True)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval, best_move

def evaluate(state):
    if state % 2 == 0:
        return -2
    else:
        return 2
