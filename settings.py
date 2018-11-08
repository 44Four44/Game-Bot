import pygame
import sys
import random
import math

pygame.init()

# size of the square tiles that make up the map
tile_size = 40
screen_width = tile_size * 20
screen_height = tile_size * 15

# true if the game is running
run = True

# File path for data files
map_path = '/Users/EthanWang/Game_Bot/map.txt'
moves_path = '/Users/EthanWang/Game_Bot/moves.txt'

# Game settings
FPS = 60
zoom = 10
Title = "mmmmmmmmmm"

# Colors
red = (255, 0, 0)
black = (0, 0, 0)
lavender = (224, 218, 254)
ghostwhite = (248, 247, 255)
lightsteelblue = (170, 165, 255)
maroon = (127, 0, 0)
palegreen = (158, 242, 155)
blue = (0, 0, 255)
midnightblue = (0, 0, 68)
lime = (53, 247, 0)

