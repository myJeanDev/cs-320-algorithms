def placement(num_players, field):
    global collision_count
    collision_count = 0
    # input validation
    if num_players is None or field is None:
        return None
    players_remaining = num_players
    team_size = int(num_players/2)
    field_size = int(len(field[0]))
    mid_field = int(field_size/2)
    players_locations = [[],[]]
    while players_remaining > 0:
        team_boolean = players_remaining <= team_size
        # Right side
        if team_boolean:
            random_x = random.randint(mid_field, field_size-1)
        # Left side   
        else:
            random_x = random.randint(0, mid_field-1)
        random_y = random.randint(0, field_size-1)
        if field[random_x][random_y] == 0:
            field[random_x][random_y] = 1
            players_locations[team_boolean].append((random_x, random_y))
            players_remaining -= 1
        else:
            clear_terminal()
            collision_count += 1
    return tuple(players_locations)