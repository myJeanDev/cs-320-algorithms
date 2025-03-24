# Load a file of distances

def _validate_distances(distances, cities):
    for city_one in cities:
        for city_two in cities:
            if (city_one, city_two) not in distances:
                print(f"Missing {city_one, city_two} distance")
                return False
    return True


def load_dist(filename):
    distances = {}
    cities = set()
    with open(filename, mode='r') as f:
        for line in f:
            line = line.strip()
            if (len(line) == 0) or (line[0] == '#'):
                continue
            A, B, distance_string = line.split(",")
            A = A.strip()
            B = B.strip()

            distance_string = distance_string.strip()
            distance = int(distance_string)
            distances[(A, B)] = distance
            distances[(B, A)] = distance
            if A not in cities:
                distances[(A, A)] = 0
                cities.add(A)
            if B not in cities:
                distances[(B, B)] = 0
                cities.add(B)

    if not _validate_distances(distances, cities):
        return None, None
    return sorted(list(cities)), distances
