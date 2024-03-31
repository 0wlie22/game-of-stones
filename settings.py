
def alpha_beta(state, depth, alpha, beta, maximizing_player):
    if depth == 0 or state['stones'] == 0:
        return state['score']

    if maximizing_player:
        max_eval = float('-inf')
        for move in [2, 3]:
            if state['stones'] - move >= 0:
                next_state = {
                    'stones': state['stones'] - move,
                    'score': state['score'] + move  
                }
                if (state['stones'] - move) % 2 == 0:
                    next_state['score'] += 2  
                eval = alpha_beta(next_state, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for move in [2, 3]:
            if state['stones'] - move >= 0:
                next_state = {
                    'stones': state['stones'] - move,
                    'score': state['score'] + move 
                }
                if (state['stones'] - move) % 2 == 0:
                    next_state['score'] += 2 
                eval = alpha_beta(next_state, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval


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


