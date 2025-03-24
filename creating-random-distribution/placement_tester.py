import collections
import main
import os

loading_step = 0
loading_animation = ["/", "~", "\\", "|", "/", "~", "\\", "|"]

def display_grid(grid):
    print("===")
    for row in grid:
        print(' '.join(str(value) for value in row))
    print('\n')


def clear_terminal():
    global loading_step
    os.system('cls' if os.name == 'nt' else 'clear')
    if loading_step >= len(loading_animation):
        loading_step = 0
    print(f"Collision Count:{main.collision_count} {loading_animation[int(loading_step)]}")
    loading_step += 0.01


def test_placement(num_players, field_size, trial_count):
    print("==================================")
    print(f"\nNum_players: {num_players} field_size: {field_size}x{field_size}")
    for _ in range(0, trial_count):
        field = [[True for _ in range(field_size)] for _ in range(field_size)]
        average_frequency = (num_players / (field_size - (0 + 1)))
        players_placed = [[], []]
        players_placed[0], players_placed[1] = main.placement(num_players, tuple(field))
        players_x_values = []
        players_y_values = []
        for team in players_placed:
            for player in team:
                players_x_values.append(player[0])
                players_y_values.append(player[1])
        number_frequencies_x = collections.Counter(players_x_values)
        number_frequencies_y = collections.Counter(players_y_values)

        frequency_tolerance = average_frequency * 1000
        for number, frequency in number_frequencies_x.items():
            if not abs(average_frequency - frequency) < frequency_tolerance:
                print(f"X Values: frequency of {number} is {frequency}, expected {average_frequency}")
                return
        for number, frequency in number_frequencies_y.items():
            if not abs(average_frequency - frequency) < frequency_tolerance:
                print(f"Y Values: frequency of {number} is {abs(average_frequency - frequency)} more than expected")
                return
        print(f"Players Placed: {len(players_placed[0]) + len(players_placed[1])}")
        print(players_placed[0], players_placed[1])


test_placement(10, 10, 10)