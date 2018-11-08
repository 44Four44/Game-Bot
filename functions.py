from settings import *

def bubble_sort(start, end):
    """
    Sorts the moves file from lowest to highest score with bubble sorting

    Parameters
    ----------
    start: int
        Starting line index of the lines that will be sorted
    end: int
        End line index of the lines that will be sorted

    Return
    ------
    None

    """

    start_time = time.time()
    with open(moves_path, 'r') as file:
        data = file.readlines()
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
    print("Bubble sort execution time:  %s seconds" % (time.time() - start_time))

def insertion_sort(start, end):
    """
    Sorts the moves file from lowest to highest score with insertion sorting

    Parameters
    ----------
    start: int
        Starting line index of the lines that will be sorted
    end: int
        End line index of the lines that will be sorted

    Return
    ------
    None

    """

    start_time = time.time()
    with open(moves_path, 'r') as file:
        data = file.readlines()
    # Cluster that is going to be sorted
    cluster = data[start : end + 1]

    for i in range(0, len(cluster)):
        current = cluster[i]
        position = i

        while position > 0 and cluster[position - 1] > current:
            cluster[position] = cluster[position - 1]
            position -= 1

        cluster[position] = current
    # [4, 4 , 6, 5, 8, 12]
    # Write back to moves file
    data[start : end + 1] = cluster
    with open(moves_path, 'w') as file:
        file.writelines(data)
    print("Insertion sort execution time:  %s seconds" % (time.time() - start_time))

def python_sort(start, end):
    """
    Sorts the moves file from lowest to highest score with python's built in

    Parameters
    ----------
    start: int
        Starting line index of the lines that will be sorted
    end: int
        End line index of the lines that will be sorted

    Return
    ------
    None

    """

    start_time = time.time()
    with open(moves_path, 'r') as file:
        data = file.readlines()
    # Cluster that is going to be sorted
    cluster = data[start : end + 1]

    cluster.sort()

    # Write back to moves file
    data[start : end + 1] = cluster
    with open(moves_path, 'w') as file:
        file.writelines(data)
    print("Python built in sort execution time:  %s seconds" % (time.time() - start_time))


def checkpoint_score(game, player):
    """
    Assigns a score to a set of moves based on the amp's checkpoints

    Parameters
    ----------
    game : Game
        The game
    player : Player
        The player object of the moves

    Return
    ------
    str
        Returns the score as a string

    """

    coordinates = game.checkpoints_list[player.checkpoint]

    dist = math.hypot(float(coordinates[0] + tile_size / 2) - float(player.rect.x + tile_size / 2),
                  float(coordinates[1] + tile_size / 2) - float(player.rect.y + tile_size / 2))

    if player.checkpoint == 0:
        total_dist = math.hypot(float(coordinates[0] + tile_size / 2) - float(game.startx + tile_size / 2),
                                float(coordinates[1] + tile_size / 2) - float(game.starty + tile_size / 2))
    else:
        prev = game.checkpoints_list[player.checkpoint - 1]
        total_dist = math.hypot(float(coordinates[0] + tile_size / 2) - float(prev[0] + tile_size / 2),
                                float(coordinates[1] + tile_size / 2) - float(prev[1] + tile_size / 2))

    score = player.checkpoint + 1 - dist / total_dist
    if player.hit:
        score -= 2

    if score < 0:
        return format(score, '.4f')
    else:
        return format(score, '.5f')

def clear_moves():
    """
    Clears all contents from the moves file

    Parameters
    ----------
    None

    Return
    ------
    None

    """

    open(moves_path, 'w').close()