# This is a modified version of the online available Monte Carlo Search Tree
# at https://github.com/int8/monte-carlo-tree-search
# This has been changed and commented to increase readablity while also changing some functions
# to fit Exploding Kittens rather than Tic Tac Toe.
import numpy as np

from Tree.MonteCarloTreeSearchNode import TwoPlayersGameMonteCarloTreeSearchNode as node
from Tree.MonteCarloTreeSearch import MonteCarloTreeSearch as tree
from Game.Gamestate import ExplodingKittensAbstractGameState as gs
from Training_Data.Generate import Generate as gen
import sys
import os

# Does a pretty print of the search tree.
def pprint_tree(node, file=None, _prefix="", _last=True):
    print(_prefix, "`- " if _last else "|- ", "P:", node.state.game.currentPlayer, " ",
        node.state.get_obsersavtion_space(), "#'s visited: ", node.n, " #'s wins: ",\
        list(node._results.values())[node.state.game.currentPlayer], " #'s loses: ",\
        list(node._results.values())[node.state.game.currentPlayer - 1], " Action: ",\
        node.action, sep="", file=file)
    _prefix += "   " if _last else "|  "
    child_count = len(node.children)
    for i, child in enumerate(node.children):
        _last = i == (child_count - 1)
        pprint_tree(child, file, _prefix, _last)

# Block
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__


board_state = gs()
print(board_state.get_obsersavtion_space())
print(board_state.get_legal_actions())
board_state = board_state.move("draw")
print(board_state.get_obsersavtion_space())
print(board_state.get_legal_actions())
print(board_state.is_game_over())
print(board_state.game_result())