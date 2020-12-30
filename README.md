# Game-Bot
An ML bot that uses reinforced learning to beat a given level in "The World's Hardest Game". The original game is https://www.coolmathgames.com/0-worlds-hardest-game.

The program works by spawning a specified number of players that move randomly and play the game out until they die. After all players die, the program finds the player that performed the best using a scoring algorithm and stores its history of moves in moves.txt (check it out!). Then the next generation begins at a location close to the location of death of the best performing player from the preivous generation. If multiple generations pass without a reasonable increase in score based on the scoring algorithm, then the generations begin back a few moves. Eventually the program will find an ideal set of moves to beat the level.

Maps can be created by the user in with specific characters that represent each aspect of the map. See the file for level 1 as an example. Enemy movement paths are coded in Game.py.


