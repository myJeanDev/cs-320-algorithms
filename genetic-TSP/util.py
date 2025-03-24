# Provides utility functions:

# A cost function for a path.
def cost(path, distances):
    if (len(distances) != (len(path) * len(path))):
        return None
    if (not valid_path(path)):
        return None
    result = 0
    for i in range(0, len(path)):
        result += distances[(path[i - 1], path[i])]
    return result

# 3. Confirms if a path is valid.
def valid_path(path):
    for c in path:
        count = 0
        for c2 in path:
            if (c2 == c):
                count += 1
        if (count > 1):
            return False
    return True

# Finds the lowest cost (best cost) path in a population.
def best_path(list_of_paths, distances):
    bp = list_of_paths[0]  # best path
    bc = cost(bp, distances)  # corresponding best cost
    for p in list_of_paths:
        if (cost(p, distances) < bc):
            bp = p
            bc = cost(p, distances)
    return bp
