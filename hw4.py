#!/usr/bin/env python

"""
These lists should match up, so Alice’s age is 20, Bob’s age is 21, and so on.

Use the zip function to merge these lists into a dictionary. (What data type does zip() return? How do you coerce that to the right data type?)
The names should be the keys, and the age should be the value.
Ask the user to input a user name
Use a while loop to keep asking the user to input a user until they find someone in the dictionary, give them up to five tries by using a counter outside the while loop
Return the user's age, as shown below
Your program should print out the response, as follows:

"Please input an user to find out their age: "
"Alice"
"Alice is 57!"

"Tabitha"
"There is nobody here named Tabitha, please try again: "
"""
location = ["C5", "D4", "B7", "A5", "C8", "C7", "D8", "A1", "A7"]

ships = ["U.S.S. Charlie", "U.S.S. Dee", "U.S.S. Frank", "U.S.S. Dennis", "U.S.S. Cricket", "U.S.S. Mac", "U.S.S. Artemis",
         "U.S.S. Gail", "U.S.S. McPoyle"]

game_pieces = dict(zip(location, ships))


def intro():
    print ("Let's play Battleship! \n\n"
    "Scattered across the board are various single-coordinate enemy Battleships that you need to seek and destroy.\n"
    "Find the battleships by inputting coordinates using a combination of A through D across and 1 through 8 vertically (ex: A5 or D3).\n"
    "Choose your coordinates wisely -- you only have 5 guesses to take out the enemy.\n\n"
    "Good luck!\n")
    global coordinate
    coordinate = input("Enter a coordinate to sink a battleship!: ")
    coordinate = coordinate.upper()
    return coordinate

intro()

global guesses

def coordinate():
    guesses = 0
    while coordinate != game_pieces.keys():
        print("Sorry, you missed.  Try again")
        guesses += 1
    if coordinate in game_pieces.keys():
        print("Bullseye! You sank {}".format(game_pieces.ships()))

coordinate()


def game_over():
    if guesses == 5:
        print("You lose!  Victory is mine!")

game_over()

