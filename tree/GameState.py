from .tree_utils import take_stones, undo_take_stones, generate_tree


class GameState:
    def __init__(self, state):
        self.state = state
        self.take_actions = []

    def take(self, count):
        self.state = take_stones(self.state, count)
        self.take_actions.append(count)

    def undo_move(self):
        if len(self.take_actions)==0:
            raise IndexError("Cannot undo move: no moves done.")
        last_action = self.take_actions[-1]
        self.state = undo_take_stones(self.state, last_action)
        self.take_actions.pop()

    def next_turns(self, turns=-1):
        return generate_tree(self.state, turns)

    def print_state(self):
        print(self.state)
