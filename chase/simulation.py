import numpy as np
import random
init_pos_limit = 10.0
turn_number = 50
sheep_number = 15
sheep_move_dist = 0.5
wolf_move_dist = 1.0


def rand_position():
    x = random.uniform(-init_pos_limit, init_pos_limit)
    y = random.uniform(-init_pos_limit, init_pos_limit)
    vector = np.array([x, y])
    return vector


def rand_sheeps():
    sheeps = []
    for i in range(sheep_number):
        sheeps.append(rand_position())
    return sheeps


def normalize_vector(vector):
    return vector/np.linalg.norm(vector)


def rand_sheep_move():
    _ = random.randint(0, 3)
    direction = {
        0: np.array([0, sheep_move_dist]),
        1: np.array([0, -sheep_move_dist]),
        2: np.array([sheep_move_dist, 0]),
        3: np.array([-sheep_move_dist, 0])
    }
    return direction.get(_)


def move_sheeps(sheep_list):
    _ = []
    for sheep in sheep_list:
        _.append(np.add(sheep, rand_sheep_move()))
    return _


if __name__ == '__main__':
    wolf_pos = np.array([0, 0])
    sheep_pos = rand_sheeps()

    for round_no in range(turn_number):
        sheep_pos = move_sheeps(sheep_pos)
        nearest = None
        for i, sheep in enumerate(sheep_pos):
            v = np.subtract(sheep, wolf_pos)
            d = np.linalg.norm(v)
            if nearest is None:
                nearest = [i, d]
            else:
                if nearest[1] > d:
                    nearest = [i, d]
        if nearest[1] <= wolf_move_dist:
            wolf_pos = sheep_pos[nearest[0]]
            sheep_pos.pop(nearest[0])
            print("Owca zjedzona")
        else:
            v = np.subtract(sheep_pos[nearest[0]], wolf_pos)
            nv = np.multiply(normalize_vector(v), wolf_move_dist)
            wolf_pos = np.add(wolf_pos, nv)
        print("Tura numer:", round_no + 1)
        print("Pozycja wilka:", wolf_pos)
        print("Liczba żywych owiec:", len(sheep_pos))
