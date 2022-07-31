"""
    -------BATTLESHIPS-------
    Pre-reqs: Loops, Strings, Arrays, 2D Arrays, Global Variables, Methods
    How the game will function:
    1. A 10x10 grid will have 8 ships of variable length randomly placed around
    2. You will have 50 bullets to take down the ships that are in place
    3. You can choose a row and column such as A3 to indicate where to shoot
    4. For every shot that hits or misses it will show up in the grid
    5. A ship cannot be placed diagonally, so if a shot hits a part of
        a ship it would be in one of 4 directions, left, right, up, and down
    6. If all ships are found before using up all bullets, you win
        else, you lose     
    Battlemap description:
    1. "." = water or empty space
    2. "O" = part of a ship
    3. "X" = part of a ship that was hit with a bullet
    4. "#" = water that was shot with a bullet, a miss because it hit no ship
"""

# Global variable for grid
grid = [[]]
# Global variable for grid size
grid_size = 10
# Global variable for number of ships to be placed
num_of_ships = 8
# Global variable for bullets left
bullets_left = 50
# Global variable for game over
game_over = False
# Global variable for number of ships sunk
num_of_ships_sunk = 0
# Global variable for ship positions
ship_positions = [[]]
# Global variable for alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

