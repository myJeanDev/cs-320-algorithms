import random  # optional and you can delete this line if not useful


def contains_duplicates(tuples):
    exists = set()
    for t in tuples:
        if t in exists:
            return True
        exists.add(t)
    return False


def placement(num_players, field):
    # input validation
    if field is None or not isinstance(num_players, int) or num_players <= 0:
        return None
    
    field_size = len(field)
    if field_size == 0 or field[0] is None or len(field[0]) != field_size:
        return (), ()

    # create decks of unoccupied locations, this section is making the algorithm O(n^2)
    left_locations = []
    right_locations = []
    
    # Left
    for x in range(field_size // 2):
        for y in range(field_size):
            if field[x][y]:
                left_locations.append((x, y))

    # Right
    for x in range(field_size // 2, field_size):
        for y in range(field_size):
            if field[x][y]:
                right_locations.append((x, y))
          
    num_players_final = min(num_players, len(left_locations), len(right_locations))

    if num_players_final == 0:
        return (), ()
    
    # creates lists made from a 'team_size' amount of random locations
    green_team_positions = random.sample(left_locations, num_players_final)
    gold_team_positions = random.sample(right_locations, num_players_final)

    combined_positions = green_team_positions + gold_team_positions
    if contains_duplicates(combined_positions):
        pass
    return tuple(green_team_positions), tuple(gold_team_positions)
