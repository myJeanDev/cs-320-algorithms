Inputs:
    num_players: a non-negative integer that represents the number of players to be placed.
    field: a tuple of tuples that represent the grid, the field will always be n x n and divisible by 2, each cell in the grid is either occupied or unoccupied.
Error Handling:
    if field is None return None
    if num_players < 0 return None
Operations:

Outputs:
    GreenTeamPlacements = ((x,y),(x,y))
    GoldTeamPlacements = ((x,y),(x,y))
    players_positions: [GreenTeamPlacements, GoldTeamPlacements]

This lab involves placing a given number of 'players' onto an (n x n) Grid called the field.
If a Player is on Green team, they must be placed on the left side of the field.
If a Player is on Gold team, they must be placed on the right side of the field.
The field will always be divisible by 2

Players must be placed randomly within the bounds of their area, a player cannot be placed on an occupied cell.
Every unoccupied cell must have an equal probability to have a player placed within it.