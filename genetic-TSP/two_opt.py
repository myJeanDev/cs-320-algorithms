# 2-opt algorithm.
from util import cost


def two_opt_swap(path, c1, c2):
    new_path = [None] * len(path)
    for c in range(0, c1):
        new_path[c] = path[c]
    for c in range(0, c2 - c1 + 1):
        new_path[c1 + c] = path[c2 - c]
    for c in range(c2 + 1, len(path)):
        new_path[c] = path[c]
    return tuple(new_path)


def two_opt_round(path, dict):
    best_cost = cost(path, dict)
    for i in range(0, len(path) - 1):
        for j in range(i + 1, len(path)):
            new_path = two_opt_swap(path, i, j)
            if (cost(new_path, dict) < best_cost):
                return new_path
    return path


def two_opt(path, dict):
    new_cost = cost(path, dict)
    best_cost = new_cost + 1
    new_path = path
    while (new_cost < best_cost):
        best_cost = new_cost
        new_path = two_opt_round(new_path, dict)
        new_cost = cost(new_path, dict)

    return new_path
