#-----------------------------------------------------------------------------
# Name:        World's Hardest Game AI (python.py)
# Purpose:     To create an AI that can learn to play the World's Hardest Game
#
# Author:      Ethan Wang
# Created:     15-Oct-2018
# Updated:     08-Nov-2018
#-----------------------------------------------------------------------------

from Game import *

with('/Users/EthanWang/Game_Bot/moves.txt'):
    
roblox = Game()
roblox.new(1)

roblox.new_player('random', 100)

clear_moves()

roblox.run()


