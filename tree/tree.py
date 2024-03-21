from .tree_utils import nextGameStates, previousStates, generateTree


class GameTree:
    def __init__(self, starting_state, height=-1):
        self.levels = generateTree(starting_state, height)

    def find_parent(self, game_state):
        return previousStates(game_state, self.levels)

    def find_children(self, game_state):
        for level in self.levels:
            if game_state in level:
                return nextGameStates(game_state)
        print("Game state is not in tree.")
        return []

    def get_level(self, level):
        return self.levels[level]

    def print_all_levels(self):  # Debug purposes only
        print(self.levels)
