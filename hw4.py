#!/usr/bin/env python

"""
This is a Battleship game simulator.  Two lists will be combined - one being the location of the ship and the other the name.
The user will enter a single coordinate to try and sink the ship.
After 5 incorrect guesses the game will end.
If the user finds them all they'll win the game.

"""
# locations of the ships
location = ["C5", "D4", "B7", "A5", "C8", "C7", "D8", "A1", "A7"]

# ship names
ships = ["Battleship Charlie", "Battleship Dee", "Battleship Frank", "Battleship Dennis", "Battleship Cricket", "Battleship Mac",
         "Battleship Artemis", "Battleship Gail", "Battleship McPoyle"]

game_pieces = dict(zip(location, ships))

# Intro for the Battleship game
def intro():
    print ("Let's play Battleship! \n\n"
    "Scattered across the board are various single-coordinate enemy Battleships that you need to seek and destroy.\n"
    "Find the battleships by inputting coordinates using a combination of A through D across and 1 through 8 vertically (ex: A5 or D3).\n"
    "Choose your coordinates wisely -- you only have 5 guesses to take out the enemy.\n\n"
    "Good luck!\n")
    # global variable that can be consumed by set

intro()

# global values
global coordinate
global coordinate_value
global guesses

battleships = {}

def game():
    for x in game_pieces:
        coordinate = input("Enter a coordinate to sink a battleship!: ")
        coordinate_value = coordinate.upper()
        guesses = 0
        if coordinate_value in game_pieces.keys():
            print("Bullseye! You chose {} and you sank the {}  ".format(coordinate_value, game_pieces[coordinate_value]))
            battleships.append(game_pieces.values())
            game()
        elif coordinate_value not in game_pieces.keys():
            guesses += 1
            print("Sorry, you missed.  Try again")
            game()
        else:
            break
    return guesses, coordinate_value, coordinate, battleships
game()

if guesses == 5:
    print("You lose!  Victory is mine!")

if len(list(battleships())) == 9:
    print("You sunk all the battleships!  Well done!")
    input("Press any key to quit")


