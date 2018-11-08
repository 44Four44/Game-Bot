from settings import *

def bubble_sort(start, end):
    with open(moves_path, 'r') as file:
        data = file.readlines()
    print(start)
    print(end)
    # Cluster that is going to be sorted
    cluster = data[start : end + 1]

    for i in range (0, len(cluster) - 1):
        for j in range (0, len(cluster) - 1):
            # Swap if value is greater than the next value
            current = cluster[j]
            next = cluster[j + 1]
            if float(current[7 : 14]) > float(next[7 : 14]):
                cluster[j], cluster[j + 1] = next, current

    # Write back to moves file
    data[start : end + 1] = cluster
    with open(moves_path, 'w') as file:
        file.writelines(data)

def checkpoint_score(Game, Player):
    coordinates = Game.checkpoints_list[Player.checkpoint]

    dist = math.hypot(float(coordinates[0] + tile_size / 2) - float(Player.rect.x + tile_size / 2),
                  float(coordinates[1] + tile_size / 2) - float(Player.rect.y + tile_size / 2))

    if Player.checkpoint == 0:
        total_dist = math.hypot(float(coordinates[0] + tile_size / 2) - float(Game.startx + tile_size / 2),
                                float(coordinates[1] + tile_size / 2) - float(Game.starty + tile_size / 2))
    else:
        prev = Game.checkpoints_list[Player.checkpoint - 1]
        total_dist = math.hypot(float(coordinates[0] + tile_size / 2) - float(prev[0] + tile_size / 2),
                                float(coordinates[1] + tile_size / 2) - float(prev[1] + tile_size / 2))

    score = Player.checkpoint + 1 - dist / total_dist
    if Player.hit:
        score -= 1

    if score < 0:
        return format(score, '.4f')
    else:
        return format(score, '.5f')