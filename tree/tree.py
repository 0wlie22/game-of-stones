from .tree_utils import (
    nextGameStates,
    previousStates,
    generateTree
)

class gameTree:
    def __init__(self, starting_state, height=-1):
        self.levels = generateTree(starting_state, height)
    
    def findParent(self, game_state):
        return previousStates(game_state, self.levels)
    
    def findChildren(self, game_state):
        for level in self.levels:
            if game_state in level:
                return nextGameStates(game_state)
        print("Game state is not in tree.")
        return []

    def getLevel(self, level):
        return self.levels[level]

    def printAllLevels(self): # Debug purposes only
        print(self.levels)