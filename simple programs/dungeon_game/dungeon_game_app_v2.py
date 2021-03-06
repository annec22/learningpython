# Filename: dungeon_game_app_v2.py
# Versions: Python 3
# Opposite of number_game_app.py. A simple python programming app that showcases use of:
#	- python collections
#	- loops, use while-else
#	- functions, call function within itself
#	- user input
#	- importing libraries
#	- exceptions
# Features:
#	- 2d user interface
#   - draw the grid
#   - pick random location for the player
#   - pick random location for the exit door
#   - pick random location for the monster
#   - draw the player in the grid
#   - take input for movement
#   - move player, unless invalid move
#   - check for win/loss
# clear screen and redraw grid
# To do:
#   - let monster move
#   - additional monster

import random
import os


CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_locations():
    return random.sample(CELLS,3)

def move_player(player, move):
    x,y = player
    if move == "LEFT":
        x -= 1
    if move == "RIGHT":
        x += 1
    if move == "UP":
        y -= 1
    if move == "DOWN":
        y += 1
    return x,y

def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x,y = player
    if y == 0:
        moves.remove("UP")
    if y == 4:
        moves.remove("DOWN")
    if x == 0:
        moves.remove("LEFT")
    if x == 4:
        moves.remove("RIGHT")
    return moves

def draw_map(player):
    print(' _'*5)
    tile = "|{}"

    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output,end=line_end)

def play_game():
    monster, door, player = get_locations()
    print("The monster is in : {}".format(monster)) #debug line
    print("The door is in : {}".format(door)) #debug line
    moves = get_moves(player)
    print("Welcome to the dungeon!")
    print("Enter QUIT to quit")
    input("Press ENTER to start")
    clear_screen()

    game_over = False
    while not game_over:
        draw_map(player)
        print("You're currently in room {}".format(player)) # fill with player position
        print("You can move {}".format(','.join(moves))) #fill  with available moves
        moves = get_moves(player)
        move = input(">  ")
        move = move.upper()
        if move == 'QUIT':
            break
        elif move not in moves:
            # Bad move? Don't change anything!
            clear_screen()
            print("That move is not valid!")
            continue
            # Otherwise, loop back around
        else:
            # Good move? Change the player position
            player = move_player(player, move)
            if player == door:
                # On the door? They win!
                print("Yay! You win!")
            elif player == monster:
                # On the monster? They lose!
                print("You woke up the monster! You lose!")
            else:
                clear_screen()
                print("Go..Keep moving..")
                continue
            game_over = True
    else:
        play_again = input("Do you want to play again? Y/N: ").upper()
        if play_again == "Y":
            clear_screen()
            play_game()
        print("Bye now!")


play_game()
