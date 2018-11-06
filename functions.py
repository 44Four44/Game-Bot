from settings import *

def bubble_sort(start, end):
    with open(map_path, 'r') as file:
        data = file.readlines()
    for i in range (0, 100):
        for j in range (0,100):
            if data[j][300] > data[j + 1][300]:
                x = data[j][300]
                data[j][300] = data[j + 1][300]
                data[j + 1][300] = x

def checkpoint_score(Game, Player):
    coordinates = Game.checkpoints_list[Player.checkpoint]

    dist = math.hypot(float(coordinates[0] + tile_size / 2) - float(Player.rect.x + Player.size / 2),
                  float(coordinates[1] + tile_size / 2) - float(Player.rect.y + Player.size / 2,))
    if Player.checkpoint == 0:
        total_dist = math.hypot(float(coordinates[0] + tile_size / 2) -
                                float(Game.startx * tile_size + tile_size / 2),
                                float(coordinates[1] + tile_size / 2) -
                                float(Game.starty * tile_size + tile_size / 2))
    else:
        prev = Game.checkpoints_list[Player.checkpoint - 1]
        total_dist = math.hypot(float(coordinates[0] + tile_size / 2) -
                                float(prev[0] + tile_size / 2),
                                float(coordinates[1] + tile_size / 2) -
                                float(prev[1] + tile_size / 2))
    score = Player.checkpoint + 1 - dist / total_dist
    if score < 0:
        return format(score, '.9f')
    else:
        return format(score, '.10f')