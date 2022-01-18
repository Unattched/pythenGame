import random

inventory: list = []
default_grid: list = [["* " for i in range(0, 10)] for j in range(0, 10)]  # constant
running_grid: list = []
items: list = ["* ", "c "]  # [path, coin]
current_item = items[0]  # item player is on (defaults to path)


def display_grid(grid):
    for i in range(0, 10):
        for j in range(0, 10):
            if j == 9:
                print(grid[i][j])
            else:
                print(grid[i][j], end="")


def interact(item):
    if item == items[0]:
        return False
    else:



def generate_upper_area(grid):
    player_row = grid[9]
    grid.clear()
    for i in range(0, 9):
        row = []
        for j in range(0, 10):
            item_index = random.randint(0, 10)
            if item_index > 8:
                row.append(items[1])  # gold coin
            else:
                row.append(items[0])  # path
        grid.append(row)
    grid.append(player_row)


def save(grid):
    pass


def set_player(grid):
    player_start_y = random.randint(0, 9)
    player_start_x = random.randint(0, 9)
    grid[player_start_y][player_start_x] = "P "
    return player_start_x, player_start_y


def movement(x_pos: int, y_pos: int, grid: list):
    global current_item
    direction: str = input("Please chose a direction of travel, Up (u), Down (d), Left (l) or Right (r): ").lower()
    while direction not in ['r', 'l', 'u', 'd']:
        direction: str = input(
            "Please chose a direction of travel, Up (u), Down (d), Left (l) or Right (r): ").lower()
    if direction == 'u':
        if y_pos != 0:
            s_y_pos = y_pos - 1
            grid[y_pos][x_pos] = current_item
            current_item = grid[s_y_pos][x_pos]
            grid[s_y_pos][x_pos] = "P "
            display_grid(grid)
            interact(current_item)
        else:
            s_y_pos = len(default_grid[0]) - 1
            grid[y_pos][x_pos] = items[0]
            grid[s_y_pos][x_pos] = "P "
            generate_upper_area(grid)
            display_grid(grid)
        save(grid)
        movement(x_pos, s_y_pos, grid)


def main():
    with open("Saves", "r", encoding="utf-8") as s:
        if s.read() == "":
            global running_grid
            running_grid = default_grid
            print("Initializing new game")
            start_x, start_y = set_player(running_grid)
            display_grid(running_grid)
            print(start_x)
            print(start_y)
            print(running_grid[start_y][start_x])
            movement(start_x, start_y, running_grid)


main()