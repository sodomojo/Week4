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
ships = ["Battleship CHARLIE", "Battleship DEE", "Battleship FRANK", "Battleship DENNIS", "Battleship CRICKET", "Battleship MAC",
         "Battleship ARTEMIS", "Battleship GAIL", "Battleship MCPOYLE"]

game_pieces = dict(zip(location, ships))

# Intro for the Battleship game
def intro():
    print ("Let's play Battleship! \n\n"
    "Scattered across the board are various single-coordinate enemy Battleships that you need to seek and destroy.\n"
    "Find the battleships by inputting a single missile coordinate using a combination of A through D across and 1 through 8 vertically (ex: A5 or D3).\n"
    "Choose your coordinates wisely -- you only have 5 guesses to take out the enemy.\n\n"
    "Good luck!\n")
intro()


# global values
global coordinate
global coordinate_value
global guesses

# create empty list to store all the correct coordinate guesses
battleships = []

def game():
    for x in game_pieces:
        # ask the user for a coordinate input
        coordinate = input("Enter a coordinate to sink a battleship!: ")
        coordinate_value = coordinate.upper()
        guesses = 0
        if coordinate_value in game_pieces.keys():
            # print the coordinate and the ship name.
            # add the coordinate to the battleship list
            print("Bullseye! You chose {} and you sank the {}  ".format(coordinate_value, game_pieces[coordinate_value]))
            battleships.append(coordinate_value)
            game()
        elif coordinate_value not in game_pieces.keys():
            # show if their coordinate misses
            print("Sorry, there is no Battleship at coordinate {}.  Please try again!".format(coordinate_value))
            guesses += 1
            game()
        else:
            break
        return guesses, battleships
game()

# if the user has 5 wrong guesses throw the game over screen
if guesses == 5:
    print("You lose!  Victory is mine!")

# if the number of coordinates added to the battleships list matches the number of location entries, print statement
if len(list(battleships)) == len(list(location)):
    print("You sunk all the battleships!  Well done!")
    input("Press any key to quit")
