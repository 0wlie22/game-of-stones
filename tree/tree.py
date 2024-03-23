from .tree_utils import *


class GameTree:
    def __init__(self, starting_state, height=-1):
        self.levels = generate_tree(starting_state, height)

    def find_parent(self, game_state):
        return previous_states(game_state, self.levels)

    def find_children(self, game_state):
        for level in self.levels:
            if game_state in level:
                return next_game_states(game_state)
        print("Game state is not in tree.")
        return []

    def get_level(self, level):
        return self.levels[level]

    def get_height(self):
        return len(self.levels)

    def get_all_levels(self):
        return self.levels
